# runGUI.py
# Nicholas Killeen,
# 31st July 2016.
# Runs a graphical user interface for the Propositional Logic Engine.

import os;

from PySide.QtCore import *;
from PySide.QtGui import *;
from PySide.QtWebKit import *;

import FactDatabase;
import Fraction;
import Interface;
import Processor;
import QuantumCounter;
import Relation;

import FactDatabase.FactDatabase as FactDatabase;
import Fraction.Fraction as Fraction;
import Interface.Interface as Interface;
import Processor.Processor as Processor;
import QuantumCounter.QuantumCounter as QuantumCounter;
import Relation.Relation as Relation
import runCLI;

MAX_RELATION_SYMBOLS_FOR_TESTING = 7;
# the maximum number of symbols that can be in a fact before the engine
# decides that the length of time involved in processing is detrimental
# to workflow
LARGEST_SYMBOL = 999;
# the largest valid symbol value

SAVE_PATH = "../Saves/";
FILE_TYPE = ".ple"

GInterface = None;
# global Interface object

def runGUI():
    # Class to bridge JavaScript and Python. Is a member of runGUI such
    # that the Object contents can be accessed without globals.
    class Bridge(QObject):
        @Slot(str)
        def addFact(this, relationConstructor):
            relationConstructor = runCLI._transpose(
                relationConstructor);
            factRelation = Relation.Relation(relationConstructor);
            GInterface.addFact(factRelation);

        @Slot(str)
        def eliminateSymbol(this, symbolNumber):
            GInterface.eliminateSymbol(int(symbolNumber));

        def evalJavaScript(this, script):
            contents.page().mainFrame().evaluateJavaScript(script);

        @Slot(str)
        def getSymbolList(this, relationConstructor):
            relationConstructor = runCLI._transpose(
                relationConstructor);
            isValidToCheckSymbols = _isRelationPseudoValid(
                relationConstructor);
            if (isValidToCheckSymbols):
                relation = Relation.Relation(relationConstructor);
                symbolList = relation.getSymbolList();
                this.evalJavaScript("Python.register = {0};".format(str(
                    symbolList)));
            else:
                # calling Relation.getSymbolList would throw an error
                this.evalJavaScript("Python.register = [];");

        # Method to be called manually after QObject.__init__.
        def initiate(this):
            global GInterface;
            GInterface = Interface.Interface(this.processError);

        @Slot(str)
        def isValid(this, relationConstructor):
            relationConstructor = runCLI._transpose(
                relationConstructor);
            relation = Relation.Relation(relationConstructor);
            isValidToCheckSymbols = _isRelationPseudoValid(
                relationConstructor);
            if (isValidToCheckSymbols):
                symbolList = relation.getSymbolList();
                if (len(symbolList) > 0 and max(symbolList) > 
                    LARGEST_SYMBOL):
                    this.evalJavaScript("Python.register = false;");
                elif (len(symbolList) > 
                    MAX_RELATION_SYMBOLS_FOR_TESTING):
                    this.evalJavaScript("Python.register = \"maybe\";");
                else:
                    isRelationValid = relation.isValid(); 
                    # this test completes the suite internal to 
                    # Relation.isValid()
                    if (isRelationValid):
                        this.evalJavaScript("Python.register = true;");
                    else:
                        this.evalJavaScript("Python.register = false;");
            else:
                this.evalJavaScript("Python.register = false;");

        @Slot(str)
        def load(this, fileAddress):
            try:
                file = open("{0}{1}{2}".format(SAVE_PATH, fileAddress, 
                    FILE_TYPE), 'r');
                fileString = file.read();

                while (fileString.count('\'') != 0):
                    fileString = fileString.replace('\'', "");
                    # the neglection of this replacement poses a serious
                    # security threat, whereby files can be manually
                    # engineered to behave otherwise like normal files,
                    # but can take partial or full control of the system
                    # through a process analagous to XSS attacks (this
                    # risk exists since eval(str) is being used to allow
                    # interaction between JS and Python)
                    # to handle this risk, any illegal characters are
                    # removed (as above), and processing then proceeds
                    # as normal

                this.evalJavaScript(
                    "Python.register = \"1\" + '{0}';".format(str(
                        fileString)));
                # '1' is a control character for whether or not the file
                # was successfully opened

                file.close();
                # the file doesn't need to be closed if it was never
                # instantiated correctly

            except Exception as error:
                this.evalJavaScript("Python.register = \"0\"");

        def processError(this, arg):
            this.evalJavaScript("Python.mapError(\"{0}\");".format(
                arg));

        @Slot(str)
        def request(this, requestStr):
            requestRelation = Relation.Relation(requestStr);
            if (requestRelation.isValid()):
                GInterface.setRequest(requestRelation);
                handler = GInterface.generateProcessor();
                handler();
                response = GInterface.retrieveResponse();
                constituentList = [];
                runCLI._formatSoughtInformation(response, 
                    constituentList.append);
            
                # the constituentList array can be abbreviated at this
                # point by the general rule [0][1] + [0](1 - [1]) = [0],
                # but it is not a feature required for full 
                # functionality

                # transfer constituents to JavaScript front-end
                constituentNumber = 0;
                numConstituents = len(constituentList);
                while (constituentNumber < numConstituents):
                    currentConstituent = constituentList[
                        constituentNumber];

                    isConstituentInfinite = False;
                    if (len(currentConstituent) > 1):
                        isConstituentInfinite = (
                            currentConstituent[0] == '1' and 
                            currentConstituent[1] == '/');
                        # the truth of this implies that the constituent
                        # has a coefficient 1/0

                    if (isConstituentInfinite):
                        this.evalJavaScript("Python.cacheInf[Python.cac"
                            "heInf.length] = \"{0}\";".format(
                                currentConstituent));
                    else:
                        this.evalJavaScript("Python.cache[Python.cache."
                            "length] = \"{0}\";".format(
                                currentConstituent));
                    constituentNumber += 1;
                this.evalJavaScript("Python.onProcessorFinish();");
            
                # empty GInterface
                numFacts = len(GInterface.getFactList());
                while (numFacts != 0):
                    GInterface.deleteFact(0);
                    numFacts = len(GInterface.getFactList());
            else:
                this.processError("Failed to set request: request is ma"
                    "lformed.");

        @Slot(str, str)
        def save(this, data, fileAddress):
            _resolveSaveDirectory();
            try:
                file = open("{0}{1}{2}".format(SAVE_PATH, fileAddress, 
                    FILE_TYPE), 'w');
                file.write(data);
                file.close();
            except Exception as error:
                this.evalJavaScript("Python.register = \"0\"");

    GUIhtml = open("PLE/GUI.html", 'r');
    htmlContent = GUIhtml.read();
    GUIhtml.close();
    htmlContent = htmlContent[htmlContent.find("<!DOCTYPE html>"):];
    # removes all header garbage before "<!DOCTYPE html>"

    # create a window
    PLE = QApplication([]);
    window = QWidget();
    window.setWindowTitle("Propositional Logic Engine");
    MARGIN_PX = -11;
    window.setContentsMargins(MARGIN_PX, MARGIN_PX, MARGIN_PX, 
        MARGIN_PX);
    contents = QWebView();

    # bind the JavaScript and Python classes "Bridge"
    bridge = Bridge();
    bridge.initiate();
    contents.page().mainFrame().addToJavaScriptWindowObject("Bridge",
        bridge);

    # display the window
    contents.setHtml(htmlContent);
    layout = QVBoxLayout();
    layout.addWidget(contents);
    window.setLayout(layout);
    window.show();

    # run
    PLE.exec_();

# Determines whether a Relation is pseudo-valid, that is, does it meet
# all of the validity criteria that do not require lengthy evaluation.
def _isRelationPseudoValid(relationConstructor):
    isValid = Relation._areAllCharactersLegal(relationConstructor);
    if (isValid):
        isValid = Relation._areCombinationsLegal(relationConstructor);
    if (isValid):
        isValid = Relation._isNestingLegal(relationConstructor);
    if (isValid):
        isValid = Relation._areNumbersLegal(relationConstructor);
    return isValid;

# Instantiates the save/load file path if it does not already exist.
def _resolveSaveDirectory():
    if (not os.path.exists(SAVE_PATH)):
        os.makedirs(SAVE_PATH);

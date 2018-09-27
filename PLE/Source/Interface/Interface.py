# Interface/Interface.py
# Nicholas Killeen,
# 24th July 2016.
# Interfacing class for a Propositional Logic Engine, allowing facts to
# be entered in mathematical form, and queries to be asked and answered.

import FactDatabase;
import Relation;
import QuantumCounter;
import Processor;
import Fraction;
import FactDatabase.FactDatabase as FactDatabase;
import Relation.Relation as Relation;
import QuantumCounter.QuantumCounter as QuantumCounter;
import Processor.Processor as Processor;
import Fraction.Fraction as Fraction;

# Class defining methods of interaction between a caller and an internal
# instance of FactDatabase.
class Interface:
    def __init__(this, errorOutputMethod = None):
        if (errorOutputMethod == None):
            errorOutputMethod = lambda errorMessage: None;
            # by default, errors are suppressed
        this.errorOutputMethod = errorOutputMethod;
        this.factDatabase = FactDatabase.FactDatabase();
        this.isRequestValid = False;
        this.processor = None;
        this.request = None;
        this.eliminatedSymbols = [];

    def addFact(this, fact):
        successState = this.factDatabase.appendFact(fact);
        if (successState == False):
            this.errorOutputMethod("Failed to append fact: fact is "
                "malformed.");

    def deleteFact(this, factNumber):
        successState = this.factDatabase.deleteFact(factNumber);
        if (successState == False):
            this.errorOutputMethod("Failed to delete fact: fact is out "
                "of range");
      
    def eliminateSymbol(this, symbolNumber):
        this.eliminatedSymbols.append(symbolNumber);

    # Returns a handle to the processor, through which the process can
    # be enacted.
    def generateProcessor(this):
        handler = None;
        if (this.isRequestValid):
            aggregate = this.factDatabase.getFactAggregation();
            currentSymbolNumber = 0;
            numSymbolsToEliminate = len(this.eliminatedSymbols);
            while (currentSymbolNumber < numSymbolsToEliminate):
                aggregate.eliminateSymbol(this.eliminatedSymbols[
                    currentSymbolNumber]);
                currentSymbolNumber += 1;

            this.eliminatedSymbols = [];

            request = this.getRequest();
            requestSymbolList = request.getSymbolList();
            totalWork = 2 ** len(requestSymbolList);
            coefficientMap = QuantumCounter.QuantumCounter();
            coefficientMap.createCoefficientMap(requestSymbolList);
            this.processor = Processor.Processor(aggregate, request, 
                coefficientMap, totalWork);
            handler = this.processor.go;
        else:
            this.errorOutputMethod("Failed to declare environment: "
                "request is not defined.");
        return handler;

    def getFactList(this):
        return this.factDatabase.getFactList();

    # Recall the currently set request.
    def getRequest(this):
        request = None;
        if (this.isRequestValid):
            request = this.request;
        else:
            this.errorOutputMethod("Failed to get request: request is "
                "not defined.");
        return request;

    def retrieveResponse(this):
        returnValue = None;
        if (this.processor == None):
            this.errorOutputMethod("Failed to retrieve fraction: no "
                "processor has been generated.");
        else:
            if (this.processor.hasFinished()):
                returnValue = _aggregateResponse(this.processor);
            else:
                this.errorOutputMethod("Failed to retrieve fraction -- "
                    "the processor is not ready.");
        return returnValue;

    def setRequest(this, request):
        isValid = request.isValid();
        this.isRequestValid = isValid;
        if (isValid):
            this.request = request;
        else:
            this.errorOutputMethod("Failed to set request: request is "
                "malformed");

def _aggregateResponse(repository):
    productWith0 = repository.getProductWith0();
    productWith1 = repository.getProductWith1();
    numerator = productWith0;
    denominator = productWith0 - productWith1;
    return Fraction.Fraction(numerator, denominator);

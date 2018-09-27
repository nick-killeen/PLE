# runCLI.py
# Nicholas Killeen,
# 27th June 2016.
# Runs a command line interface for the Propositional Logic Engine,
# with limited functionality.

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
import Relation.Relation as Relation;

def runCLI():
    interface = Interface.Interface(print);
    userWishesToExit = False;
    print("Running PLE, welcome!");
    print("Press the return key twice to quit.");
    while (not userWishesToExit):
        command = input("\n1. Add a fact"
            "\n2. Delete a fact"
            "\n3. Show a list of facts "
            "\n4. Request a solution\n>>> ");
        if (command == "1"):
            # add
            constructor = input("Enter the fact to add:\n>>> ");
            constructor = _transpose(constructor);
            fact = Relation.Relation(constructor);
            interface.addFact(fact);
        elif (command == "2"):
            # delete
            rawInput = input("Enter the fact number to delete:\n>>> ");
            try: 
                factNumberToDelete = int(rawInput) - 1;
                interface.deleteFact(factNumberToDelete);
            except Exception as error:
                print("Could not delete fact.");
        elif (command == "3"):
            # show list (in transposed form)
            factList = interface.getFactList();
            factNumber = 0;
            numFacts = len(factList);
            while (factNumber < numFacts):
                currentFactStr = factList[factNumber].data;
                print("{0} -> {1}".format(factNumber + 1, 
                    currentFactStr));
                factNumber += 1;
            if (numFacts == 0):
                print("There are no facts.");
        elif (command == "4"):
            # request solution
            request = Relation.Relation(input("Enter the request:\n>>> "
                ));
            if (request.isValid()):
                interface.setRequest(request);
                handler = interface.generateProcessor();
                handler();
                response = interface.retrieveResponse();
                _formatSoughtInformation(response, print);
            else:
                print("The request is malformed.");
        elif (command == ""):
            userWishesToExit = True;
        else:
            print("Did not recognise command.");

# Given a fraction, formats it as a development of constituents, whose
# respective coefficients can take the values 0, 1, 0/0, or 1/0.
def _formatSoughtInformation(fraction, outputMethod):
    numerator = fraction.getNumerator();
    denominator = fraction.getDenominator();
    involvedSymbolList = denominator.getSymbolList();
    coefficientMap = QuantumCounter.QuantumCounter();
    coefficientMap.createCoefficientMap(involvedSymbolList);
    
    coefficientNumber = 0;
    numCoefficients = 2 ** len(involvedSymbolList);
    while (coefficientNumber < numCoefficients):

        numeratorCopy = Relation.Relation();
        numeratorCopy.copyFrom(numerator);
        numeratorCopy.insertArguments(coefficientMap);
        currentNumerator = numeratorCopy.evaluate();

        denominatorCopy = Relation.Relation();
        denominatorCopy.copyFrom(denominator);
        denominatorCopy.insertArguments(coefficientMap);
        currentDenominator = denominatorCopy.evaluate();

        if (currentNumerator == 0 and currentDenominator == 0):
            outputMethod("0/0{0}".format(coefficientMap.toString()));
        elif (currentNumerator == 1 and currentDenominator == 1):
            outputMethod("1{0}".format(coefficientMap.toString()));
        elif (currentNumerator == 1 and currentDenominator == 0):
            outputMethod("1/0{0}".format(coefficientMap.toString()));
        # else the coefficient is naught (0/1), and does not need to
        # be printed

        coefficientMap.increment();
        coefficientNumber += 1;

# Function to convert Relations in the form "subject copula predicate"
# ("A = B") -- which the user understands easily -- to the more machine 
# understandable form "A(1 - B) + B(1 - A) = 0".
def _transpose(constructor):
    transposedConstructor = None;
    constructor = constructor.replace(" =", '=');
    constructor = constructor.replace("= ", '=');
    slicedConstructor = constructor.split('=');
    if (len(slicedConstructor) == 2):
        subject = slicedConstructor[0];
        predicate = slicedConstructor[1];
        transposedConstructor = ("({0})(1 - ({1})) + ({1})(1 - ({0}))"
            "").format(subject, predicate);
    else:
        # set the constructor to something illegal
        transposedConstructor = 'v';
    return transposedConstructor;

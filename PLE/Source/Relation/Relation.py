# Relation/Relation.py
# Nicholas Killeen,
# 19th June 2016.
# Class to store and algebraically manipulate Boolean relations.

import QuantumCounter;
import QuantumCounter.QuantumCounter as QuantumCounter;

# Stores and manipulates a connection of Boolean symbols.
# Unsafe unless Relation::isValid(this) -> True.
class Relation:
    def __add__(this, arg):
        return Relation(this.data + "+" + arg.data);

    def __eq__(this, arg):
        # compile a list of all symbols in the two Relations, then use
        # that list to construct a QuantumCounter as a coefficientMap
        symbolList = this.getSymbolList();
        symbolList.extend(arg.getSymbolList());
        symbolList = list(set(symbolList)); # remove any repeated items
        coefficientMap = QuantumCounter.QuantumCounter();
        coefficientMap.createCoefficientMap(symbolList);

        # iterate through every possible state of coefficients, if pairs
        # do not match from both relations, they are not equal
        numInvolvedSymbols = len(symbolList);
        numCoefficients = 2 ** numInvolvedSymbols;
        coefficientNumber = 0;
        hasEncounteredDiscrepancy = False;
        while (coefficientNumber < numCoefficients):
            relationA = Relation();
            relationA.copyFrom(this);
            relationA.insertArguments(coefficientMap);
            relationB = Relation();
            relationB.copyFrom(arg);
            relationB.insertArguments(coefficientMap);
            if (relationA.evaluate() != relationB.evaluate()):
                # not all non-zero coefficients are treated equally
                hasEncounteredDiscrepancy = True;
            coefficientMap.increment();
            coefficientNumber += 1;
        return not hasEncounteredDiscrepancy;

    def __init__(this, constructor = ""):
        this.data = constructor;

    def __mul__(this, arg):
        return Relation("(" + this.data + ")(" + arg.data + ")");

    def __ne__(this, arg):
        return not this == arg;

    def __sub__(this, arg):
        return Relation(this.data + "-(" + arg.data + ")");

    def copyFrom(this, source):
        this.data = source.data;

    def eliminateSymbol(this, symbolNumber):
        coefficientMap = QuantumCounter.QuantumCounter();
        coefficientMap.createCoefficientMap([symbolNumber]);

        relationWith0 = Relation();
        relationWith0.copyFrom(this);
        relationWith0.insertArguments(coefficientMap);

        coefficientMap.increment();
        relationWith1 = Relation();
        relationWith1.copyFrom(this);
        relationWith1.insertArguments(coefficientMap);

        resultOfElimination = relationWith0 * relationWith1;
        this.copyFrom(resultOfElimination);

    # Evaluates a Relation that contains no symbols.
    # Unsafe method; must not be called unless: 
    #  - Relation::isValid(this) -> True.
    #  - Relation::getSymbolList(this) -> [].
    def evaluate(this):
        evaluableString = this.data.replace(")(", ")*(");
        return eval(evaluableString);

    def getSymbolList(this):
        symbolList = [];
        symbolOccurrences = this.data.split(']');
        symbolOccurrences.pop();
        # the final element of symbolOccurrences is garbage, containing
        # the rest of the data string after the final symbol
        numOccurrences = len(symbolOccurrences);
        occurrence = 0;
        while (occurrence < numOccurrences):
            currentSymbolString = symbolOccurrences[occurrence];
            currentSymbolString = currentSymbolString.split('[')[1];
            currentSymbol = int(currentSymbolString);
            if (symbolList.count(currentSymbol) == 0):
                symbolList.append(currentSymbol);
            occurrence += 1;
        return symbolList;

    def insertArguments(this, quantumCounter):
        argumentMap = quantumCounter.read();
        argumentNumber = 0;
        numArguments = len(argumentMap);
        while (argumentNumber < numArguments):
            currentArgument = argumentMap[argumentNumber];
            if (currentArgument == 0 or currentArgument == 1):
                symbolToReplace = '[' + str(argumentNumber) + ']';
                replacementArgument = '(' + str(currentArgument) + ')';
                this.data = this.data.replace(symbolToReplace, 
                    replacementArgument);
            argumentNumber += 1;

    # Determines whether a Relation is invalid. Malformed Relations are
    # potentially unsafe.
    def isValid(this):
        dataString = this.data;
        isValid = _areAllCharactersLegal(dataString);
        if (isValid):
            isValid = _areCombinationsLegal(dataString);
            # check for disallowed character adjacencies
        if (isValid):
            isValid = _isNestingLegal(dataString);
            # check that each bracket occurs in a legal pair
        if (isValid):
            isValid = _areNumbersLegal(dataString); 
            # check that no numbers have trailing 0s
        if (isValid):
            isValid = (this == this * this); 
            # check that the expression exists in the Boolean domain, 
            # {0, 1}, as by the condition n = n^2
        return isValid;

    # Attempt to optimise the data a Relation instance stores.
    # Should only impact performance.
    def optimise(this):
        this.data = this.data.replace(' ', "");
        this.data = this.data.replace("(1)(", "(");
        this.data = this.data.replace(")(1)", ")");


def _areAllCharactersLegal(dataString):
    hasFoundIllegalChar = False;
    for character in dataString:
        if ("0123456789 +-()[]".count(character) == 0):
            hasFoundIllegalChar = True;
    return not hasFoundIllegalChar;

def _areCombinationsLegal(dataString):
    reducedData = dataString;

    # turn all numberical expressions into 'n'
    for digit in "0123456789":
        reducedData = _recursivelyReplace(reducedData, digit, 'n');
    reducedData = _recursivelyReplace(reducedData, "nn", 'n');

    # collapse all symbols "[n]", since they are equivalent to "(n)"
    reducedData = _recursivelyReplace(reducedData, "[n]", "(n)");

    # replace all multipliable terms 'n' with 'M'
    reducedData = _recursivelyReplace(reducedData, '(n)', "(M)");

    # replace all non-multiplable terms 'n' with "(B)"
    reducedData = _recursivelyReplace(reducedData, 'n', "(B)");

    # replace all '-' signs with '+', since they are of the same nature
    reducedData = _recursivelyReplace(reducedData, "-", "+");

    # remove all double whitespace as they are treated equally to single
    # spaces
    reducedData = _recursivelyReplace(reducedData, "  ", ' ');

    # flag the beginning and end of the string with "O", and then remove
    # meaningless whitespace at the start and end of the string
    reducedData = 'O' + reducedData + 'O';
    reducedData = reducedData.replace("O ", 'O');
    reducedData = reducedData.replace(" O", 'O');

    # search the reduced string for all possible illegal expressions
    LIST_OF_ILLEGAL_EXPRESSIONS = ["M)(B", "B)(M" , ") (", "()", "( )", 
        "++", "+ +", "+)", "(+", "[", "]", "OM", "OB", "O)", "O+", "+O",
        "(O", "BO", "MO", "OO", "B)(", ")(B"];
    hasFoundIllegalCombination = False;
    for expression in LIST_OF_ILLEGAL_EXPRESSIONS:
        if (reducedData.count(expression) != 0):
            hasFoundIllegalCombination = True;

    return not hasFoundIllegalCombination;

def _areNumbersLegal(dataString):
    # compile a list of all numbers
    involvedNumbers = [""];
    currentNumber = 0;
    for character in dataString:
        if ("0123456789".count(character) != 0):
            involvedNumbers[currentNumber] += character;
        elif involvedNumbers[currentNumber] != "":
            involvedNumbers.append("");
            currentNumber += 1;

    # check that each number has no leading zeros if it is more than
    # one digit long
    hasFoundIllegalNum = False;
    for number in involvedNumbers:
        if (len(number) > 1):
            if (number[0] == '0'):
                hasFoundIllegalNum = True;

    return not hasFoundIllegalNum;

def _isNestingLegal(dataString):
    # generate a list of all brackets
    listOfBrackets = "";
    for character in dataString:
        if (character == ')' or character =='('):
            listOfBrackets += character;
        elif (character == ']'):
            listOfBrackets += ')';
        elif (character == '['):
            listOfBrackets += '(';

    # eliminate all legal bracket pairs
    uneliminatedBrackets = _recursivelyReplace(listOfBrackets, "()", "");
    if (uneliminatedBrackets == ""):
        isBalanced = True;
    else:
        isBalanced = False;
    return isBalanced;

def _recursivelyReplace(string, searchTerm, replacementTerm):
    if (replacementTerm.count(searchTerm) != 0):
        assert(searchTerm == replacementTerm or string == "");
    stringBeforeChange = "";
    stringAfterChange = string;
    while (stringAfterChange != stringBeforeChange):
        stringBeforeChange = stringAfterChange; 
        stringAfterChange = stringBeforeChange.replace(searchTerm, 
            replacementTerm);
    return stringAfterChange;
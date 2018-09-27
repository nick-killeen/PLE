# QuantumCounter/QuantumCounter.py
# Nicholas Killeen,
# 19th June 2016.
# Object definition for a binary counter, supporting rudimentary quantum
# states.

# Class to count in binary, but skipping quantum bit states.
class QuantumCounter:
    def __init__(this, superPositionStates = []):
        this.bitStates = [];
        bitNumber = 0;
        numBits = len(superPositionStates);
        while (bitNumber < numBits):
            if (superPositionStates[bitNumber] == 0):
                this.bitStates.append(0);
            elif (superPositionStates[bitNumber] == 1):
                this.bitStates.append(1);
            else:
                this.bitStates.append(-1);
                # -1 is used to represent a quantum superposition, 
                # namely, something other than 0 or 1
            bitNumber += 1;

    # Simulate numIterations iterations.
    def add(this, numIterations):
        iteration = 0;
        while (iteration < numIterations):
            this.increment()
            iteration += 1;
        
    def copyFrom(this, source):
        this.bitStates = source.bitStates;

    # Set up a QuantumCounter, where the symbols in involvedSymbolList
    # take the value of 0, and all other symbols are in superposition.
    def createCoefficientMap(this, involvedSymbolList):
        largestSymbol = 0;
        if (len(involvedSymbolList) > 0):
            largestSymbol = (max(involvedSymbolList));
        coefficientArray = [-1] * (largestSymbol + 1);
        for symbol in involvedSymbolList:
            coefficientArray[symbol] = 0;
        coefficientMap = QuantumCounter(coefficientArray);
        this.copyFrom(coefficientMap);

    # Increment the current state of the counter, moving over quantum
    # bits. Overflow resets the counter.
    def increment(this):
        bitNumber = len(this.bitStates) - 1;
        carry = 1;
        # iterate over each bit, right to left, stop if there is no
        # longer a bit to carry
        while (bitNumber >= 0 and carry == 1):
            currentState = this.bitStates[bitNumber];
            if (currentState == 0):
                this.bitStates[bitNumber] = 1;
                carry = 0;
            elif (currentState == 1):
                this.bitStates[bitNumber] = 0;
            bitNumber -= 1;

    def read(this):
        return this.bitStates;

    def toString(this):
        string = "";
        bitNumber = 0;
        numBits = len(this.bitStates)
        while (bitNumber < numBits):
            currentBit = this.bitStates[bitNumber];
            if (currentBit == 0):
                string += "(1 - [{0}])".format(bitNumber);
            elif (currentBit == 1):
                string += "[{0}]".format(bitNumber);
            bitNumber += 1;
        return string;
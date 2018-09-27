# Processor/Processor.py
# Nicholas Killeen,
# 19th June 2016.
# Module to perform mass calculations so as to generate a partial answer
# to a request from the P.L.E.

import Relation;
import QuantumCounter;
import Relation.Relation as Relation;
import QuantumCounter.QuantumCounter as QuantumCounter;

# Class to calculate the products of coefficients in a representative
# aggregation of facts with respect to the list of symbols that comprise
# a request, and then, sort these coefficients into two piles.
class Processor:
    def __init__(this, aggregate, soughtDevelopment, quantumCounter, 
        numIterations):
        this.aggregate = aggregate;
        this.finishedProcessing = False;
        this.productWith0 = Relation.Relation("1");
        this.productWith1 = Relation.Relation("1");
        this.quantumCounter = quantumCounter;
        this.remainingIterations = numIterations;
        this.soughtDevelopment = soughtDevelopment;

    def getProductWith0(this):
        return this.productWith0;

    def getProductWith1(this):
        return this.productWith1;

    # Iterates through numIterations coefficient maps, and stores the
    # results locally to be retrieved with getProductWith0 /
    # getProductWith1.
    def go(this):
        while (this.remainingIterations > 0):
            fullDevelopmentCopy = Relation.Relation();
            fullDevelopmentCopy.copyFrom(this.aggregate);
            fullDevelopmentCopy.insertArguments(this.quantumCounter);
            soughtDevelopmentCopy = Relation.Relation();
            soughtDevelopmentCopy.copyFrom(this.soughtDevelopment);
            soughtDevelopmentCopy.insertArguments(this.quantumCounter);

            coefficient = soughtDevelopmentCopy.evaluate();
            if (coefficient == 0):
                this.productWith0 = (this.productWith0 * 
                    fullDevelopmentCopy);
            else:
                this.productWith1 = (this.productWith1 * 
                    fullDevelopmentCopy);

            this.quantumCounter.increment();
            this.remainingIterations -= 1;
        this.finishedProcessing = True;

    def hasFinished(this):
        return this.finishedProcessing;

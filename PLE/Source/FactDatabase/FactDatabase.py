# FactDatabase/FactDatabase.py
# Nicholas Killeen,
# 19th June 2016.
# Class to store and perform operations on a collection of facts.

import Relation;
import Relation.Relation as Relation;

# Data structure to store and manipulate a group of facts.
class FactDatabase:
    def __init__(this):
        this.factList = [];

    def appendFact(this, fact):
        if (hasattr(fact, "isValid")): 
            if (fact.isValid()):
                this.factList.append(fact);
                successState = True;
            else:
                successState = False;
                # the Relation is malformed
        else:
            successState = False;
            # the object is not of type Relation
        return successState;

    def deleteFact(this, factNumber):
        if (factNumber >= 0 and factNumber < len(this.factList)):
            this.factList.pop(factNumber);
            successState = True;
        else:
            successState = False;
        return successState;

    # Returns one Relation containing the combined knowledge of all 
    # facts in the system.
    def getFactAggregation(this):
        optimisedFactList = [];
        for fact in this.factList:
            optimisedFact = Relation.Relation();
            optimisedFact.copyFrom(fact);
            optimisedFact.optimise();
            optimisedFactList.append(optimisedFact);

        UNITY = Relation.Relation('1');
        aggregate = Relation.Relation('0');
        factNumber = 0;
        numFacts = len(optimisedFactList);
        while (factNumber < numFacts):
            priorFactNumber = 0;
            productOfPriorFacts = Relation.Relation('1');
            while (priorFactNumber < factNumber):
                productOfPriorFacts = productOfPriorFacts * (UNITY - 
                    optimisedFactList[priorFactNumber]);
                priorFactNumber += 1;
            currentFact = optimisedFactList[factNumber];
            aggregate += currentFact * productOfPriorFacts;
            factNumber += 1;
        aggregate.optimise();
        return aggregate;

    def getFactList(this):
        return this.factList;
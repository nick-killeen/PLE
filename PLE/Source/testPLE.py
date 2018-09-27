# testPLE.py
# Nicholas Killeen,
# 19th June 2016.
# Automated tests for the P.L.E program's functionality.

import FactDatabase.testFactDatabase as testFactDatabase;
import Fraction.testFraction as testFraction;
import QuantumCounter.testQuantumCounter as testQuantumCounter;
import Relation.testRelation as testRelation;
import Processor.testProcessor as testProcessor;
import Interface.testInterface as testInterface;

def testPLE():
    print("Testing Fraction ........... ", end="");
    testFraction.testFraction();
    print("passed!");

    print("Testing QuantumCounter ..... ", end="");
    testQuantumCounter.testQuantumCounter();
    print("passed!");

    print("Testing Relation ........... ", end="");
    testRelation.testRelation();
    print("passed!");

    print("Testing FactDatabase ....... ", end="");
    testFactDatabase.testFactDatabase();
    print("passed!");

    print("Testing Processor .......... ", end="");
    testProcessor.testProcessor();
    print("passed!");

    print("Testing Interface .......... ", end="");
    testInterface.testInterface();
    print("passed!");

    print("\nAll tests passed!!!\nYou are awesome!");
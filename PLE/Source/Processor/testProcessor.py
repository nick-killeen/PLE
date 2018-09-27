# Processor/testProcessor.py
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for Processor.py.

import Relation;
import QuantumCounter;
import Processor;
import Processor.Processor as Processor;
import Relation.Relation as Relation;
import QuantumCounter.QuantumCounter as QuantumCounter;

def testProcessor():
    # test all methods: __init__, go, hasFinished, getProductWith0 and
    # getProductWith1.

    # group 1
    aggregate1 = Relation.Relation("[0](1 - [1]) + [1](1 - [0])");
    soughtDevelopment1 = Relation.Relation("[0]");

    quantumCounter1 = QuantumCounter.QuantumCounter();
    quantumCounter1.createCoefficientMap(soughtDevelopment1.
        getSymbolList());
    processor1 = Processor.Processor(aggregate1, soughtDevelopment1, 
        quantumCounter1, 2);
    processor1.go();
    assert(processor1.getProductWith0() == Relation.Relation("[1]"));
    assert(processor1.getProductWith1() == Relation.Relation("1-[1]"));

    # group 2
    aggregate2_3 = Relation.Relation("[0](1 - [1])[4] + (1 - [4])[5][1]"
        "(1 - [0])");
    soughtDevelopment2_3 = Relation.Relation("[0][1](1 - [5])");

    quantumCounter2 = QuantumCounter.QuantumCounter();
    quantumCounter2.createCoefficientMap(soughtDevelopment2_3.
        getSymbolList());
    processor2 = Processor.Processor(aggregate2_3, 
        soughtDevelopment2_3, quantumCounter2, 5);
    assert(processor2.hasFinished() == False);
    processor2.go();
    assert(processor2.hasFinished() == True);

    quantumCounter3 = QuantumCounter.QuantumCounter();
    quantumCounter3.createCoefficientMap(soughtDevelopment2_3.
        getSymbolList());
    quantumCounter3.add(5);
    processor3 = Processor.Processor(aggregate2_3,
        soughtDevelopment2_3, quantumCounter3, 3);
    assert(processor3.hasFinished() == False);
    processor3.go();
    assert(processor3.hasFinished() == True);

    productWith0For2_3 = (processor2.getProductWith0() * 
        processor3.getProductWith0());
    assert(productWith0For2_3 == Relation.Relation("0"));
    productWith1For2_3 = (processor2.getProductWith1() *
        processor3.getProductWith1());
    assert(productWith1For2_3 == Relation.Relation("0"));

    # group 3
    aggregate4_5 = Relation.Relation("[2](1 - [3]) + (1 - [2])([3][4] +"
        "(1 - [3])(1 - [4]))");
    soughtDevelopment4_5 = Relation.Relation("[2](1 - [3])[5] + (1 - [5"
        "])[2](1 - [3]) + [3](1 - [2])");

    quantumCounter4 = QuantumCounter.QuantumCounter();
    quantumCounter4.createCoefficientMap(soughtDevelopment4_5.
        getSymbolList());
    processor4 = Processor.Processor(aggregate4_5,
        soughtDevelopment4_5, quantumCounter4, 4);
    processor4.go();

    quantumCounter5 = QuantumCounter.QuantumCounter();
    quantumCounter5.createCoefficientMap(soughtDevelopment4_5.
        getSymbolList());
    quantumCounter5.add(4);
    processor5 = Processor.Processor(aggregate4_5,
        soughtDevelopment4_5, quantumCounter5, 4);
    processor5.go();

    productWith0For4_5 = (processor4.getProductWith0() * 
        processor5.getProductWith0());
    assert(productWith0For4_5 == Relation.Relation("0"));
    productWith1For4_5 = (processor4.getProductWith1() *
        processor5.getProductWith1());
    assert(productWith1For4_5 == Relation.Relation("[4]"));
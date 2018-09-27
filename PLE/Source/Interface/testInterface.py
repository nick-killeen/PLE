# Interface/testInterface.py
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for Interface.py.

import Interface;
import Relation;
import Interface.Interface as Interface;
import Relation.Relation as Relation;

def testInterface():
    # test constructor __init__, getFactList, addFact, and deleteFact
    errorList = [];
    interface1 = Interface.Interface(errorList.append);
    assert(interface1.getFactList() == []);

    relation1 = Relation.Relation("1");
    interface1.addFact(relation1);
    assert(interface1.getFactList() == [relation1]);

    relation2 = Relation.Relation("0");
    interface1.addFact(relation2);
    assert(interface1.getFactList() == [relation1, relation2]);

    relation3 = Relation.Relation("[0]");
    interface1.addFact(relation3);
    assert(interface1.getFactList() == [relation1, relation2, 
        relation3]);

    assert(len(errorList) == 0);
    interface1.deleteFact(-1);
    assert(interface1.getFactList() == [relation1, relation2, 
        relation3]);
    assert(len(errorList) == 1);

    interface1.deleteFact(0);
    assert(interface1.getFactList() == [relation2, relation3]);
    interface1.deleteFact(1);
    assert(interface1.getFactList() == [relation2]);

    interface1.deleteFact(1);
    assert(interface1.getFactList() == [relation2]);
    assert(len(errorList) == 2);

    relation4 = Relation.Relation("2");
    interface1.addFact(relation4);
    assert(interface1.getFactList() == [relation2]);
    assert(len(errorList) == 3);

    # testing setRequest, and getRequest
    interface1.setRequest(relation4);
    assert(len(errorList) == 4);
    request = interface1.getRequest();
    assert(request == None);
    assert(len(errorList) == 5);

    relation5 = Relation.Relation("[1]");
    interface1.setRequest(relation5);
    request = interface1.getRequest();
    assert(request == relation5);
    assert(len(errorList) == 5);
     
    errorList.clear();

    # testing generateProcessor, and retrieveSoughtInformation
    interface2 = Interface.Interface(errorList.append);
    interface2.retrieveResponse();
    assert(len(errorList) == 1);
    interface2.generateProcessor();
    assert(len(errorList) == 2);

    interface2.addFact(Relation.Relation("1"));
    interface2.setRequest(Relation.Relation("1"));
    interface2.generateProcessor();
    assert(len(errorList) == 2);
    interface2.generateProcessor();
    assert(len(errorList) == 2);

    errorList.clear();

    interface3 = Interface.Interface(errorList.append);
    handler = interface3.generateProcessor();
    assert(handler == None);
    assert(len(errorList) == 1);

    interface3.addFact(Relation.Relation("[1]"));
    interface3.setRequest(Relation.Relation("[1]"));
    handler = interface3.generateProcessor();
    assert(len(errorList) == 1);
    assert(handler != None);

    interface3.retrieveResponse();
    assert(len(errorList) == 2);
    handler();
    interface3.retrieveResponse();

    quaesitum = interface3.retrieveResponse();
    assert(len(errorList) == 2);
    assert(quaesitum.getNumerator().evaluate() / quaesitum.
        getDenominator().evaluate() == 0);

    errorList.clear();

    interface3 = Interface.Interface(errorList.append);
    interface3.addFact(Relation.Relation("[1](1 - [0])"));
    interface3.addFact(Relation.Relation("[0](1 - [1])"));
    interface3.setRequest(Relation.Relation("[1]"));
    quaesitum = interface3.retrieveResponse();
    assert(len(errorList) == 1);
    handler = interface3.generateProcessor();
    quaesitum = interface3.retrieveResponse();
    assert(quaesitum == None);
    assert(len(errorList) == 2);
    handler();
    quaesitum = interface3.retrieveResponse();
    assert(quaesitum != None);
    assert(len(errorList) == 2);

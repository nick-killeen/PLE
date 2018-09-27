# FactDatabase/testFactDatabase.py
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for FactDatabase.py.

import FactDatabase;
import FactDatabase.FactDatabase as FactDatabase;
import Relation;
import Relation.Relation as Relation;

def testFactDatabase():
    # test constructor __init__, appendFact, and getFactList
    factDatabase1 = FactDatabase.FactDatabase();
    assert(factDatabase1.getFactList() == []);
    relation1 = Relation.Relation("[0]");
    successStateAdd1 = factDatabase1.appendFact(relation1);
    assert(successStateAdd1 == True);
    assert(factDatabase1.getFactList()[0] == relation1);
    assert(len(factDatabase1.getFactList()) == 1);

    relation2 = Relation.Relation("[0] + 1");
    successStateAdd2 = factDatabase1.appendFact(relation2);
    assert(successStateAdd2 == False);
    assert(factDatabase1.getFactList()[0] == relation1);
    assert(len(factDatabase1.getFactList()) == 1);

    relation3 = Relation.Relation("[0] + (1 - [0])[12]");
    successStateAdd3 = factDatabase1.appendFact(relation3);
    assert(successStateAdd3 == True);
    assert(factDatabase1.getFactList()[0] == relation1);
    assert(factDatabase1.getFactList()[1] == relation3);
    assert(len(factDatabase1.getFactList()) == 2);

    successStateAdd4 = factDatabase1.appendFact("pulled pork");
    assert(successStateAdd4 == False);
    assert(factDatabase1.getFactList()[0] == relation1);
    assert(factDatabase1.getFactList()[1] == relation3);
    assert(len(factDatabase1.getFactList()) == 2);

    relation5 = Relation.Relation("[12](1 - [5]) + [5](1 - [12])[0]");
    successStateAdd5 = factDatabase1.appendFact(relation5);
    assert(successStateAdd5 == True);
    assert(factDatabase1.getFactList()[0] == relation1);
    assert(factDatabase1.getFactList()[1] == relation3);
    assert(factDatabase1.getFactList()[2] == relation5);
    assert(len(factDatabase1.getFactList()) == 3);

    # test deleteFact
    factDatabase2 = FactDatabase.FactDatabase();
    successStateDelete1 = factDatabase2.deleteFact(0);
    assert(successStateDelete1 == False);
    successStateDelete2 = factDatabase2.deleteFact(1);
    assert(successStateDelete2 == False);
    successStateDelete3 = factDatabase2.deleteFact(-1);
    assert(successStateDelete3 == False);

    relation6 = Relation.Relation("[1][2](1 - [3])");
    factDatabase2.appendFact(relation6);
    successStateDelete4 = factDatabase2.deleteFact(0);
    assert(successStateDelete4 == True);
    assert(len(factDatabase2.getFactList()) == 0);

    relation7 = Relation.Relation("[1][8] + (1 - [1])(1 - [8])");
    factDatabase2.appendFact(relation7);
    relation8 = Relation.Relation("[1][2] + [2](1 - [8])(1 - [1])");
    factDatabase2.appendFact(relation8);
    relation9 = Relation.Relation("[2](1 - [3]) + [4][3](1 - [2])");
    factDatabase2.appendFact(relation9);
    relation10 = Relation.Relation("0");
    factDatabase2.appendFact(relation10);
    successStateDelete5 = factDatabase2.deleteFact(4);
    assert(successStateDelete5 == False);
    successStateDelete6 = factDatabase2.deleteFact(0);
    assert(successStateDelete6 == True);
    factList1 = factDatabase2.getFactList();
    assert(factList1[0] == relation8);
    assert(factList1[1] == relation9);
    assert(factList1[2] == relation10);
    assert(len(factList1) == 3);

    successStateDelete7 = factDatabase2.deleteFact(1);
    assert(successStateDelete7 == True);
    factList2 = factDatabase2.getFactList();
    assert(factList2[0] == relation8);
    assert(factList2[1] == relation10);
    assert(len(factList2) == 2);

    successStateDelete8 = factDatabase2.deleteFact(1);
    assert(successStateDelete8 == True);
    factList3 = factDatabase2.getFactList();
    assert(factList3[0] == relation8);
    assert(len(factList3) == 1);

    # test getFactAggregation
    factDatabase3 = FactDatabase.FactDatabase();
    relation11 = Relation.Relation("[0]");
    factDatabase3.appendFact(relation11);
    assert(factDatabase3.getFactAggregation() == relation11);
    relation12 = Relation.Relation("[1]");
    factDatabase3.appendFact(relation12);
    relation13 = Relation.Relation("[1] + [0](1 - [1])");
    assert(factDatabase3.getFactAggregation() == relation13);
    relation14 = Relation.Relation("(1 - [2][3])");
    factDatabase3.appendFact(relation14);
    relation15 = Relation.Relation("[0] + [1](1 - [0]) + (1 - [2][3])(1"
        " - [1])(1 - [0])");
    assert(factDatabase3.getFactAggregation() == relation15);
    relation16 = Relation.Relation("[3] + (1 - [3])(1 - [2])");
    factDatabase3.appendFact(relation16);
    relation17 = Relation.Relation("[0] + [1](1 - [0]) + (1 - [1])(1 - "
        "[0])");
    assert(factDatabase3.getFactAggregation() == relation17);

    factDatabase4 = FactDatabase.FactDatabase();
    relation18 = Relation.Relation("0");
    assert(factDatabase4.getFactAggregation() == relation18);
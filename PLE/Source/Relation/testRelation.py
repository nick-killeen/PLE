# Relation/testRelation.py
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for Relation.py.

import Relation;
import QuantumCounter;
import Relation.Relation as Relation;
import QuantumCounter.QuantumCounter as QuantumCounter;

def testRelation():
    # test helper function _areAllCharactersLegal
    assert(Relation._areAllCharactersLegal("") == True);
    assert(Relation._areAllCharactersLegal(" ") == True);
    assert(Relation._areAllCharactersLegal("1 0 + -") == True);
    assert(Relation._areAllCharactersLegal("012345678911 [") == True);
    assert(Relation._areAllCharactersLegal("[]1( )") == True);
    assert(Relation._areAllCharactersLegal(",") == False);
    assert(Relation._areAllCharactersLegal(". ") == False);
    assert(Relation._areAllCharactersLegal("13 16 22 4 19 a") == False);
    assert(Relation._areAllCharactersLegal("`") == False);
    assert(Relation._areAllCharactersLegal("*") == False);
    assert(Relation._areAllCharactersLegal("/ 9001") == False);

    # test helper function _areCombinationsLegal
    assert(Relation._areCombinationsLegal("") == False);
    assert(Relation._areCombinationsLegal(" + ") == False);
    assert(Relation._areCombinationsLegal(")-") == False);
    assert(Relation._areCombinationsLegal("(12) -") == False);
    assert(Relation._areCombinationsLegal("(144)-     ") == False);
    assert(Relation._areCombinationsLegal("(1) (9)") == False);
    assert(Relation._areCombinationsLegal("(4) 2") == False);
    assert(Relation._areCombinationsLegal("2 [1]") == False);
    assert(Relation._areCombinationsLegal("(1]+ 3") == False);
    assert(Relation._areCombinationsLegal("2 [1]") == False);
    assert(Relation._areCombinationsLegal("[") == False);
    assert(Relation._areCombinationsLegal("]") == False);
    assert(Relation._areCombinationsLegal("[1)") == False);
    assert(Relation._areCombinationsLegal("(1 2)") == False);
    assert(Relation._areCombinationsLegal("[3 1]") == False);
    assert(Relation._areCombinationsLegal("(     )(12)") == False);
    assert(Relation._areCombinationsLegal("()") == False);
    assert(Relation._areCombinationsLegal("[12]") == True);
    assert(Relation._areCombinationsLegal("[123456789](0)") == True);
    assert(Relation._areCombinationsLegal("1 + 1") == True);
    assert(Relation._areCombinationsLegal("2+n") == True);
    assert(Relation._areCombinationsLegal("n+(5)") == True);
    assert(Relation._areCombinationsLegal("[5]+(((n)))") == True);
    assert(Relation._areCombinationsLegal("((1+((1)(( n)))))") == True);

    # test helper function _areNumbersLegal
    assert(Relation._areNumbersLegal("") == True);
    assert(Relation._areNumbersLegal("tortilla") == True);
    assert(Relation._areNumbersLegal("0 1-- 2, three 1007") == True);
    assert(Relation._areNumbersLegal("007") == False);
    assert(Relation._areNumbersLegal("0*0*1") == True);
    assert(Relation._areNumbersLegal("00     12") == False);
    assert(Relation._areNumbersLegal("100000 600001") == True);

    # test helper function _isNestingLegal
    assert(Relation._isNestingLegal("") == True);
    assert(Relation._isNestingLegal("()") == True);
    assert(Relation._isNestingLegal("      ") == True);
    assert(Relation._isNestingLegal(" ( ( )  ) ") == True);
    assert(Relation._isNestingLegal("(a(x)+) (]") == True);
    assert(Relation._isNestingLegal("([[1()]()[2]])") == True);
    assert(Relation._isNestingLegal("(()()") == False);
    assert(Relation._isNestingLegal(")( )( ") == False);
    assert(Relation._isNestingLegal(")(())(") == False);
    assert(Relation._isNestingLegal("(a)v)") == False);

    # test helper function _recursivelyReplace
    assert(Relation._recursivelyReplace("ab", "a", "b") == "bb");
    assert(Relation._recursivelyReplace("ab", "ab", "ab") == "ab");
    assert(Relation._recursivelyReplace("23232323", "2323", "23") == 
        "23");
    assert(Relation._recursivelyReplace("110111101 10011111111", "11", 
        "1") == "10101 1001");
    assert(Relation._recursivelyReplace("", "a", "cd") == "");
    assert(Relation._recursivelyReplace("", "", "l") == "");
    assert(Relation._recursivelyReplace("", "n", "") == "");
    assert(Relation._recursivelyReplace("x", "", "") == "x");

    # test test-helper function, _areArraysEqual
    assert(_areArraysEqual([0], [1]) == False);
    assert(_areArraysEqual([1, 2], [1]) == False);
    assert(_areArraysEqual([1, 2, 3, 4], [1, 3, 2, 4]) == True);
    assert(_areArraysEqual([0, 0], [1]) == False);
    assert(_areArraysEqual([0, 199], [199, 0]) == True);
    assert(_areArraysEqual([], []) == True);
    assert(_areArraysEqual([12], []) == False);
    assert(_areArraysEqual([12, 13, 13], [13, 12, 12]) == False);
    assert(_areArraysEqual([12, 13, 13], [13, 12, 12]) == False);
    assert(_areArraysEqual([1, 2, 3, 55, 102, 1042, 4, 16], [1, 2, 3, 
        55, 1042, 102, 4, 16]) == True);
    assert(_areArraysEqual([1, 2, 3, 55, 102, 1043, 4, 16], [1, 2, 3, 
        55, 1042, 102, 4, 16]) == False);

    # test getSymbolList
    relation1 = Relation.Relation("[1] + [0](1 - [1])");
    symbolsInRelation1 = relation1.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation1, [0, 1]));

    relation2 = Relation.Relation("1");
    symbolsInRelation2 = relation2.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation2, []));

    relation3 = Relation.Relation("0 + [1]");
    symbolsInRelation3 = relation3.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation3, [1]));

    relation4 = Relation.Relation("0 + [5](1 - [2])(1 - [4][7])");
    symbolsInRelation4 = relation4.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation4, [2, 4, 5, 7]));

    relation5 = Relation.Relation("(1 - [3])([12] + [15](1 - [12]))");
    symbolsInRelation5 = relation5.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation5, [3, 12, 15]));

    relation6 = Relation.Relation("[1][2][100] + [9001][1](1 - [2])(1 -"
        " [100])");
    symbolsInRelation6 = relation6.getSymbolList();
    assert(_areArraysEqual(symbolsInRelation6, [1, 2, 100, 9001]));

    # test evaluate
    relation7 = Relation.Relation("1");
    assert(relation7.evaluate() == 1);

    relation8 = Relation.Relation("0");
    assert(relation8.evaluate() == 0);

    relation9 = Relation.Relation("(0)(1)");
    assert(relation9.evaluate() == 0);

    relation10 = Relation.Relation("(0)(1) + 1 + (0)(1 - (1))");
    assert(relation10.evaluate() == 1);

    relation11 = Relation.Relation("(1)(1)(0) + (1)(1 - (1))(1 - ((0)(1"
        "))) + (1 - (1))(1 - (1))");
    assert(relation11.evaluate() == 0);

    relation12 = Relation.Relation("(0)(1 - (0)) + (0)(1 - (1)) + (1)("
        "1 - (0))(1 - (1 - (1)))");
    assert(relation12.evaluate() == 1);

    # test insertArguments, "==" operator __eq__, copyFrom, and the "!="
    # comparator __ne__
    quantumCounter13 = QuantumCounter.QuantumCounter([1, 0]);
    relation13 = Relation.Relation("[1]");
    relation13.insertArguments(quantumCounter13);
    assert(relation13.evaluate() == 0);

    quantumCounter14 = QuantumCounter.QuantumCounter([0, 0]);
    relation14 = Relation.Relation("[0] + [0](1 - [1])");
    relation14.insertArguments(quantumCounter14);
    assert(relation14.evaluate() == 0);

    quantumCounter15 = QuantumCounter.QuantumCounter([1]);
    relation15 = Relation.Relation("[0](1 - [1]) + [1](1 - [0])");
    relation15.insertArguments(quantumCounter15);
    relation16 = Relation.Relation("(1 - [1])");
    assert((relation15 == relation16) == True);
    assert((relation15 != relation16) == False);
    relation16Copy = Relation.Relation();
    relation16Copy.copyFrom(relation16);
    assert(relation16 == relation16Copy);

    relation17 = Relation.Relation("[4]");
    relation18 = Relation.Relation("0");
    assert((relation17 == relation18) == False);
    assert((relation17 != relation18) == True);
    quantumCounter17 = QuantumCounter.QuantumCounter([1, 0, -1, 0, 0]);
    relation17.insertArguments(quantumCounter17);
    assert((relation17 == relation18) == True);
    assert((relation17 != relation18) == False);
    assert((relation17 == relation17) == True);
    assert((relation17 != relation17) == False);
    assert((relation18 == relation18) == True);
    assert((relation18 != relation18) == False);
    relation17Copy = Relation.Relation();
    relation17Copy.copyFrom(relation17);
    assert(relation17 == relation17Copy);
    
    relation19 = Relation.Relation("1");
    relation20 = Relation.Relation("[2][1][111] + (1 - [2])[111](1 - [1"
        "]) + (0)(1 - [6]) + [1][2](1 - [111]) + (1 - [1])(1 - [111]) +"
        " [1][111](1 - [2]) + [2][111](1 - [1]) + 0 + [1](1 - [111])(1 "
        "- [2])");
    relation21 = Relation.Relation("[2][1][111] + (1 - [2])[111](1 - [1"
        "]) + (0)(1 - [6]) + [1][2](1 - [111]) + (1 - [1])(1 - [111]) +"
        " [1][111](1 - [2]) + [2][111](1 - [1]) + 0 + [1](1 - [111])(1 "
        "- [1])");
    assert((relation19 == relation20) == True);
    assert((relation19 != relation20) == False);
    assert((relation20 == relation21) == False);
    assert((relation20 != relation21) == True);

    relation22 = Relation.Relation("[4][0][1] + (1 - [0])[1](1 - [4])");
    quantumCounter22 = QuantumCounter.QuantumCounter(['v', 'v', 'v', 
        'v', 1, 'v', 1]);
    relation23 = Relation.Relation("(1)[0][1] + (1 - [0])[1](1 - (1))");
    assert((relation22 == relation23) == False);
    relation22.insertArguments(quantumCounter22);
    assert(relation22 == relation23);
    relation24 = Relation.Relation();
    relation24.copyFrom(relation22);
    assert(relation23 == relation24);

    relation25 = Relation.Relation("0 + [1](1 - [2])(1 - [0][3])");
    relation26 = Relation.Relation();
    relation26.copyFrom(relation25);
    relation27 = Relation.Relation();
    relation27.copyFrom(relation26);
    assert(relation25 == relation26);
    assert(relation25 == relation27);
    assert((relation26 != relation27) == False);
    quantumCounter25 = QuantumCounter.QuantumCounter([]);
    relation25.insertArguments(quantumCounter25);
    assert(relation25 == relation26);
    quantumCounter26 = QuantumCounter.QuantumCounter(["1"]);
    relation26.insertArguments(quantumCounter26);
    assert(relation25 == relation26);
    assert(relation26 == relation27);
    quantumCounter27 = QuantumCounter.QuantumCounter([0, 1, 0, 1]);
    relation27.insertArguments(quantumCounter27);
    assert(relation27.evaluate() == 1);

    # test the "*" operator __mul__
    relation28 = Relation.Relation("[0]");
    relation29 = Relation.Relation("[0]");
    relation30 = relation28 * relation29;
    assert(relation28 * relation29 == relation28);
    assert(relation28 * relation29 == relation29);
    relation31 = Relation.Relation("[1]");
    relation32 = relation31 * relation30;
    relation33 = relation30 * relation31;
    relation34 = Relation.Relation("[0][1]");
    assert(relation32 == relation33);
    assert(relation34 == relation33);
    assert(relation34 == relation32);
    assert(relation34 != relation28);

    relation35 = Relation.Relation("[0] + [1](1 - [0])");
    relation36 = Relation.Relation("0");
    relation37 = Relation.Relation("1");
    relation38 = Relation.Relation("(0) + ((([1])))");
    relation39 = Relation.Relation("([1])");
    assert(relation35 * relation36 == relation36);
    assert(relation35 != relation36);
    assert(relation35 * relation35 == relation35);
    assert(relation35 * relation37 == relation35);
    assert(relation37 * relation35 == relation35);
    assert(relation36 * relation37 == relation36);
    assert(relation36 * relation38 == relation36);
    assert(relation37 * relation38 == relation38);
    assert(relation38 * relation38 == relation38);
    assert(relation35 * relation38 == relation39);
    assert(relation38 * relation35 == relation39);
    assert(relation38 * relation39 == relation39);

    # test eliminateSymbol
    relation39 = Relation.Relation("[0]");
    relation39.eliminateSymbol(0);
    assert(relation39.evaluate() == 0);

    relation40 = Relation.Relation("[0](1 - [1]) + (1 - [0])(1 - [1])");
    relation40.eliminateSymbol(1);
    relation41 = Relation.Relation("0");
    assert(relation40 == relation41);

    relation42 = Relation.Relation("[9](1 - [1]) + [9][1](1 - [2][3])");
    relation42.eliminateSymbol(1);
    relation43 = Relation.Relation("[9](1 - [2][3])");
    assert(relation42 == relation43);

    relation44 = Relation.Relation("0");
    relation44.eliminateSymbol(5);
    assert(relation44.evaluate() == 0);

    relation45 = Relation.Relation("[10][2][3] + [10](1 - [2])(1 - [3])"
        " + (1 - [10])(1 - [2])");
    relation46 = Relation.Relation("(1 - [2])(1 - [3])");
    relation45.eliminateSymbol(10);
    assert(relation45 == relation46);

    # test the binary "+" operator __add__
    relation46 = Relation.Relation("0");
    relation47 = Relation.Relation("1");
    relation48 = Relation.Relation("[2]");
    relation49 = Relation.Relation("(1 - [2])");
    assert(relation46 + relation46 == relation46);
    assert(relation46 + relation47 == relation47);
    assert(relation48 + relation49 + relation46 == relation47);

    relation50 = Relation.Relation("[12][11]");
    relation51 = Relation.Relation("(1 - [12])[11][4]");
    relation52 = Relation.Relation("(1 - [12])[11](1 - [4])");
    relation53 = Relation.Relation("(1 - [12])[11]");
    relation54 = Relation.Relation("[11]");
    assert(relation50 + relation51 + relation52 == relation54);
    assert(relation52 + relation50 + relation51 == relation54);
    assert(relation53 == relation51 + relation52);
    assert(relation54 == relation50 + relation53);

    relation55 = Relation.Relation("[102](1 - [0])");
    relation56 = Relation.Relation("[0](1 - [1][102])");
    relation57 = Relation.Relation("[102](1 - [0])(1 - [1]) + [102](1 -"
        " [0])[1] + [0](1 - [1][102])");
    relation58 = Relation.Relation("[102](1 - [0])(1 - [4]) + [102](1 -"
        " [0])[1] + [0](1 - [1][102])");
    assert(relation55 + relation56 == relation57);
    assert(relation55 + relation56 != relation58);

    # test binary "-" operator __sub__
    relation57 = Relation.Relation("[102]");
    relation58 = Relation.Relation("(1 - [102])");
    relation59 = Relation.Relation("0");
    relation60 = Relation.Relation("1");
    assert(relation57 - relation57 == relation59);
    assert(relation60 - relation57 == relation58);
    assert(relation60 - relation58 == relation57);
    assert(relation60 - (relation60 - relation58) == relation58);
    assert(relation60 - (relation60 - relation57) == relation57);

    relation61 = Relation.Relation("[3](1 - [4]) + (1 - [3])[4]");
    relation62 = Relation.Relation("[12]([3][4] + (1 - [3])(1 - [4])) +"
        " (1 - [12])([3][4] + (1 - [3])(1 - [4]))");
    relation63 = Relation.Relation("1");
    assert(relation63 - relation61 == relation62);
    assert(relation63 - relation62 == relation61);

    relation64 = Relation.Relation("[0][1](1 - [2])[4] + (1 - [4])");
    relation65 = Relation.Relation("(1 - [4])");
    relation66 = Relation.Relation("[0][1](1 - [2])[4]");
    assert(relation64 - relation65 == relation66);
    assert(relation64 - relation66 == relation65);

    # test isValid, optimise
    relation67 = Relation.Relation("0");
    relation67Copy = Relation.Relation();
    relation67Copy.copyFrom(relation67);
    relation67Copy.optimise();
    assert(relation67.isValid() == True);
    assert(relation67 == relation67Copy);

    relation68 = Relation.Relation("1");
    relation68Copy = Relation.Relation();
    relation68Copy.copyFrom(relation68);
    relation68Copy.optimise();
    assert(relation68.isValid() == True);
    assert(relation68 == relation68Copy);

    relation69 = Relation.Relation("(1) + 0");
    relation69Copy = Relation.Relation();
    relation69Copy.copyFrom(relation69);
    relation69Copy.optimise();
    assert(relation69.isValid() == True);
    assert(relation69 == relation69Copy);

    relation70 = Relation.Relation("(1)(1)");
    relation70Copy = Relation.Relation();
    relation70Copy.copyFrom(relation70);
    relation70Copy.optimise();
    assert(relation70.isValid() == True);
    assert(relation70 == relation70Copy);

    relation71 = Relation.Relation("(((1)))(0)");
    relation71Copy = Relation.Relation();
    relation71Copy.copyFrom(relation71);
    relation71Copy.optimise();
    assert(relation71.isValid() == True);
    assert(relation71 == relation71Copy);

    relation72 = Relation.Relation("(((1)))(0) - (0)");
    relation72Copy = Relation.Relation();
    relation72Copy.copyFrom(relation72);
    relation72Copy.optimise();
    assert(relation72.isValid() == True);
    assert(relation72 == relation72Copy);

    relation73 = Relation.Relation("[0]");
    relation73Copy = Relation.Relation();
    relation73Copy.copyFrom(relation73);
    relation73Copy.optimise();
    assert(relation73.isValid() == True);
    assert(relation73 == relation73Copy);

    relation74 = Relation.Relation("[10]");
    relation74Copy = Relation.Relation();
    relation74Copy.copyFrom(relation74);
    relation74Copy.optimise();
    assert(relation74.isValid() == True);
    assert(relation74 == relation74Copy);

    relation75 = Relation.Relation("[104]");
    relation75Copy = Relation.Relation();
    relation75Copy.copyFrom(relation75);
    relation75Copy.optimise();
    assert(relation75.isValid() == True);
    assert(relation75 == relation75Copy);

    relation76 = Relation.Relation("1 - [99]");
    relation76Copy = Relation.Relation();
    relation76Copy.copyFrom(relation76);
    relation76Copy.optimise();
    assert(relation76.isValid() == True);
    assert(relation76 == relation76Copy);

    relation77 = Relation.Relation("1 - [13][12]");
    relation77Copy = Relation.Relation();
    relation77Copy.copyFrom(relation77);
    relation77Copy.optimise();
    assert(relation77.isValid() == True);
    assert(relation77 == relation77Copy);

    relation78 = Relation.Relation("(1 - [13][1])[13]");
    relation78Copy = Relation.Relation();
    relation78Copy.copyFrom(relation78);
    relation78Copy.optimise();
    assert(relation78.isValid() == True);
    assert(relation78 == relation78Copy);

    relation79 = Relation.Relation("[0] + (1 - [0])[1]");
    relation79Copy = Relation.Relation();
    relation79Copy.copyFrom(relation79);
    relation79Copy.optimise();
    assert(relation79.isValid() == True);
    assert(relation79 == relation79Copy);

    relation80 = Relation.Relation("[0](1 - [2]) + (1 - [0])[1](1 - [2]"
        " + [2])");
    relation80Copy = Relation.Relation();
    relation80Copy.copyFrom(relation80);
    relation80Copy.optimise();
    assert(relation80.isValid() == True);
    assert(relation80 == relation80Copy);

    relation81 = Relation.Relation("     0 ");
    relation81Copy = Relation.Relation();
    relation81Copy.copyFrom(relation81);
    relation81Copy.optimise();
    assert(relation81.isValid() == True);
    assert(relation81 == relation81Copy);

    relation82 = Relation.Relation(" (          1 )+  0");
    relation82Copy = Relation.Relation();
    relation82Copy.copyFrom(relation82);
    relation82Copy.optimise();
    assert(relation82.isValid() == True);
    assert(relation82 == relation82Copy);

    relation83 = Relation.Relation("1    +   (0)(1)");
    relation83Copy = Relation.Relation();
    relation83Copy.copyFrom(relation83);
    relation83Copy.optimise();
    assert(relation83.isValid() == True);
    assert(relation83 == relation83Copy);

    relation84 = Relation.Relation("                                   "
        "                                                              "
        "                             [0]                              "
        "                                                              "
        "                                                              "
        "            +                  (1 - [0])                      "
        "                                                            ");
    relation84Copy = Relation.Relation();
    relation84Copy.copyFrom(relation84);
    relation84Copy.optimise();
    assert(relation84.isValid() == True);
    assert(relation84 == relation84Copy);

    relation85 = Relation.Relation("((                 ([0])))([0])+(1-"
        "[0])");
    relation85Copy = Relation.Relation();
    relation85Copy.copyFrom(relation85);
    relation85Copy.optimise();
    assert(relation85.isValid() == True);
    assert(relation85 == relation85Copy);

    relation86 = Relation.Relation("[0][2] -  0 - ([2][0][1] - [1])");
    relation86Copy = Relation.Relation();
    relation86Copy.copyFrom(relation86);
    relation86Copy.optimise();
    assert(relation86.isValid() == True);
    assert(relation86 == relation86Copy);

    relation87 = Relation.Relation("-1");
    assert(relation87.isValid() == False);

    relation88 = Relation.Relation("-2");
    assert(relation88.isValid() == False);

    relation89 = Relation.Relation("2");
    assert(relation89.isValid() == False);
    
    relation90 = Relation.Relation("[0] + [1]");
    assert(relation90.isValid() == False);
    
    relation91 = Relation.Relation("[0] + [0]");
    assert(relation91.isValid() == False);

    relation92 = Relation.Relation("");
    assert(relation92.isValid() == False);
    
    relation93 = Relation.Relation("0.0");
    assert(relation93.isValid() == False);
    
    relation94 = Relation.Relation("all men are mortals");
    assert(relation94.isValid() == False);

    relation95 = Relation.Relation("((1)");
    assert(relation95.isValid() == False);

    relation96 = Relation.Relation("2(1)");
    assert(relation96.isValid() == False);
    
    relation97 = Relation.Relation("[ 0]");
    assert(relation97.isValid() == False);
    
    relation98 = Relation.Relation("[10 2]");
    assert(relation98.isValid() == False);
    
    relation99 = Relation.Relation("[2 ]");
    assert(relation99.isValid() == False);
    
    relation100 = Relation.Relation("[2+1]");
    assert(relation100.isValid() == False);
    
    relation101 = Relation.Relation("[12] + ()(1 - [12])");
    assert(relation101.isValid() == False);

    relation102 = Relation.Relation("[12] + (1(1) 1)");
    assert(relation102.isValid() == False);
    
    relation103 = Relation.Relation("[])");
    assert(relation103.isValid() == False);
    
    relation104 = Relation.Relation("[-1])");
    assert(relation104.isValid() == False);
    
    relation105 = Relation.Relation("[00]");
    assert(relation105.isValid() == False);
    
    relation106 = Relation.Relation("00");
    assert(relation106.isValid() == False);
    
    relation107 = Relation.Relation("[01]");
    assert(relation107.isValid() == False);
    
    relation108 = Relation.Relation("+");
    assert(relation108.isValid() == False); 
    
    relation109 = Relation.Relation("-");
    assert(relation109.isValid() == False);
    
    relation110 = Relation.Relation("[12]a");
    assert(relation110.isValid() == False);
    
    relation111 = Relation.Relation("[12] + b");
    assert(relation111.isValid() == False);
    
    relation112 = Relation.Relation("[12] + ");
    assert(relation112.isValid() == False);
    
    relation113 = Relation.Relation("1 +*");
    assert(relation113.isValid() == False);
    
    relation114 = Relation.Relation("(1)*(1)");
    assert(relation114.isValid() == False);
    
    relation115 = Relation.Relation("[");
    assert(relation115.isValid() == False);
    
    relation116 = Relation.Relation(")");
    assert(relation116.isValid() == False);
    
    relation117 = Relation.Relation("([1)]");
    assert(relation117.isValid() == False);
    
    relation118 = Relation.Relation("1 - [13][3]     )");
    assert(relation118.isValid() == False);
    
    relation119 = Relation.Relation("(1) (1)");
    assert(relation119.isValid() == False);
    
    relation120 = Relation.Relation("9 / 9");
    assert(relation120.isValid() == False);
    
    relation121 = Relation.Relation("1/1");
    assert(relation121.isValid() == False);
    
    relation122 = Relation.Relation("[1] + (1 - [1.])");
    assert(relation122.isValid() == False);
    
    relation123 = Relation.Relation("[1] + l (1 - [1])");
    assert(relation123.isValid() == False);
    
    relation124 = Relation.Relation("{1 + 0}");
    assert(relation124.isValid() == False);
    
    relation125 = Relation.Relation("shredded lettuce");
    assert(relation125.isValid() == False);
    
    relation126 = Relation.Relation("\"\"");
    assert(relation126.isValid() == False);
    
    relation127 = Relation.Relation("assert(False)");
    assert(relation127.isValid() == False);
    
    relation128 = Relation.Relation("eval(assert(False))");
    assert(relation128.isValid() == False);
    
    relation129 = Relation.Relation("1 + 0^1");
    assert(relation129.isValid() == False);
    
    relation130 = Relation.Relation("1 -- 0");
    assert(relation130.isValid() == False);
    
    relation131 = Relation.Relation("0 +- 0");
    assert(relation131.isValid() == False);
    
    relation132 = Relation.Relation("0 +- 1");
    assert(relation132.isValid() == False);
    
    relation133 = Relation.Relation("(((((((1))))) )");
    assert(relation133.isValid() == False);
    
    relation134 = Relation.Relation("0\t");
    assert(relation134.isValid() == False);
    
    relation135 = Relation.Relation("0 0");
    assert(relation135.isValid() == False);
    
    relation136 = Relation.Relation("0 0");
    assert(relation136.isValid() == False);
    
    relation137 = Relation.Relation("1[0]");
    assert(relation137.isValid() == False);
    
    relation138 = Relation.Relation("-[0]");
    assert(relation138.isValid() == False);
    
    relation139 = Relation.Relation("[0][1] + [0](1 - [1]) + (1-[0])[1] "
        "+ (1-[0])(1 - [1]) + [2](1 - [1])");
    assert(relation139.isValid() == False);
    
    relation140 = Relation.Relation("((([0]) + (1 - [0])) + 1(0))");
    assert(relation140.isValid() == False);
    
    relation141 = Relation.Relation(")1(");
    assert(relation141.isValid() == False);
    
    relation142 = Relation.Relation("]4[");
    assert(relation142.isValid() == False);
    
    relation143 = Relation.Relation("[6] -(");
    assert(relation143.isValid() == False);

    relation144 = Relation.Relation("1(1 - [1])");
    assert(relation144.isValid() == False);

    relation145 = Relation.Relation("(1 - [1])1");
    assert(relation145.isValid() == False);

# Helper function to test two unsorted arrays for equality.
def _areArraysEqual(arrayA, arrayB):
    hasEncounteredDiscrepancy = False;

    # create a list of all symbols in A
    symbolListConcatenation = "";
    index = 0;
    lengthOfA = len(arrayA);
    while (index < lengthOfA):
        currentElement = str(arrayA[index]);
        assert(currentElement.find('[') == -1);
        assert(currentElement.find(']') == -1);
        item = '[' + currentElement + ']';
        if (symbolListConcatenation.find(item) != -1):
            hasEncounteredDiscrepancy = True;
        symbolListConcatenation += item;
        index += 1;

    # eliminate every symbol in A that is also present in B
    index = 0;
    lengthOfB = len(arrayB);
    while (index < lengthOfB):
        currentElement = str(arrayB[index]);
        assert(currentElement.find('[') == -1);
        assert(currentElement.find(']') == -1);
        item = '[' + currentElement + ']';
        if (symbolListConcatenation.find(item) == -1):
            hasEncounteredDiscrepancy = True;
        symbolListConcatenation = symbolListConcatenation.replace(
            item, "");
        index += 1;
            
    if (symbolListConcatenation != ""):
        hasEncounteredDiscrepancy = True;

    return not hasEncounteredDiscrepancy;
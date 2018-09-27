# QuantumCounter/testQuantumCounter
# Nicholas Killeen,
# 19th June 2016.
# Unit tests for QuantumCounter.py.

import QuantumCounter;
import QuantumCounter.QuantumCounter as QuantumCounter;

def testQuantumCounter():
    # test constructor __init__, read, toString, and increment
    quantumCounter1 = QuantumCounter.QuantumCounter([0]);
    assert(quantumCounter1.read() == [0]);
    quantumCounter1.increment();
    assert(quantumCounter1.read() == [1]);
    assert(quantumCounter1.toString() == "[0]");
    quantumCounter1.increment();
    assert(quantumCounter1.read() == [0]);
    assert(quantumCounter1.toString() == "(1 - [0])");

    quantumCounter2 = QuantumCounter.QuantumCounter([-1]);
    bitState2 = quantumCounter2.read();
    assert(bitState2[0] != 0 and bitState2[0] != 1);
    quantumCounter2.increment();
    bitState2 = quantumCounter2.read();
    assert(bitState2[0] != 0 and bitState2[0] != 1);
    assert(quantumCounter2.toString() == "");

    quantumCounter3 = QuantumCounter.QuantumCounter([0, -1]);
    bitState3 = quantumCounter3.read();
    assert(bitState3[0] == 0)
    assert(bitState3[1] != 0 and bitState3[1] != 1);
    quantumCounter3.increment();
    assert(bitState3[0] == 1);
    assert(bitState3[1] != 0 and bitState3[1] != 1);

    quantumCounter4 = QuantumCounter.QuantumCounter([-1, 'v', 0.5]);
    quantumCounter4.increment();
    bitState4 = quantumCounter4.read();
    assert(bitState4[0] != 0 and bitState4[0] != 1);
    assert(bitState4[1] != 0 and bitState4[1] != 1);
    assert(bitState4[2] != 0 and bitState4[2] != 1);

    quantumCounter5 = QuantumCounter.QuantumCounter([-10, 0, 1.2]);
    assert(quantumCounter5.toString() == "(1 - [1])");
    bitState5 = quantumCounter5.read();
    assert(bitState5[0] != 0 and bitState5[0] != 1);
    assert(bitState5[1] == 0);
    assert(bitState5[2] != 0 and bitState5[2] != 1);
    quantumCounter5.increment();
    assert(quantumCounter5.toString() == "[1]");
    bitState5 = quantumCounter5.read();
    assert(bitState5[0] != 0 and bitState5[0] != 1);
    assert(bitState5[1] == 1);
    assert(bitState5[2] != 0 and bitState5[2] != 1);
    quantumCounter5.increment();
    bitState5 = quantumCounter5.read();
    assert(bitState5[0] != 0 and bitState5[0] != 1);
    assert(bitState5[1] == 0);
    assert(bitState5[2] != 0 and bitState5[2] != 1);

    quantumCounter6 = QuantumCounter.QuantumCounter([0, 0, 0, 1]);
    assert(quantumCounter6.toString() == "(1 - [0])(1 - [1])(1 - [2])[3]");
    assert(quantumCounter6.read() == [0, 0, 0, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.toString() == "(1 - [0])(1 - [1])[2](1 - [3])");
    assert(quantumCounter6.read() == [0, 0, 1, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 0, 1, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 1, 0, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 1, 0, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 1, 1, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 1, 1, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 0, 0, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 0, 0, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 0, 1, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 0, 1, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 1, 0, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 1, 0, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 1, 1, 0]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [1, 1, 1, 1]);
    quantumCounter6.increment();
    assert(quantumCounter6.read() == [0, 0, 0, 0]);

    quantumCounter7 = QuantumCounter.QuantumCounter([0, -1, "", 0, 0]);
    bitState7 = quantumCounter7.read();
    assert(bitState7[0] == 0);
    assert(bitState7[1] != 0 and bitState7[1] != 1);
    assert(bitState7[2] != 0 and bitState7[2] != 1);
    assert(bitState7[3] == 0);
    assert(bitState7[4] == 0);
    quantumCounter7.increment();
    bitState7 = quantumCounter7.read();
    assert(bitState7[0] == 0);
    assert(bitState7[1] != 0 and bitState7[1] != 1);
    assert(bitState7[2] != 0 and bitState7[2] != 1);
    assert(bitState7[3] == 0);
    assert(bitState7[4] == 1);
    quantumCounter7.increment();
    bitState7 = quantumCounter7.read();
    assert(bitState7[0] == 0);
    assert(bitState7[1] != 0 and bitState7[1] != 1);
    assert(bitState7[2] != 0 and bitState7[2] != 1);
    assert(bitState7[3] == 1);
    assert(bitState7[4] == 0);
    quantumCounter7.increment();
    bitState7 = quantumCounter7.read();
    assert(bitState7[0] == 0);
    assert(bitState7[1] != 0 and bitState7[1] != 1);
    assert(bitState7[2] != 0 and bitState7[2] != 1);
    assert(bitState7[3] == 1);
    assert(bitState7[4] == 1);
    quantumCounter7.increment();
    bitState7 = quantumCounter7.read();
    assert(bitState7[0] == 1);
    assert(bitState7[1] != 0 and bitState7[1] != 1);
    assert(bitState7[2] != 0 and bitState7[2] != 1);
    assert(bitState7[3] == 0);
    assert(bitState7[4] == 0);
    quantumCounter7.increment();

    quantumCounter8 = QuantumCounter.QuantumCounter([0, 1, 0, 1]);
    assert(quantumCounter8.read() == [0, 1, 0, 1]);
    quantumCounter8.increment();
    assert(quantumCounter8.read() == [0, 1, 1, 0]);
    quantumCounter8.increment();
    assert(quantumCounter8.read() == [0, 1, 1, 1]);
    quantumCounter8.increment();
    assert(quantumCounter8.read() == [1, 0, 0, 0]);

    # testing copyFrom
    quantumCounter9 = QuantumCounter.QuantumCounter([0, 5, '0', 1]);
    quantumCounter10 = QuantumCounter.QuantumCounter();
    quantumCounter10.copyFrom(quantumCounter9);
    assert(quantumCounter9.read() == quantumCounter10.read());
    
    # testing createCoefficientMap
    quantumCounter11 = QuantumCounter.QuantumCounter();
    quantumCounter11.createCoefficientMap([3]);
    assert(quantumCounter11.read()[3] == 0);
    quantumCounter11.increment();
    assert(quantumCounter11.read()[3] == 1);
    quantumCounter11.increment();
    assert(quantumCounter11.read()[3] == 0);

    quantumCounter12 = QuantumCounter.QuantumCounter();
    quantumCounter12.createCoefficientMap([0, 1, 2, 4]);
    bitState12 = quantumCounter12.read();
    assert(bitState12[0] == 0);
    assert(bitState12[1] == 0);
    assert(bitState12[2] == 0);
    assert(bitState12[3] != 0 and bitState12[3] != 1);
    assert(bitState12[4] == 0);

    quantumCounter13 = QuantumCounter.QuantumCounter();
    quantumCounter13.createCoefficientMap([1, 12, 2, 3]);
    quantumCounter14 = QuantumCounter.QuantumCounter(['0', 0, 0, 0, -1,
        2, 3, 5, "guacomole", "", -1.30001, 'v', 0]);

    # testing add
    quantumCounter15 = QuantumCounter.QuantumCounter(['a', 1, 2, 0, 1]);
    quantumCounter16 = QuantumCounter.QuantumCounter(['a', 1, 2, 0, 1]);
    quantumCounter15.increment();
    quantumCounter16.add(1);
    assert(quantumCounter15.read() == quantumCounter16.read());
    quantumCounter15.increment(); # 1
    quantumCounter15.increment(); # 2
    quantumCounter15.increment(); # 3
    quantumCounter15.increment(); # 4
    quantumCounter16.add(4);
    assert(quantumCounter15.read() == quantumCounter16.read());

    quantumCounter17 = QuantumCounter.QuantumCounter([0, 0, 0, 1, 'v', 
        0, 1, 0, 'v']);
    quantumCounter18 = QuantumCounter.QuantumCounter([0, 0, 0, 1, 'v', 
        0, 1, 0, 'v']);
    i = 0;
    while (i < 10):
        # increment 10 times
        quantumCounter17.increment();
        i += 1;
    quantumCounter18.add(10);
    assert(quantumCounter17.read() == quantumCounter17.read());
    while (i < 230):
        # increment 230 times
        quantumCounter17.increment();
        i += 1;
    quantumCounter18.add(229);
    quantumCounter18.increment();
    assert(quantumCounter17.read() == quantumCounter17.read());
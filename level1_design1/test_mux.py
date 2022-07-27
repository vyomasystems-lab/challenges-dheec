# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    inp0 = 0
    inp1 = 1
    inp2 = 2
    inp3 = 3
    inp4 = 0
    inp5 = 1
    inp6 = 2
    inp7 = 3
    inp8 = 0
    inp9 = 1
    inp10 = 2
    inp11 = 3
    inp12 = 0
    inp13 = 1
    inp14 = 2
    inp15 = 3
    inp16 = 0
    inp17 = 1
    inp18 = 2
    inp19 = 3
    inp20 = 0
    inp21 = 1
    inp22 = 2
    inp23 = 3
    inp24 = 0
    inp25 = 1
    inp26 = 2
    inp27 = 3
    inp28 = 0
    inp29 = 1
    inp30 = 2
    
    dut.tmp.value = 0
    
    #for i in range(4):
    dut.sel.value = 30
    await Timer(2, units='ns')
    if dut.sel.value == 0:
        tmp = dut.inp0.value 
    elif dut.sel.value == 1:
        tmp = dut.inp1.value 
    elif dut.sel.value == 2:
        tmp = dut.inp2.value
    elif dut.sel.value == 3:
        tmp = dut.inp3.value 
    elif dut.sel.value == 4:
        tmp = dut.inp4.value
    elif dut.sel.value == 5:
        tmp = dut.inp5.value 
    elif dut.sel.value == 6:
        tmp = dut.inp6.value
    elif dut.sel.value == 7:
        tmp = dut.inp7.value 
    elif dut.sel.value == 8:
        tmp = dut.inp8.value
    elif dut.sel.value == 9:
        tmp = dut.inp9.value 
    elif dut.sel.value == 10:
        tmp = dut.inp10.value
    elif dut.sel.value == 11:
        tmp = dut.inp11.value 
    elif dut.sel.value == 12:
        tmp = dut.inp12.value
    elif dut.sel.value == 13:
        tmp = dut.inp13.value 
    elif dut.sel.value == 14:
        tmp = dut.inp14.value
    elif dut.sel.value == 15:
        tmp = dut.inp15.value 
    elif dut.sel.value == 16:
        tmp = dut.inp17.value
    elif dut.sel.value == 18:
        tmp = dut.inp18.value 
    elif dut.sel.value == 19:
        tmp = dut.inp19.value
    elif dut.sel.value == 20:
        tmp = dut.inp20.value 
    elif dut.sel.value == 21:
        tmp = dut.inp21.value
    elif dut.sel.value == 22:
        tmp = dut.inp22.value 
    elif dut.sel.value == 23:
        tmp = dut.inp13.value
    elif dut.sel.value == 24:
        tmp = dut.inp24.value 
    elif dut.sel.value == 25:
        tmp = dut.inp25.value
    elif dut.sel.value == 26:
        tmp = dut.inp26.value 
    elif dut.sel.value == 27:
        tmp = dut.inp27.value
    elif dut.sel.value == 28:
        tmp = dut.inp28.value 
    elif dut.sel.value == 29:
        tmp = dut.inp29.value
    elif dut.sel.value == 30:
        tmp = dut.inp30.value 
    
    dut.out.value = tmp; 
    
    
    await Timer(2, units='ns')

    assert dut.out.value == dut.tmp.value, f"Mux result is incorrect: {dut.out.value} != {dut.tmp.value}"
    print("                      tmp : %d, out : %d, sel : %d" % (dut.tmp.value,dut.out.value,dut.sel.value))
    
    
    

    
    
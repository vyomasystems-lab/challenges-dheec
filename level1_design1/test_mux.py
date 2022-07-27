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
    
    
    dut.tmp.value = 1
    #for i in range(4):
    dut.sel.value = 30
    await Timer(2, units='ns')
    if dut.sel.value == 0:
         dut.inp0.value = tmp 
    elif dut.sel.value == 1:
          dut.inp1.value = tmp
    elif dut.sel.value == 2:
          dut.inp2.value = tmp
    elif dut.sel.value == 3:
          dut.inp3.value = tmp
    elif dut.sel.value == 4:
          dut.inp4.value = tmp
    elif dut.sel.value == 5:
          dut.inp5.value = tmp
    elif dut.sel.value == 6:
          dut.inp6.value = tmp
    elif dut.sel.value == 7:
          dut.inp7.value = tmp
    elif dut.sel.value == 8:
          dut.inp8.value = tmp
    elif dut.sel.value == 9:
          dut.inp9.value = tmp
    elif dut.sel.value == 10:
          dut.inp10.value = tmp
    elif dut.sel.value == 11:
          dut.inp11.value = tmp
    elif dut.sel.value == 12:
          dut.inp12.value = tmp
    elif dut.sel.value == 13:
          dut.inp13.value = tmp
    elif dut.sel.value == 14:
          dut.inp14.value = tmp
    elif dut.sel.value == 15:
          dut.inp15.value = tmp
    elif dut.sel.value == 16:
          dut.inp17.value = tmp
    elif dut.sel.value == 18:
          dut.inp18.value = tmp
    elif dut.sel.value == 19:
          dut.inp19.value = tmp
    elif dut.sel.value == 20:
          dut.inp20.value = tmp
    elif dut.sel.value == 21:
         dut.inp21.value = tmp
    elif dut.sel.value == 22:
          dut.inp22.value = tmp
    elif dut.sel.value == 23:
          dut.inp13.value = tmp
    elif dut.sel.value == 24:
          dut.inp24.value = tmp
    elif dut.sel.value == 25:
         dut.inp25.value = tmp
    elif dut.sel.value == 26:
          dut.inp26.value = tmp
    elif dut.sel.value == 27:
          dut.inp27.value = tmp
    elif dut.sel.value == 28:
          dut.inp28.value = tmp
    elif dut.sel.value == 29:
          dut.inp29.value = tmp
    elif dut.sel.value == 30:
          dut.inp30.value = tmp
    
    dut.out.value = tmp; 
    
    
    await Timer(2, units='ns')

    assert dut.out.value == dut.tmp.value, f"Mux result is incorrect: {dut.out.value} != {dut.tmp.value}"
    print("                      tmp : %d, out : %d, sel : %d" % (dut.tmp.value,dut.out.value,dut.sel.value))
    
    
    

    
    
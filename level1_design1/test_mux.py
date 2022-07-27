# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
        
    
    
    #for i in range(4):
    dut.sel.value = 9
    await Timer(2, units='ns')
    if dut.sel.value == 0:
         dut.inp0.value = 0
    elif dut.sel.value == 1:
          dut.inp1.value = 1
    elif dut.sel.value == 2:
          dut.inp2.value = 2
    elif dut.sel.value == 3:
          dut.inp3.value = 3 
    elif dut.sel.value == 4:
          dut.inp4.value = 0
    elif dut.sel.value == 5:
          dut.inp5.value = 1
    elif dut.sel.value == 6:
          dut.inp6.value = 2
    elif dut.sel.value == 7:
          dut.inp7.value = 3
    elif dut.sel.value == 8:
          dut.inp8.value = 0
    elif dut.sel.value == 9:
          dut.inp9.value = 1
    elif dut.sel.value == 10:
          dut.inp10.value = 2
    elif dut.sel.value == 11:
          dut.inp11.value = 3
    elif dut.sel.value == 12:
          dut.inp12.value = 0
    elif dut.sel.value == 13:
          dut.inp13.value = 1
    elif dut.sel.value == 14:
          dut.inp14.value = 2
    elif dut.sel.value == 15:
          dut.inp15.value = 3
    elif dut.sel.value == 16:
          dut.inp17.value = 0
    elif dut.sel.value == 18:
          dut.inp18.value = 1
    elif dut.sel.value == 19:
          dut.inp19.value = 2
    elif dut.sel.value == 20:
          dut.inp20.value = 3
    elif dut.sel.value == 21:
         dut.inp21.value = 0
    elif dut.sel.value == 22:
          dut.inp22.value = 1
    elif dut.sel.value == 23:
          dut.inp13.value = 2
    elif dut.sel.value == 24:
          dut.inp24.value = 3
    elif dut.sel.value == 25:
         dut.inp25.value = 0
    elif dut.sel.value == 26:
          dut.inp26.value = 1
    elif dut.sel.value == 27:
          dut.inp27.value = 2
    elif dut.sel.value == 28:
          dut.inp28.value = 3
    elif dut.sel.value == 29:
          dut.inp29.value = 0
    elif dut.sel.value == 30:
          dut.inp30.value = 1
          
    
    
    
    await Timer(2, units='ns')

    assert dut.out.value == dut.inp9.value, f"Mux result is incorrect: {dut.out.value} != {dut.inp9.value}"
    print("                      inp9 : %d, out : %d, sel : %d" % (dut.inp9.value,dut.out.value,dut.sel.value))
    
    
    

    
    
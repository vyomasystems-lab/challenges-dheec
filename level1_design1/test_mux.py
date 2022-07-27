# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
        
    
    dut.tmp.value = 1
    #for i in range(4):
    dut.sel.value = 30
    await Timer(2, units='ns')
    if dut.sel.value == 0:
         dut.inp0.value = dut.tmp.value 
    elif dut.sel.value == 1:
          dut.inp1.value = dut.tmp.value 
    elif dut.sel.value == 2:
          dut.inp2.value = dut.tmp.value 
    elif dut.sel.value == 3:
          dut.inp3.value = dut.tmp.value 
    elif dut.sel.value == 4:
          dut.inp4.value = dut.tmp.value 
    elif dut.sel.value == 5:
          dut.inp5.value = dut.tmp.value 
    elif dut.sel.value == 6:
          dut.inp6.value = dut.tmp.value 
    elif dut.sel.value == 7:
          dut.inp7.value = dut.tmp.value 
    elif dut.sel.value == 8:
          dut.inp8.value = dut.tmp.value 
    elif dut.sel.value == 9:
          dut.inp9.value = dut.tmp.value 
    elif dut.sel.value == 10:
          dut.inp10.value = dut.tmp.value 
    elif dut.sel.value == 11:
          dut.inp11.value = dut.tmp.value 
    elif dut.sel.value == 12:
          dut.inp12.value = dut.tmp.value 
    elif dut.sel.value == 13:
          dut.inp13.value = dut.tmp.value 
    elif dut.sel.value == 14:
          dut.inp14.value = dut.tmp.value 
    elif dut.sel.value == 15:
          dut.inp15.value = dut.tmp.value 
    elif dut.sel.value == 16:
          dut.inp17.value = dut.tmp.value 
    elif dut.sel.value == 18:
          dut.inp18.value = dut.tmp.value 
    elif dut.sel.value == 19:
          dut.inp19.value = dut.tmp.value 
    elif dut.sel.value == 20:
          dut.inp20.value = dut.tmp.value 
    elif dut.sel.value == 21:
         dut.inp21.value = dut.tmp.value 
    elif dut.sel.value == 22:
          dut.inp22.value = dut.tmp.value 
    elif dut.sel.value == 23:
          dut.inp13.value = dut.tmp.value 
    elif dut.sel.value == 24:
          dut.inp24.value = dut.tmp.value 
    elif dut.sel.value == 25:
         dut.inp25.value = dut.tmp.value 
    elif dut.sel.value == 26:
          dut.inp26.value = dut.tmp.value 
    elif dut.sel.value == 27:
          dut.inp27.value = dut.tmp.value 
    elif dut.sel.value == 28:
          dut.inp28.value = dut.tmp.value 
    elif dut.sel.value == 29:
          dut.inp29.value = dut.tmp.value 
    elif dut.sel.value == 30:
          dut.inp30.value = dut.tmp.value 
    
    dut.out.value = dut.tmp.value  
    
    
    await Timer(2, units='ns')

    assert dut.out.value == dut.tmp.value, f"Mux result is incorrect: {dut.out.value} != {dut.tmp.value}"
    print("                      tmp : %d, out : %d, sel : %d" % (dut.tmp.value,dut.out.value,dut.sel.value))
    
    
    

    
    
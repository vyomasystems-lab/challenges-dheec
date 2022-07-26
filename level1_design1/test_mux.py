# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    sel1=1
    #for i in range(4):
    dut.sel.value = 00001
    await Timer(2, units='ns')
    #dut.inp0.value = 0
    #await Timer(2, units='ns')
    dut.inp1.value = 1
    #dut.inp2.value = 2
    #dut.inp3.value = 3
    #dut.inp4.value = 0
    #dut.inp5.value = 1
    #dut.inp6.value = 2
    #dut.inp7.value = 3
    #dut.inp8.value = 0
    #dut.inp9.value = 1
    #dut.inp10.value = 2
    #dut.inp11.value = 3
    #dut.inp12.value = 0
    #dut.inp13.value = 1
    #dut.inp14.value = 2
    #dut.inp15.value = 3
    #dut.inp16.value = 0
    #dut.inp17.value = 1
    #dut.inp18.value = 2
    #dut.inp19.value = 3
    #dut.inp20.value = 0
    #dut.inp21.value = 1
    #dut.inp22.value = 2
    #dut.inp23.value = 3
    #dut.inp24.value = 0
    #dut.inp25.value = 1
    #dut.inp26.value = 2
    #dut.inp27.value = 3
    #dut.inp28.value = 0
    #dut.inp29.value = 1
    #dut.inp30.value = 2
    

    await Timer(2, units='ns')

    assert dut.out.value == 1, f"Mux result is incorrect: {dut.out.value} != (1)"
    print("tested the code for single  select value at a time");

    
    
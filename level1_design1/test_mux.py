# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    sel1=1
    for i in range(4):
        dut.sel.value = ~sel
        await Timer(2, units='ns')
        dut.inp0.value = 0
        await Timer(2, units='ns')
        dut.inp1.value = 1
        await Timer(2, units='ns')
    #dut.inp0.value = 02;
    #dut.inp0.value = 03;
    #dut.inp0.value = 00;

    await Timer(2, units='ns')

    assert dut.out.value == (1 or 0), f"Mux result is incorrect: {dut.out.value} != (1 or 0)"
    print("tested the code for 2 select values");

    
    
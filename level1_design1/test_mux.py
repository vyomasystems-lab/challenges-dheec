# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    
    dut.sel.value = ~1
    dut.inp0.value = 0
    dut.inp0.value = 1
    #dut.inp0.value = 02;
    #dut.inp0.value = 03;
    #dut.inp0.value = 00;

    await Timer(1, units='ns')

    assert dut.out.value == (1 or 0), f"Mux result is incorrect: {dut.X.value} != (1 or 0)"

    #for i in range(5):
    #    sel1  = random.randint(0, 31)

    #    dut.sel.value = sel1
    #    await Timer(2, units='ns')
    
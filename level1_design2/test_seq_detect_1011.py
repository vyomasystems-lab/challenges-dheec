# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    #for i in range (10):
    #    inp_bit = random.randint(0, 1)
    #    print("inp_bit = %d" % inp_bit)
    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 1
    print("seq_seen = %d" % dut.seq_seen.value)    
    
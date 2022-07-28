Test Scenario 
Test Inputs: sel = 30
Expected Output: out = inp30
Observed Output in the DUT dut.out=01
Output mismatches for the above inputs proving that there is a design bug

Design Bug
Based on the above test input and analysing the design, we see the following

Test Scenario 
Test Inputs: sel = 31
Expected Output: out = inp31
Observed Output in the DUT dut.out= NULL
Error:mux contains no object named inp31
Output mismatches for the above inputs proving that there is a design bug

Design Bug
Based on the above test input and analysing the design, we see the following
For 5 bit 'select' lines there should be 32 input lines.

Test Scenario 
Test Inputs: sel = 1
Expected Output: out = 0
Observed Output in the DUT dut.out= 'Z'
Error:ValueError : Unresolvable bit in binary string: 'z'
Output mismatches for the above inputs proving that there is a design bug

Design Bug
Based on the above test input and analysing the design, we see the following
Output should be'Zero' When only 'Select signal ' is there


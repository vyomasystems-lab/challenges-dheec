Test Scenario 
Test Inputs: sel = 30
Expected Output: out = inp30
Observed Output in the DUT dut.out=01
Output mismatches for the above inputs proving that there is a design bug

Design Bug
Based on the above test input and analysing the design, we see the following

 For 5 bit 'select' lines there should be 32 input lines.

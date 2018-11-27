2017 - Day 2

Part 1
For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

Read each row, find max and min, subtract, and to running total

Part 2
It sounds like the goal is to find the only two numbers in each row where one evenly divides the other.

Only 1 pair per row. So in each row we check each element to all the elements after it.
if i%j or j%i = 0 then they divide each other and we add those up

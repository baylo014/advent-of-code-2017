2017 - Day 1

Part 1
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.

For this problem, we can cycle though each element in the list, check the next element, and add to a running sum if they are the same.

Ex. 1122 should have a sum of 3
  11221 Should have a sum of 4 [circular]

Implemented in python is simple, just compare element i to (i+1)%l
We modulo to stop an out of bounds index.

Part 2
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.

Same logic, just compare element i to (i + l//2) % l
Again we modulo to account of out of bound and allows us to wrap around once we reach the half way point of the list

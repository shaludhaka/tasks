First take the lower limit and upper limit of range from user. Calculate mid value from these two limits to separate the range into two parts upper range and lower range.
Then create two list say left_list which will contain values from lower limit to mid value(excluding) and right_list which will contain values from mid value (excluding) to upper limit.

Start the while loop1 until the length of right_list becomes 73. In this loop random number is generated using Linear congruential generator(LCG) method in which an equation is used ie
[number = (increment + current time * multiplier) % mod] and then 'number' generated from this equation is put into [value = number / mod] (which will give output value between 0 and 1). And this value is put into a formula [lower limit + value * (upper limit - lower limit] to calculate random number in given desired range. Then add final value to right_list

Start the second while loop2 until the length of min list becomes 27.
Same procedure is done as above while loop1 Then add final value to left_list

Print both the right_list and left_list

Then print final_list ie concatenated list of right_list and left_list
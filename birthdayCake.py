import math
import os

import random
import re
import sys


#Task
# You are in charge of the cake for a child’s birthday. You have decided 
# the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
#candles = [4, 4, 1, 3]
#The maximum height candles are 4 units high. There are 2 of them, so return 2.

cand_count=int(input().strip())
candles = list(map(int, input().rstrip().split()))
def birthdayCakeCandles(candles):
    # Write your code here
    count=0
    maxHeight=max(candles)
    for height in candles:
        if height==maxHeight:
            count=count+1
    print(count)

    birthdayCakeCandles(candles)
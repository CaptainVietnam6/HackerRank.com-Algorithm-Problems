#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    array = sorted(arr)
    count = 0
    minimum = 0
    maximum = 0
    for i in range(len(array) - 1):
        minimum += arr[count]
        count += 1
    count = len(array)
    for i in range(len(array) - 1):
        maximum += array[count - 1]
        count -= 1
    print(f"{minimum} {maximum}")

if __name__ == '__main__':


    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

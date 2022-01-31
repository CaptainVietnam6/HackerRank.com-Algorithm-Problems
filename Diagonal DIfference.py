#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    elements_num = len(arr)
    right_down_diagonal = int((elements_num).math.sqrt() + 1)
    left_down_diagonal = int((elements_num).math.sqrt() - 2)
    values_to_add = int(elements_num).math.sqrt()
    diagonal_a = arr[0]
    diagonal_b = arr[values_to_add]
    
    for i in range(values_to_add):
        diagonal_a += arr[right_down_diagonal]
        right_down_diagonal += right_down_diagonal
        diagonal_b += arr[left_down_diagonal]
        left_down_diagonal += left_down_diagonal
        
    difference = int(diagonal_a - diagonal_b).abs()
    return difference
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

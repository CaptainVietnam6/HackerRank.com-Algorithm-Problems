#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    row = 1
    output = ""
    for i in range(n):
        row_out = ""
        for i in range(n - row):
            row_out = row_out + " "
        for i in range(row):
            row_out = row_out + "#"
        output = output + f"\n{row_out}"
        row += 1
    print("\n".join(output.split("\n")[1:]))


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    A.sort(reverse=True)
    B.sort()
    sum_list = [A[i] + B[i] for i in range(0,len(A))]
    if (all(i >= k for i in sum_list)):
        return "YES"
    else:
        return "NO"
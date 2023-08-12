#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    bad_letters = 0
    prev_check = "S"
    curr_check = "S"
    for i in range(0,len(s)):
        if(s[i]==curr_check):
            if (curr_check == "O"):
                curr_check = "S"
                prev_check = "O"
            else:
                if(curr_check=="S")&(prev_check=="O"):
                    curr_check="S"
                    prev_check="S"
                else:
                    curr_check="O"
                    prev_check="S"
        else:
            bad_letters=bad_letters+1
            if (curr_check == "O"):
                curr_check = "S"
                prev_check = "O"
            else:
                if(curr_check=="S")&(prev_check=="O"):
                    curr_check="S"
                    prev_check="S"
                else:
                    curr_check="O"
                    prev_check="S"
    return bad_letters
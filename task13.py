# Hackerrank
"""https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem"""

s = int(input().strip())
stairCaseVals = {1:1,2:2,3:4}

def stairCase(n):
    if n in stairCaseVals.keys():
        return stairCaseVals[n]
    else:
        stairCaseVals[n] = (stairCase(n-1)+ stairCase(n-2)+ stairCase(n-3))        
        return stairCaseVals[n]


for a0 in range(s):
    n = int(input().strip())
    print (stairCase(n))
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    val = -math.inf
    rows = len(arr)
    cols = len(arr[0])

    r = 0
    while r <= rows-3:
        c = 0
        while c <= cols-3:
            _val = float(arr[r][c]+arr[r][c+1]+arr[r][c+2]+\
                    arr[r+1][c+1]+\
                    arr[r+2][c]+arr[r+2][c+1]+arr[r+2][c+2])  
            if _val > val:
                val = _val
            c+=1
        r+=1

    return int(val)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

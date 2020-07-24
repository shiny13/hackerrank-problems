import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    a = dict(enumerate(arr,1))
    b = {v:k for k,v in a.items()}
    count = 0
    for i in a:
        x = a[i]
        if x!=i:
            y = b[i]
            a[y] = x
            b[x] = y
            count+=1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

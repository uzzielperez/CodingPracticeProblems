# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

import os

def findMedian(arr):
    # Write your code here
    sortedArr = sorted(arr)
    n = len(arr)
    if n%2 !=0:
        i = int(n/2)
        median = (sortedArr[i])
    elif n%2 == 0:
        i   = n/2
        j   = i - 1 
        median = (sortedArr[i] + sortedArr[j])/2
    return median
     
if __name__ == '__main__':
    # Hackerrank has predefined inputs 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

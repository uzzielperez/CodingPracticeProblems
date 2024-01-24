import sys

arr = [[1, 2, 3],[4, 5, 6],[9, 8, 9]]

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    print(n)
    sumLR, sumRL = 0, 0 
    i = 0 
    
    while i < n:
        # print (i, i, arr[i][i])
        print (i, n-1-i, arr[i][n-1-i])
        sumLR += arr[i][i]
        sumRL += arr[i][n-1-i]
        i += 1
    diagDiff = abs(sumLR-sumRL)
    return diagDiff

result = diagonalDifference(arr)
print(result)


    
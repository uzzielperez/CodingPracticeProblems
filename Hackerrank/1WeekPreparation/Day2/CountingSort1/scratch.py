arr = [1, 1, 3, 2, 1]

def countingSort(arr):
    # Write your code here

    i = 0 
    n = len(arr)
    freqArr = [0]*100
    
    while i < n:
        freqArr[arr[i]] += 1   
        print (i, arr[i], freqArr)
        i +=1
    return freqArr


    ##### FAILED for edge cases 
    # i = 0 
    # n = len(arr)
    # freqArr = [0]*n
    
    # while i < n:
    #     freqArr[arr[i]] += 1   
    #     print (i, arr[i], freqArr)
    #     i +=1
    # return freqArr

    ##### FAILED for an edge case 
    # max_val = max(arr)
    # freqArr = [0] * (max_val + 1)
    # for num in arr:
    #     freqArr[num] += 1
    # return freqArr

    # FAILED
    # min_val, max_val = min(arr), max(arr)
    # freqArr = [0] * (max_val - min_val + 1)

    # for num in arr:
    #     freqArr[num - min_val] += 1

    # return freqArr



    


result = countingSort(arr)
print(result)


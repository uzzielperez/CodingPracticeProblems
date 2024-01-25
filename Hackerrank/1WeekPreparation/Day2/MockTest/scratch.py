# I failed to solve this one in the time required (24 minutes)

matrix1 = [[1,2], [3,4]]
matrix2 = [[112, 42, 83, 113], [56, 135, 56, 47], [15, 78, 101, 43], [62, 98, 114, 108]]

def flippingMatrix(matrix):

    print ("original matrix:", matrix)
    n = int( len(matrix)/2 )
    print(n)

    # Reverse Column n 
    column = []
    for i in range(len(matrix)):
        column.append(matrix[len(matrix)-1-i][n])
        print(n-i, i, matrix[len(matrix)-1-i], len(matrix)-1-i)
    print("reversed column:", column)
   
    for i in range(len(matrix)):
        matrix[i][n] = column[i]
    

    print ("Reversed Column n: ", matrix)

    # Reverse Row 0
    matrix[0] = matrix[0][::-1]
    print ("Reversed Row 0:", matrix)

    # Sum of the First Quadrant
    qsum = 0
    for i in range(int(len(matrix)/2)):
        for j in range(int(len(matrix[i])/2)):
            e = matrix[i][j]
            print (e)
            qsum += e 
    
    print ("sum: %d" %(qsum))
         
# flippingMatrix(matrix1)
flippingMatrix(matrix2)
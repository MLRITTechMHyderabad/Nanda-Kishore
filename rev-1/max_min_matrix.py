def maxmin(matrix):
    print("Minimum element in a matrix :  " +str(min(min(row) for row in matrix)))
    print("Maximum element in a matrix :  "+str(max(max(row) for row in matrix)))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
maxmin(matrix)
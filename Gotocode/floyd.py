def floyd(n):
    matrix=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                matrix[i][j]=0
            else:
                matrix[i][j]=float('inf')

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])

    return matrix
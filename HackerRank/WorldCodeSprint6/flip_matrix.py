q = int(input())

for s in range(q):
    n = int(input())
    matrix = []
    matrix_size = 2*n
    for e in range(matrix_size):
        matrix.append([int(c) for c in input().split()])
    max_sum = 0
    for i in range(n):
        for j in range(n):
            biggest = matrix[i][j]
            if matrix[i][matrix_size-1-j] > biggest:
                biggest = matrix[i][matrix_size-1-j]
            if matrix[matrix_size-1-i][matrix_size-1-j] > biggest:
                biggest = matrix[matrix_size-1-i][matrix_size-1-j]
            if matrix[matrix_size-1-i][j] > biggest:
                biggest = matrix[matrix_size-1-i][j]
            max_sum += biggest
            
    print(max_sum)
            
import numpy as np
m=["0111", "1111", "1111", "1111"] 
def MatrixChallenge(matrix):
    if not matrix: return 0
    M = len(matrix)
    N = len(matrix[0])
    dp = [[0] * N for _ in range(M)]
    for i in range(M):
        dp[i][0] = int(matrix[i][0])
    for j in range(N):
        dp[0][j] = int(matrix[0][j])
    for i in range(1, M):
        for j in range(1, N):
            if int(matrix[i][j]) == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    return max(map(max, dp)) ** 2

def SearchingChallenge(strArr):
    row = len(strArr)
    
    col = len(strArr[0])
    def df(i,j):
        length=0
        v=strArr[i][j]
        for z,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
            if z>=0 and z<row and y>=0 and y<col and strArr[z][y]>v:
                length = max(length, df(z,y)+1)
        return length
    return max(df(i, j) for i in range(row) for j in range(col))

h=["67", "21", "45"] 
print(SearchingChallenge(h))


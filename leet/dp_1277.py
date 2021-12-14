def countSquares(matrix):
    start=matrix[0]
    column_n=len(start)
    row_n=len(matrix)
    numberofsq=0
 #   for i in range(len(matrix)):
  #      matrix[i]=[0]+matrix[i]
    for i in range(1,row_n):
        for j in range(1,column_n):
            if matrix[i][j]==1:
                matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
                
        
            else:
                continue
    for i in range(len(matrix)):
        numberofsq=sum(matrix[i])+numberofsq
        
    return numberofsq



def TreeConstructor(strArr):
  parents = {}
  children = {}
  for s in strArr:
    a, b = map(int, s.replace('(', '').replace(')', '').split(','))
    if a in parents:
      return False
    else:
      parents[a] = True
    if b in children:
      children[b] += 1
      if children[b] > 2:
        return False
    else:
      children[b] = 1
  return True


print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] ))

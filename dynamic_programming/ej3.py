import time
def minimizeMatrix(matrix, x, y):
  if x==0 and y==0:
    return matrix[0][0]
  
  if x<0 or y<0:
    return 100
  
  total = 0
  if x>0 or y>0:
    total = min(
      minimizeMatrix(matrix, x-1, y) + matrix[x][y], 
      minimizeMatrix(matrix, x, y-1) + matrix[x][y]
    )

  return total


def minimizeMDP(matrix, x, y, mdp):
  if mdp[x][y] == 0:
    total = min(
      minimizeMatrix(matrix, x-1, y) + matrix[x][y], 
      minimizeMatrix(matrix, x, y-1) + matrix[x][y]
    )

  return total

def minimize_iter(matrix):
  lenght_h = len(matrix)
  lenght_y = len(matrix[0])

  mdp = [
    [1000, 1000, 1000, 1000],
    [1000, 1000, 1000, 1000], 
    [1000, 1000, 1000, 1000],
    [1000, 1000, 1000, 1000]
  ]

  for i in range(lenght_h):
    for j in range(lenght_y):
      if i == 0 and j ==0:
        mdp[i][j] = matrix[i][j]
      else:
        mdp[i][j] = matrix[i][j] + min(mdp[i-1][j], mdp[i][j-1])
        
  return mdp[i][j]

if __name__ == "__main__" :
  matrix = [
    [2, 8, 3, 4],
    [5, 3, 4, 5], 
    [1, 2, 2, 1],
    [3, 4, 6, 5]
  ]

  mdp = [
    [0, 0, 0, 0],
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]
  
  current_time = time.time()
  print(current_time)
  #print(minimizeMatrix(matrix, len(matrix)-1, len(matrix[0])-1))
  #print(minimizeMDP(matrix, len(matrix)-1, len(matrix[0])-1, mdp )  )
  print(minimize_iter(matrix))
  print(time.time()-current_time)
 


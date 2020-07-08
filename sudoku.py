import random
import numpy as np
## Initialization Variables ## 
x = 0 

## Method Initialization ##

## ========================================= ##
##         Prettified Print Function         ##  
## ========================================= ##
def pprint(s, spacing="█", width=1):
  print("█" + spacing*width + s + spacing * width + "█") 

## ========================================= ##
## Check that the Sudoku Puzzle is Solvable, ## 
##             Else Return Fail              ## 
## ========================================= ##
def check(grid):

 for y in range (0,9): 
  if not len(np.unique(grid[y])) == 9:
    return 0 

  if not len(np.unique(grid[:, y])) == 9:
    return 0 
 ## Y,X is the coordinates of each 3x3 submatrix
 ## I is an interator to return each row of the 3x3 submatrix 
 for y in range (0,3):
  for x in range (0,3):
   temp = np.zeros((3,3))
   for i in range (0,3): 
    temp[i] = grid[ i + (3*x)][y*3:y*3+3]
   if not len(np.unique(temp)) == 9:
     return False
 return True

## ========================================= ##
##      Attempt to fill numbers into grid    ## 
## ========================================= ##

def genNumbers(): 
 #grid=np.zeros((9,9))
 grid = np.arange(100,181).reshape(9,9)

 for x in range(0,9):
  for y in range(0,9):
   failCount = 0 ## Init failcount everytime solver makes progression. 
   testGrid = grid   
   testGrid[x][y] = random.randint(1,9)

   while not check(testGrid): 
    if failCount > 250: ## Restart Condition
      return 0 
    testGrid[x][y] = random.randint(1,9) ## Attempt to fill grid.
    failCount = failCount + 1 

 if(check(grid)):
  return [1, grid]

## ========================================= ##
##     Print results...                      ## 
## ========================================= ##
def results(x):

  print("\r\n")
  a = x[1].copy().tolist()
  l = x[1].tolist() # Convert Numpy Array to List
  
  ## Eliminate Numbers from Sudoku Puzzle
  for elim in range(random.randint(30,40)):
   x = random.randint(0,8)
   y = random.randint(0,8)
   l[x][y] = "_" 
   
  ## Top Border
  print("█" * 15)
  for row in range(len(l)):
    r = l[row]
    if (row % 3 == 0):
      pprint(str("█" * 11))
    ## Print Rows (Strigify with Borders)
    pprint(str(r[0]) + str(r[1]) + str(r[2]) + "█" + str(r[3]) + str(r[4]) + str(r[5]) + "█" + str(r[6]) + str(r[7]) + str(r[8]))

  ## Bottom Border
  print("█" * 15)
  
  print("\r\n")
  print("*" * 15)
  print("#### ANSWER ###")
  print("*" * 15)
  print("\r\n")
 
  
  ## Top Border
  print("█" * 15)
  for row in range(len(a)):
    r = a[row]
    if (row % 3 == 0):
      pprint(str("█" * 11))
    ## Print Rows (Strigify with Borders)
    pprint(str(r[0]) + str(r[1]) + str(r[2]) + "█" + str(r[3]) + str(r[4]) + str(r[5]) + "█" + str(r[6]) + str(r[7]) + str(r[8]))

  ## Bottom Border
  print("█" * 15)
  
  print("\r\n")
## ========================================= ##
##     End Functions                         ## 
## ========================================= ##

## .init() ##
while x == 0:
 x = genNumbers()
results(x)



#  File: Triangle.py

#  Description: Min path sum for triangle

#  Student Name: Athul Srinivasaraghavan 

#  Student UT EID: as84444

#  Partner Name: None

#  Partner UT EID: N/a

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 03/28/2021

#  Date Last Modified:

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
  possibles = []
  brute_helper(grid, 0, 0, possibles, 0)
  maxval = 0
  for i in range(len(possibles)):
    if possibles[i] > maxval:
      maxval = possibles[i]
  return maxval

  return
def brute_helper (grid, idx, adj, possibles, count):
  if idx == len(grid):
    possibles.append(count)
  else:
    count += grid[idx][adj]
    return (brute_helper(grid, idx+1, adj, possibles, count)) or (brute_helper(grid, idx+1, adj+1, possibles, count))
# returns the greatest path sum using greedy approach
def greedy (grid):
  adj = 0
  count = 0
  for i in range(len(grid)):
    count += grid[i][adj]
    if i < len(grid)-1:
      if grid[i+1][adj+1] > grid[i+1][adj]:
        adj = adj + 1
  return count

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  possibles = []
  div_helper(grid, possibles, 0)
  maxval = 0
  for i in range(len(possibles)):
    if possibles[i] > maxval:
      maxval = possibles[i]
  return maxval

def div_helper (grid, possibles, count):
  if len(grid) == 1:
    possibles.append(count + grid[0][0])
  else:
    grida = []
    gridb = []
    for i in grid[1:]:
      grida.append(i[1:])
      gridb.append(i[:-1])
    count = count + grid[0][0]
    return (div_helper(grida, possibles, count)) or (div_helper(gridb, possibles, count))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  n = len(grid)
  y = len(grid[0])
  for i in range(n-2,-1,-1):
    for j in range(y):
      if grid[i][j] != 0:
        grid[i][j] += max(grid[i+1][j], grid[i+1][j+1])
  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  '''
  

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  print('The greatest path sum through exhaustive search is')
  print(brute_force(grid))
  # print time taken using exhaustive search
  print('The time taken for exhaustive search in seconds is')
  print(times)

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  print('The greatest path sum through greedy search is')
  print(greedy(grid))
  # print time taken using greedy approach
  print('The time taken for greedy search in seconds is')
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  print('The greatest path sum through divide and conquer search is')
  print(divide_conquer(grid))
  # print time taken using divide-and-conquer approach
  print('The time taken for divide and conquer search in seconds is')
  print(times)
  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  print('The greatest path sum through dynamic programming search is')
  print(dynamic_prog(grid))
  # print time taken using dynamic programming
  print('The time taken for dynamic programming search in seconds is')
  print(times)

if __name__ == "__main__":
  main()


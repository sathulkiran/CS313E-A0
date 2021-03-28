
#  File: Work.py

#  Description:

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID: as84444

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:03/04/2021

#  Date Last Modified:

import sys

import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  tot = v
  temp = 10
  mult = 1
  while temp > 0:
    x = v//k**mult
    tot += x
    temp = x
    mult += 1
  return tot



# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  v = 0
  for i in range(n+1):
    if sum_series(i,k)-n > -1:
      v = i
      break

  return v

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  lo = 1
  hi = n
  mid = (lo+hi)//2

  
  while abs(sum_series(mid,k)-n) > 1:
    mid = (lo+hi)//2
    if sum_series(mid,k)-n < 0:
      lo = mid
    if sum_series(mid,k)-n > 0:
      hi = mid
  if(sum_series(mid-1,k)-n) == 0:
    mid = mid - 1
  if (sum_series(mid,k)-n) < 0:
    mid += 1
  mid = mid
  
    
  return mid

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()


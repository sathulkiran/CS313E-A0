#  File: OfficeSpace.py

#  Description:

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID: as84444

#  Partner Name: None

#  Partner UT EID: None

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys
import math

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    ylen = rect[3]-rect[1]
    xlen = rect[2]-rect[0]
    return (xlen*ylen)

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    x11 = rect1[0]
    x12 = rect1[2]
    x21 = rect2[0]
    x22 = rect2[2]
    y11 = rect1[1]
    y12 = rect1[3]
    y21 = rect2[1]
    y22 = rect2[3]
    tup = []
    if (min(x12, x22)>max(x11, x21)) and (min(y12, y22)>max(y11, y21)):
        tup = [max(x11, x21), max(y11, y21), min(x12, x22),min(y12, y22)]
    else:
        tup = [0,0,0,0]
    newtup = tuple(tup)
    return newtup

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    ans = 0
    for i in bldg:
        for j in i:
            if j==0:
                ans +=1
    return ans

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    ans = 0
    for i in bldg:
        for j in i:
            if j>1:
                ans +=1
    return ans
# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    y2 = len(bldg)
    space = 0
    xb = rect[0]
    xt = rect[2]-1
    yb = y2 - rect[3]
    yt = y2 - rect[1]-1
    while yb <= yt:
        while xb <= xt:
            if bldg[yb][xb] == 1:
                space += 1
            xb += 1
        xb = rect[0]
        yb += 1
    return space
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    x2 = office[2]
    y2 = office[3]
    Matrix = [[0 for x in range(x2)] for y in range(y2)]
    for i in cubicles:
        xb = i[0]
        xt = i[2]-1
        yb = y2 - i[3]
        yt = y2 - i[1]-1
        while yb <= yt:
            while xb <= xt:
                Matrix[yb][xb] +=1
                xb += 1
            xb = i[0]
            yb += 1
    return Matrix



# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
  content = sys.stdin.readlines()
  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation
  n = int(content[1])
  tempcont = content.copy()
  tempcont.remove(tempcont[0])
  tempcont.remove(tempcont[0])
  names = []
  cubics = []
  for i in range(n):
      temp = tempcont[i].split()
      names.append(temp[0])
      x = (int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]))
      cubics.append(x)



  # compute the total office space
  temp = content[0].split()
  bldgtup = [0, 0, int(temp[0]), int(temp[1])]
  bldgtup = tuple(bldgtup)
  print('Total', area(bldgtup))
  bldg = request_space(bldgtup,cubics)

  # compute the total unallocated space
  
  print('Unallocated', unallocated_space(bldg))
  # compute the total contested space
  print('Contested', contested_space(bldg))
  # compute the uncontested space that each employee gets
  for i in range(n):
      print(names[i], uncontested_space(bldg,cubics[i]))



if __name__ == "__main__":
  main()

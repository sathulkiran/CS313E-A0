
#  File: Hull.py

#  Description: Calculate vertices that create convex hull for a given set of points

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID:as84444

#  Partner Name: None

#  Partner UT EID: N/a

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:02/28/2021

#  Date Last Modified:03/01/2021

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  deta = (q.x*r.y)-(q.y*r.x)
  detb = r.y-q.y
  detc = r.x-q.x
  totdet = deta-p.x*(detb)+p.y*(detc)
  return totdet

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  n = len(sorted_points)
  for i in range(2,n):
    upper_hull.append(sorted_points[i])
    while (len(upper_hull)>=3) and (det(upper_hull[-3], upper_hull[-2], upper_hull[-1])>=0):
      upper_hull.pop(-2)
  
  lower_hull = []
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
  for i in range(n-1,-1,-1):
    lower_hull.append(sorted_points[i])
    while (len(lower_hull)>=3) and (det(lower_hull[-3], lower_hull[-2], lower_hull[-1])>=0):
      lower_hull.pop(-2)
  
  lower_hull.pop()
  lower_hull.remove(lower_hull[0])
  for i in lower_hull:
    upper_hull.append(i)
  convex_hull = upper_hull

  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  n = len(convex_poly)
  fhalf = (convex_poly[0].y)*(convex_poly[n-1].x)
  shalf = (convex_poly[n-1].y)*(convex_poly[0].x)
  for i in range(n-1):
    temp = (convex_poly[i].x)*(convex_poly[i+1].y)
    temp2 = (convex_poly[i].y)*(convex_poly[i+1].x)
    fhalf += temp
    shalf += temp2
  deter = abs(fhalf-shalf)

  return ((1/2)*deter)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():

  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  
  # print the sorted list of Point objects
  #for p in sorted_points:
    #print (str(p))


  # get the convex hull
  x = convex_hull(sorted_points)
  
  # run your test cases

  # print your results to standard output
  
  # print the convex hull
  print('Convex Hull')
  for p in x:
    print (str(p))
  print()
  # get the area of the convex hull
  area = area_poly(x)
  


  # print the area of the convex hull
  print('Area of Convex Hull =', area)
if __name__ == "__main__":
  main()

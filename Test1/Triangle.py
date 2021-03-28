# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Athul Srinivasaraghavan

# Student UT EID:

# Course Name: CS 313E

# Unique Number:

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)



class Triangle (object):
    # constructor

    def __init__(self, PointA = Point(),PointB = Point(), PointC = Point()):
      self.PointA = PointA
      self.PointB = PointB
      self.PointC = PointC

    # print string representation of Triangle

    def __str__(self):
      return ('Point1: ({}, {}), Point2: ({}, {}), Point3: ({}, {}), Area: {}'.format(self.PointA.x, self.PointA.y, self.PointB.x, self.PointB.y, self.PointC.x, self.PointC.y, self.area()))

    # check congruence of Triangles with equality

    def __eq__(self, other):
      s11 = self.PointA.dist(self.PointB)
      s12 = self.PointA.dist(self.PointC)
      s13 = self.PointB.dist(self.PointC)
      s21 = other.PointA.dist(other.PointB)
      s22 = other.PointA.dist(other.PointC)
      s23 = other.PointB.dist(other.PointC)
      listA = [s11, s12, s13]
      listB = [s21, s22, s23]
      listA = sorted(listA)
      listB = sorted(listB)

      if listA == listB:
        return True
      else:
        return False

    # returns whether or not the triangle is valid

    def is_triangle(self):
      if self.area() <= TOL:
        return False
      else:
        return True

    # return the area of the triangle:

    def area(self):
      return abs((self.PointA.x * (self.PointB.y - self.PointC.y) + self.PointB.x * (self.PointC.y - self.PointA.y) + self.PointC.x * (self.PointA.y - self.PointB.y))/2)

######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())
    

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)

    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()

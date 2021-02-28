#  File: Geometry.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      self.x = x
      self.y = y
      self.z = z

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      return ('({}, {}, {})'.format(self.x, self.y, self.z))

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      dis = math.sqrt((self.x - other.x)**2+(self.y - other.y)**2+(self.z - other.z)**2)
      return dis

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):

      tol = 1.0e-6
      x = abs(self.x-other.x)
      y = abs(self.y-other.y)
      z = abs(self.z-other.z)
      if (x<tol) and (y<tol) and (z<tol):
          return True
      else:
          return False  

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      self.x = x
      self.y = y
      self.z = z
      self.radius = radius


  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      return ('Center: ({}, {}, {}), Radius: {}'.format(self.x, self.y, self.z, self.radius))

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      return (4*math.pi*self.radius**2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      return ((4/3)*math.pi*self.radius**3)

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      ref_point = Point(self.x, self.y, self.z)
      dis = ref_point.distance(p)
      if dis <= 1:
          return True
      else:
          return False


  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      ref_point = Point(self.x, self.y, self.z)
      ref_point2 = Point(other.x, other.y, other.z)
      if self.is_inside_point(ref_point2):
          dis = ref_point.distance(ref_point2)
          if (dis + other.radius)<self.radius:
              return True
          else:
              return False
      else:
          return False    

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      v1 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v2 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v3 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v4 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v5 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v6 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v7 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v8 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      if (self.is_inside_point(v1)) and (self.is_inside_point(v2)) and (self.is_inside_point(v3)) and (self.is_inside_point(v4)) and (self.is_inside_point(v5)) and (self.is_inside_point(v6)) and (self.is_inside_point(v7)) and (self.is_inside_point(v8)):
          return True
      else:
          return False  


  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      horiz_dist = math.sqrt((self.x-a_cyl.x)**2+(self.y-a_cyl.y)**2)+a_cyl.radius
      vert_distance = math.sqrt((self.z-a_cyl.z)**2)+(1/2)*a_cyl.height
      diag = math.sqrt((horiz_dist)**2+(vert_distance)**2)
      if diag <= self.radius:
          return True
      else:
          return False  


  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      refpoint = Point(other.x, other.y, other.z)
      refpoint2 = Point(self.x, self.y, self.z)
      if self.is_inside_sphere(other):
          return False
      if other.is_inside_sphere(self):
          return False
      if (refpoint.distance(refpoint2)<= self.radius) or (refpoint2.distance(refpoint) <= other.radius):
          return True
        

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      if (self.is_inside_cube(a_cube)):
          return False
      if (a_cube.is_inside_sphere(self)):
          return False  
      
      v1 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v2 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v3 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v4 = Point((a_cube.x+(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v5 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v6 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y+(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      v7 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z+(1/2)*a_cube.side))
      v8 = Point((a_cube.x-(1/2)*a_cube.side), (a_cube.y-(1/2)*a_cube.side), (a_cube.z-(1/2)*a_cube.side))
      if (self.is_inside_point(v1)) or (self.is_inside_point(v2)) or (self.is_inside_point(v3)) or (self.is_inside_point(v4)) or (self.is_inside_point(v5)) or (self.is_inside_point(v6)) or (self.is_inside_point(v7)) or (self.is_inside_point(v8)):
          return True
      else:
          return False 


  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      sidelen = math.sqrt(((self.radius*2)**2)/3)
      return (Cube(self.x, self.y, self.z, sidelen))

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      self.x = x
      self.y = y
      self.z = z
      self.side = side

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      return ('Center: ({}, {}, {}), Side: {}'.format(self.x, self.y, self.z, self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      return (6*(self.side**2))

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      return self.side**3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      side = self.side
      x_min = self.x-(side/2)
      y_min = self.y-(side/2)
      z_min = self.z-(side/2)
      x_max = self.x+(side/2)
      y_max = self.y+(side/2)
      z_max = self.z+(side/2)
      if ((p.x >= x_min) and (p.x <= x_max)) and ((p.y >= y_min) and (p.y <= y_max)) and ((p.z >= z_min) and (p.z <= z_max)):
          return True
      else:
          return False  

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      v1 = Point((self.x+(1/2)*self.side), (self.y+(1/2)*self.side), (self.z+(1/2)*self.side))
      v2 = Point((self.x+(1/2)*self.side), (self.y+(1/2)*self.side), (self.z-(1/2)*self.side))
      v3 = Point((self.x+(1/2)*self.side), (self.y-(1/2)*self.side), (self.z+(1/2)*self.side))
      v4 = Point((self.x+(1/2)*self.side), (self.y-(1/2)*self.side), (self.z-(1/2)*self.side))
      v5 = Point((self.x-(1/2)*self.side), (self.y+(1/2)*self.side), (self.z+(1/2)*self.side))
      v6 = Point((self.x-(1/2)*self.side), (self.y+(1/2)*self.side), (self.z-(1/2)*self.side))
      v7 = Point((self.x-(1/2)*self.side), (self.y-(1/2)*self.side), (self.z+(1/2)*self.side))
      v8 = Point((self.x-(1/2)*self.side), (self.y-(1/2)*self.side), (self.z-(1/2)*self.side))
      if (a_sphere.is_inside_point(v1)) or (a_sphere.is_inside_point(v2)) or (a_sphere.is_inside_point(v3)) or (a_sphere.is_inside_point(v4)) or (a_sphere.is_inside_point(v5)) or (a_sphere.is_inside_point(v6)) or (a_sphere.is_inside_point(v7)) or (a_sphere.is_inside_point(v8)):
          return False
      sx = a_sphere.x
      sy = a_sphere.y
      sz = a_sphere.z
      cx = self.x
      cy = self.y
      cz = self.z
      shalf = self.side/2
      r = a_sphere.radius
      if (sx+r>cx+shalf) or (sx-r<cx-shalf) or (sy+r>cy+shalf)or(sy-r<cy-shalf) or (sz+r>cz+shalf)or(sz-r<cz-shalf):
          return False
      return True  

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      
      v1 = Point((other.x+(1/2)*other.side), (other.y+(1/2)*other.side), (other.z+(1/2)*other.side))
      v2 = Point((other.x+(1/2)*other.side), (other.y+(1/2)*other.side), (other.z-(1/2)*other.side))
      v3 = Point((other.x+(1/2)*other.side), (other.y-(1/2)*other.side), (other.z+(1/2)*other.side))
      v4 = Point((other.x+(1/2)*other.side), (other.y-(1/2)*other.side), (other.z-(1/2)*other.side))
      v5 = Point((other.x-(1/2)*other.side), (other.y+(1/2)*other.side), (other.z+(1/2)*other.side))
      v6 = Point((other.x-(1/2)*other.side), (other.y+(1/2)*other.side), (other.z-(1/2)*other.side))
      v7 = Point((other.x-(1/2)*other.side), (other.y-(1/2)*other.side), (other.z+(1/2)*other.side))
      v8 = Point((other.x-(1/2)*other.side), (other.y-(1/2)*other.side), (other.z-(1/2)*other.side))
      if (self.is_inside_point(v1)) and (self.is_inside_point(v2)) and (self.is_inside_point(v3)) and (self.is_inside_point(v4)) and (self.is_inside_point(v5)) and (self.is_inside_point(v6)) and (self.is_inside_point(v7)) and (self.is_inside_point(v8)):
          return True
      elif (self.x == other.x) and (self.y == other.y) and (self.z == other.z) and (self.side == other.side):
          return True
      else:
          return False       

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      cyx = a_cyl.x
      cyy = a_cyl.y
      cyz = a_cyl.z
      r = a_cyl.radius
      h = a_cyl.height/2
      cx = self.x
      cy = self.y
      cz = self.z
      shalf = self.side/2
      if (cyx+r>cx+shalf) or (cyx-r<cx-shalf) or (cyy+r>cy+shalf)or(cyy-r<cy-shalf) or (cyz+h>cz+shalf)or(cyz-h<cz-shalf):
          return False 
      return True        
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
      if (self.is_inside_cube(other)) or (other.is_inside_cube(self)):
          return False
      v1 = Point((other.x+(1/2)*other.side), (other.y+(1/2)*other.side), (other.z+(1/2)*other.side))
      v2 = Point((other.x+(1/2)*other.side), (other.y+(1/2)*other.side), (other.z-(1/2)*other.side))
      v3 = Point((other.x+(1/2)*other.side), (other.y-(1/2)*other.side), (other.z+(1/2)*other.side))
      v4 = Point((other.x+(1/2)*other.side), (other.y-(1/2)*other.side), (other.z-(1/2)*other.side))
      v5 = Point((other.x-(1/2)*other.side), (other.y+(1/2)*other.side), (other.z+(1/2)*other.side))
      v6 = Point((other.x-(1/2)*other.side), (other.y+(1/2)*other.side), (other.z-(1/2)*other.side))
      v7 = Point((other.x-(1/2)*other.side), (other.y-(1/2)*other.side), (other.z+(1/2)*other.side))
      v8 = Point((other.x-(1/2)*other.side), (other.y-(1/2)*other.side), (other.z-(1/2)*other.side))
      if (self.is_inside_point(v1)) or (self.is_inside_point(v2)) or (self.is_inside_point(v3)) or (self.is_inside_point(v4)) or (self.is_inside_point(v5)) or (self.is_inside_point(v6)) or (self.is_inside_point(v7)) or (self.is_inside_point(v8)):
          return True  

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      return


  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  
  def inscribe_sphere (self):
      return

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      self.x = x
      self.y = y
      self.z = z
      self.radius = radius
      self.height = height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      return ('Center: ({}, {}, {}), Radius: {}, Height: {}'.format(self.x, self.y, self.z, self.radius, self.height))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      return (((math.pi*self.radius**2)*2)+(2*math.pi*self.radius*self.height))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      return (math.pi*self.radius**2*self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      return

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      return

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # self is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      return

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      return

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      return

def main():
  # read data from standard input
  content = sys.stdin.readlines()

  # read the coordinates of the first Point p
  test = content[0].split()

  # create a Point object 
  p = Point(float(test[0]), float(test[1]), float(test[2]))
  # read the coordinates of the second Point q
  test2 = content[1].split()
  # create a Point object 
  q = Point(float(test2[0]), float(test2[1]), float(test2[2]))
  # read the coordinates of the center and radius of sphereA
  
  # create a Sphere object 

  # read the coordinates of the center and radius of sphereB

  # create a Sphere object

  # read the coordinates of the center and side of cubeA

  # create a Cube object 

  # read the coordinates of the center and side of cubeB

  # create a Cube object 

  # read the coordinates of the center, radius and height of cylA

  # create a Cylinder object 

  # read the coordinates of the center, radius and height of cylB

  # create a Cylinder object


  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin


  # print if Point p is inside sphereA

  # print if sphereB is inside sphereA

  # print if cubeA is inside sphereA

  # print if cylA is inside sphereA

  # print if sphereA intersects with sphereB

  # print if cubeB intersects with sphereB

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA


  # print if Point p is inside cubeA

  # print if sphereA is inside cubeA

  # print if cubeB is inside cubeA

  # print if cylA is inside cubeA

  # print if cubeA intersects with cubeB

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA


  # print if Point p is inside cylA

  # print if sphereA is inside cylA

  # print if cubeA is inside cylA

  # print if cylB is inside cylA

  # print if cylB intersects with cylA

if __name__ == "__main__":
  main()

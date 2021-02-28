#  File: Intervals.py

#  Description: Creating spiral matrix and summining around specific number

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID:as84444

#  Partner Name:none

#  Partner UT EID:none

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 01/29/2021

#  Date Last Modified: 02/01/2021

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

import sys

def merge_tuples (tuples_list):

   # Input: tuples_list is a list of tuples of denoting intervals
   # Output: a list of tuples sorted by ascending order of the size of
   #         the interval
   #         if two intervals have the size then it will sort by the
   #         lower number in the interval
   
   templist = []

   for i in tuples_list:
       a = i[0]
       b = i[1]
       for j in tuples_list:
           if j != i:

                if (j[0]<a and j[1]>=a and j[1]<b):
                    a = j[0]
                    tuples_list.remove(j)
                elif (j[0]<b and j[0]>a and j[1]>=b):
                    b = j[1]
                    tuples_list.remove(j)
                elif (j[0]<=a and j[1]>=b):
                    a = j[0]
                    b = j[1]
                    tuples_list.remove(j)
                elif (j[0]>=a and j[1]<=b):
                        tuples_list.remove(j)
       temp = []
       temp.append(a)
       temp.append(b)
       x = tuple(temp)
       y = tuples_list.index(i)
       tuples_list[y] = x

   tuples_list.sort() 
   return tuples_list  



def sort_by_interval_size (tuples_list):
    sorted_list = []
    for i in tuples_list:
        ref = tuples_list.index(i)
        templist = []
        a = i[0]
        b = i[1]
        for j in tuples_list:
            x = j[0]
            y = j[1]
            if abs(y-x) < abs(b-a):
                ref = tuples_list.index(j)
                a = x
                b = y
        templist.append(a)
        templist.append(b)
        tuples_list.remove(tuples_list[ref])
        z = tuple(templist)
        sorted_list.append(z)
    return sorted_list 

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():


  # open file intervals.in and read the data and create a list of tuples

   content = sys.stdin.readlines()
   n = int(content[0])
   tups = []
   for i in range(n+1):
       if i > 0:
           x = content[i].split()
           y = []
           y.append(int(x[0]))
           y.append(int(x[1]))
           z = tuple(y)
           tups.append(z)



   

    




  # merge the list of tuples
   new_tups = merge_tuples(tups)
   print(new_tups)
  # sort the list of tuples according to the size of the interval
   new_tups = sort_by_interval_size(new_tups)
  # run your test cases


  # write the output list of tuples from the two functions
   print(new_tups)
if __name__ == "__main__":
  main()
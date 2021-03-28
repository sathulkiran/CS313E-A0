#  File: Modulo.py

#  Description: Determines if a list of integers is closed under modulo (x % y is also a member # of the list for any nonzero x and y in the list)

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

import sys

# Input: lst is a list of positive integers that includes 0
# Output: return True if for any 2 nonzero elements x and y in the list, x % y is also in the list
# return False otherwise

def is_closed_modulo(lst):
    
    for i in lst:
        if i != 0:
            #cop1 = lst.copy()
            #cop1.remove(i)
            for j in lst:
                if j != 0:
                    key = i%j
                    cop = lst.copy()
                    cop.remove(i)
                    if (key in lst) == False:
                        return False
    return True


def main(): 
    # read input file
    lst = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    # get result from your call to is_closed_modulo()
    result = is_closed_modulo(lst)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()
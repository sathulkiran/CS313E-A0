#  File: Palindrome.py

#  Description: return shortest palindrome by modifying input string

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID:as84444

#  Partner Name:none

#  Partner UT EID:n/a

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:03/08/2021

#  Date Last Modified:03/09/2021

import sys

def check_palin(str):
  n = len(str)
  forw = []
  back = []
  lim = (-1*(n//2))-1
  if n%2 == 0:
    for i in range(n//2):
      forw.append(str[i])
    for i in range(-1, lim, -1):
      back.append(str[i])
  else:
    for i in range(n//2):
      forw.append(str[i])
    for i in range(-1, lim, -1):
      back.append(str[i])
  if forw == back:
    return True
  else:
    return False


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
  str = str.rstrip()
  n = -1*(len(str)+1)
  if check_palin(str):
    return str
  count = 0
  for i in range(-1, n, -1):
    str = str[:count]+str[i]+str[count:]
    if check_palin(str):
      return str
    count += 1

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''

    # read the data
    content = sys.stdin.readlines()
    n = len(content)
    for i in range(n):
      print(smallest_palindrome(content[i]))

    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()
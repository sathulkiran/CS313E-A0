
import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  n = len(strng)
  test = len(strng)
  if math.sqrt(test).is_integer():
    x = int(math.sqrt(test))
  else:
    x = math.ceil(math.sqrt(test))
  Matrix = [[0 for x in range(x)] for y in range(x)] 
  col = x-1
  row = 0

  for i in range(n):
    Matrix[row][col] = strng[i]
    row += 1
    if row == x:
      row = 0
      col -= 1  
  decrypstring = ''
  for i in Matrix:
    for j in i:

      if (j != '\n') and (j != 0):
        decrypstring += j
  
  return decrypstring


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
  n = len(strng)

  test = len(strng)
  if math.sqrt(test).is_integer():
    x = int(math.sqrt(test))
  else:
    x = math.ceil(math.sqrt(test))
  Matrix = [[0 for x in range(x)] for y in range(x)] 
  numblank = x**2-n
  col = 0
  row = x-1
  tempcol = 0
  temprow = x-1
  if numblank != 0:
    for i in range(numblank):
      Matrix[temprow][tempcol] = '*'
      temprow -= 1
      if temprow == -1:
        tempcol += 1
        temprow = x-1
  itercount = 0
  newrow = 0
  newcol = x-1
  for i in range(x):
    for j in range(x):
      if Matrix[i][j] == 0:
        Matrix[i][j] = strng[itercount]
        itercount += 1
  decrypstring = ''
  for i in range(x):
    for j in range(x):

      if Matrix[newrow][newcol] != '*':
        decrypstring += Matrix[newrow][newcol]
        newrow += 1
      if newrow == x:
        newrow = 0
        newcol -= 1
  return decrypstring


def main():

  # read the strings P and Q from standard input
   content = sys.stdin.readlines()
   p = content[0]
   q = content[1]
   

  # encrypt the string P
   x = encrypt(p)
  # decrypt the string Q
   y = decrypt(q)
  # print the encrypted string of P
   print(x)
  # and the decrypted string of Q
   print(y)

if __name__ == "__main__":
  main()



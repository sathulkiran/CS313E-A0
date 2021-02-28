#  File: Spiral.py

#  Description: Creating spiral matrix and summining around specific number

#  Student Name: Athul Srinivasaraghavan

#  Student UT EID:as84444

#  Partner Name:none

#  Partner UT EID:none

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 01/29/2021

#  Date Last Modified: 02/01/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral (n):
    if n%2 ==1:
        n = n+1
    rows, cols = (n, n) 
    spiral=[] 
    for i in range(cols): 
        col = [] 
        for j in range(rows): 
            col.append(0) 
        spiral.append(col)
   
    x = n//2
    y = n//2
    spiral[x][y]=1
    i= 0
    k = n
    square = 4*k - 4
    row = 0
    col = n-1
    top_right = n*n 
    #number of outer squares 
    c = n//2
    for i in range(c):
        square = 4*(k-(2*i))-4 
        start_row = i
        start_col = n - 1 - i 
        row = start_row
        col = start_col
        for i in range(square):
            #fill top side
            if col>start_row and row == start_row:
                spiral[row][col] = top_right 
                top_right -= 1
                col -=1
            elif row<(start_col) and col ==start_row: 
                spiral[row][col] = top_right 
                top_right -= 1
                row = row + 1
            #fill bottom side
            elif col<(start_col) and row == (start_col):
                spiral[row][col] = top_right 
                top_right -=1
                col += 1
            elif row>start_row and col == start_col:
                spiral[row][col]=top_right 
                top_right -=1
                row -=1
    return spiral



# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

    
def sum_adjacent_numbers (spiral, n):
    dim = len(spiral)
    sumval = 0
    a = 0
    b = 0
    row = 0
    col = 0
    for i in range(dim):
        for j in range(dim):
            if spiral[i][j]==n:
                row=i 
                col=j
                a=row-1 
                b=col-1
                
                
                for x in range(3):
                    for y in range(3):
                        if (a>=0 and a<=(dim-1)) and (b>=0 and b<=(dim-1)):
                            
                            sumval += spiral[a][b] 
                            
                        b+=1
                    a+=1
                    b=col-1
                break 
    sumval -= n            
    return sumval

def main():

  # read the input file
    content = sys.stdin.readlines()
    n = int(content[0])
    in1 = int(content[1])
    in2 = int(content[2])
    in3 = int(content[3])
    in4 = int(content[4])

  # create the spiral
    spi = create_spiral(n)
  # add the adjacent numbers
    out1 = sum_adjacent_numbers(spi, in1)
    out2 = sum_adjacent_numbers(spi, in2)
    out3 = sum_adjacent_numbers(spi, in3)
    out4 = sum_adjacent_numbers(spi, in4)
  # print the result
 
    print(out1)
    print(out2)
    print(out3)
    print(out4)

  
if __name__ == "__main__":
  main()
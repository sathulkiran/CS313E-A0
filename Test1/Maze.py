#  File: Maze.py

#  Description: Determine if you can escape the maze

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number: 

import sys

# determines whether we can escape this maze with k energy
# returns a Boolean
def solve(maze, energy):
    rows = len(maze)
    cols = len(maze[0])
    neweng = [[0]*cols for k in range(rows)]
    neweng[0][0] = maze[0][0]
    for j in range(1,cols):
        neweng[0][j] = maze[0][j] + maze[0][j-1]
    for i in range(1,rows):
        neweng[i][0] = maze[i][0] + maze[i-1][0]
    for i in range(1,rows):
        for j in range(1,cols):
            neweng[i][j] = min(neweng[i-1][j], neweng[i][j-1]) + maze[i][j]
    if neweng[rows-1][cols-1] <= energy:
        return True
    else:
        return False

def main():
    # read in N (maze size)
    N = int(sys.stdin.readline().strip())
 
    # read in K (amount of energy)
    energy = int(sys.stdin.readline().strip())
 
    # read in the maze
    maze = [[0 for i in range(N)] for k in range(N)]
    for i in range(N):
        line = sys.stdin.readline().strip().split(" ")
        for k in range(N):
            maze[i][k] = int(line[k])
 
    # determine if the maze can be escaped
    if solve(maze, energy):
        print("ESCAPED")
    else:
        print("TRAPPED")
 
if __name__ == "__main__":
    main()
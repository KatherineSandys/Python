#useing backtracking

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#print out the board
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="") #doesnt add /n at the end

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="") #doesnt add /n at the end

    print("") #add a newline afterwards

#find an empty square and return the position
def find_empty(bo):
    #loop through board and find a space that equals 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                #return a tuple of the position
                return (i, j) #row, col

    return None #if there are no empty spots

#check if the baord is valid
def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range (box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    #only reached if conditions are met
    return True

#solve ther board useing recrusion
def solve(bo):
    #check to see if board is comeplete, ie at the bottum right corner
    find = find_empty(bo)
    if not find:
        return True #means we have comepleted the baord
    else:
        row, col = find

    for i in range(1, 10): #loop 1 through 9
        if valid(bo, i, (row, col)):
            bo[row][col] = i #add into board

            if solve(bo):
                return True

            bo[row][col] = 0 #backtracking

    return False

print_board(board)
solve(board)
print_board(board)

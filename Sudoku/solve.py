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

#

print_board(board)

import random

#print out the board
def print_board(board_user):
    for i in range(len(board_user)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range(len(board_user[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="") #doesnt add /n at the end

            if j == 8:
                if board_user[i][j] == 0:
                    print(" ")
                else:
                    print(board_user[i][j])
            else:
                if board_user[i][j] == 0:
                    print("  ", end="")
                else:
                    print(str(board_user[i][j]) + " ", end="") #doesnt add /n at the end

def check_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if check_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board):
    number_list = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(number_list)
                for num in number_list:
                    if check_valid(board, num, (i, j)):
                        board[i][j] = num
                        if not find_empty(board) or fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def remove_numbers_from_board(board, num_holes):
    while num_holes > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_holes -= 1

def generate_sudoku_puzzle(difficulty="medium"):
    difficulty_map = {
        "easy": 30,
        "medium": 40,
        "hard": 50
    }
    
    num_holes = difficulty_map.get(difficulty, 40)
    full_board = generate_full_board()
    remove_numbers_from_board(full_board, num_holes)
    return full_board

# Generate and print a Sudoku puzzle
difficulty = "medium"  # "easy", "medium", or "hard"
sudoku_puzzle = generate_sudoku_puzzle(difficulty)
print_board(sudoku_puzzle)

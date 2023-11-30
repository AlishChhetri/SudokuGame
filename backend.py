import random


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("─" * 21)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("│", end=" ")

            if j == 8:
                print("▢" if board[i][j] == 0 else board[i][j])
            else:
                if board[i][j] == 0:
                    print("▢", end=" ")
                else:
                    print(f"{board[i][j]}", end=" ")


def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)

    empty_cells = random.randint(40, 50)
    while empty_cells > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            empty_cells -= 1

    return board

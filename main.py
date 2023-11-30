from backend import print_board, is_valid, solve, generate_sudoku


def game():
    sudoku_board = generate_sudoku()
    solved_board = [row[:] for row in sudoku_board]
    original_board = [row[:] for row in sudoku_board]
    print("\nSudoku!")
    print()
    print_board(sudoku_board)

    while True:
        print()
        row = int(input("Enter row (1-9, or 0 to exit): ")) - 1
        if row == -1:
            print()
            print("Exiting the game. Goodbye!")
            break

        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter a number (1-9): "))
        print()

        if original_board[row][col] != 0:
            print()
            print("You cannot modify the original number!", style="bold red")
        elif is_valid(sudoku_board, num, (row, col)):
            sudoku_board[row][col] = num
        else:
            print()
            print("Invalid move! Try again.", style="bold red")
            print()

        print_board(sudoku_board)

    print("\nSolved:")
    print()
    solve(solved_board)
    print_board(solved_board)
    print()


if __name__ == "__main__":
    game()

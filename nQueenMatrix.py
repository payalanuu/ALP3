# N-Queens using Backtracking

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    # All queens are placed
    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main program
n = int(input("Enter number of queens: "))

if n <= 0:
    print("Enter a positive number")

elif n == 1:
    print("Final N-Queens Matrix:")
    print("1")

else:
    board = [[0 for j in range(n)] for i in range(n)]

    # Place first queen
    board[0][0] = 1

    print("\nInitial Matrix:")
    for row in board:
        print(*row)

    if solve(board, 1, n):

        print("\nFinal N-Queens Matrix:")
        for row in board:
            print(*row)

    else:
        print("\nSolution does not exist with first queen at (0,0).")





#   Sample Output=
# Test case: N = 4
# Enter number of queens: 4

# Initial Matrix:
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

# Final N-Queens Matrix:
# 1 0 0 0
# 0 0 1 0
# 0 0 0 1
# 0 1 0 0
def num_paths_bishop(n, x1, y1):
    return min(n-x1, n-y1) + min(x1-1, y1-1)

def num_paths_rook(n, x1, y1):
    return 2*(n-1)

def num_paths_queen(n, x1, y1):
    return num_paths_bishop(n, x1, y1) + num_paths_rook(n, x1, y1)

# Example usage: print the number of unique paths for a bishop starting at position (2, 3) on a 5 x 5 board
n = 5
x1 = 2
y1 = 3
print(num_paths_bishop(n, x1, y1)) # expected output: 2

# Example usage: print the number of unique paths for a rook starting at position (1, 1) on a 4 x 4 board
n = 4
x1 = 1
y1 = 1
print(num_paths_rook(n, x1, y1)) # expected output: 6

# Example usage: print the number of unique paths for a queen starting at position (3, 4) on a 6 x 6 board
n = 6
x1 = 3
y1 = 4
print(num_paths_queen(n, x1, y1)) # expected output: 14

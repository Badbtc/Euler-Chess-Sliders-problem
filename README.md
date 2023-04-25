# Euler-Chess-Sliders-problem

<a>The Chess Sliders problem involves finding the number of unique paths that a bishop, rook, or queen can take on a chessboard of size n x n, starting at a given position and moving only diagonally (for the bishop), horizontally or vertically (for the rook and queen). Here are the steps to solve this problem:</a>

1-For the bishop, we can find the number of unique paths by counting the number of squares on each of the two diagonals that the bishop can reach from its starting position.
If the starting position is (x1, y1) and the board size is n x n, then the bishop can reach a maximum of min(n-x1, n-y1) squares on the upper-right diagonal and min(x1-1, y1-1) squares on the lower-left diagonal.
The total number of unique paths for the bishop is the sum of these two values.

2-For the rook, we can find the number of unique paths by counting the number of squares on the same row or column as the starting position. If the starting position is (x1, y1) and the board size is n x n, then the rook can reach a maximum of n-1 squares on the same row or column. The total number of unique paths for the rook is twice this value (since it can move in either direction along the row or column).

3-For the queen, we can find the number of unique paths by adding the number of paths for the bishop and the rook (since the queen can move like both pieces).

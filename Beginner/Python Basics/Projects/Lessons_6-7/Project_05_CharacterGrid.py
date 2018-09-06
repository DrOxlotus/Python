# This project references skills learned from lessons 1-7.

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

for i in range(len(grid)):
    for j in range(len(grid)):
        try:
            if j == (len(grid) - 1):
                print(grid[j][i])
            else:
                print(grid[j][i], end = " ")
        except IndexError:
            continue

import sys
sys.setrecursionlimit(10000)

def recurse(grid, i, j): # i: depth, j: row pointer
  if i == len(grid):
    return max(grid[i-1])

  if j == 0:
    grid[i][j] += grid[i-1][j]
    return recurse(grid, i, j+1)

  if j == len(grid[i])-1:
    grid[i][j] += grid[i-1][j-1]
    return recurse(grid, i+1, 0)

  grid[i][j] += max(grid[i-1][j-1], grid[i-1][j])
  return recurse(grid, i, j+1)


def parse_grid(fp):
  grid = list()
  with open(fp, 'r') as f:
    for row_str in f:
      row = [ int(n_str) for n_str in row_str.split(' ') ]
      grid.append(row)
  return grid


fp = './67.txt'
grid = parse_grid(fp)
print(grid)
print(recurse(grid, 1, 0))
'''
This challenge is based on the game Minesweeper.

Create a function that takes a grid of # and -,
where each hash (#) represents a mine and each dash 
(-) represents a mine-free spot. Return an array where 
each dash is replaced by a digit indicating the number 
of mines immediately adjacent to the spot 
(horizontally, vertically, and diagonally).

Examples

numGrid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]

numGrid([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]

numGrid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["1", "1", "2", "#", "#"],
  ["1", "#", "3", "3", "2"],
  ["2", "4", "#", "2", "0"],
  ["1", "#", "#", "2", "0"],
  ["1", "2", "2", "1", "0"],
]
Source: https://edabit.com/challenge/voZCqTGMSNjCrRhf9
https://gist.github.com/CoGrammarCodeReview/ad478fd583270fd162d3e7125d69f3c0

# Looping through index, value:
https://www.techiedelight.com/loop-through-list-with-index-python/

# Arrays
https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
https://medium.com/an-amygdala/how-to-iterate-through-a-2d-list-in-python-5a90693f3a15

# Create array
rows, cols = (5, 5)
  newArr=[]
  for i in range(rows):
      col = []
      for j in range(cols):
          col.append(0)
      newArr.append(col)

'''

class MineSweeper:
  def __init__(self, data):
    super().__init__()
    self.grid = data
    self.mines = []
    for i in range(len(data)):
      for j in range(len(data[i])):
        if data[i][j] == "-":
          data[i][j] = str(0)
        elif data[i][j] == "#":
          self.mines.append((i, j))

  def print_grid(self):
    for i in range(len(self.grid)):
      print(self.grid[i])

  def print_mines(self):
    print("-----------------------------")
    for i in range(len(self.mines)):
      print(self.mines[i])
    print("-----------------------------")

  def is_first_row(self, row, cell, row_length):
    pairs = []
    if cell == 0: # frist cell
      ## Update next, down diagonal right, down
      pairs = [(row, cell + 1), (row + 1, cell + 1), (row + 1, cell)]
      self.add_one(pairs)
    if cell == row_length: # last cell
      ## Update prev, down diagonal left, down
      pairs = [(row, cell - 1), (row + 1, cell - 1), (row + 1, cell)]
      self.add_one(pairs)
    if cell != 0 and cell < row_length: # middle
      ## Update prev, next, down, both diagonals down
      pairs = [(row, cell - 1), (row, cell + 1), (row + 1, cell), (row + 1, cell - 1), (row + 1, cell + 1)]
      self.add_one(pairs)
  
  def is_last_row(self, row, cell, row_length):
    pairs = []
    if cell == 0: # first cell
      ## Update next, diagonal up right, up
      pairs = [(row, cell + 1), (row - 1, cell + 1), (row - 1, cell)]
      self.add_one(pairs)
    if cell == row_length: # last cell
      ## Update prev, diagonal up left, up
      pairs = [(row, cell - 1), (row - 1, cell - 1), (row - 1, cell)]
      self.add_one(pairs)
    if cell != 0 and cell < row_length: # middle
      ## Update prev, next, up, both diagonals up
      pairs = [(row, cell - 1), (row, cell + 1), (row - 1, cell), (row - 1, cell - 1), (row - 1, cell + 1)]
      self.add_one(pairs)

  def is_middle_row(self, row, cell, row_length):
    pairs = []
    if cell == 0: # frist cell
      ## Update next, diagonal up and down right, up, down
      pairs = [(row, cell + 1), (row - 1, cell + 1), (row + 1, cell + 1), (row - 1, cell), (row + 1, cell)]
      self.add_one(pairs)
    if cell == row_length: # last cell
      ## Update prev, diagonal up and down left, up, down
      pairs  = [(row, cell - 1), (row - 1, cell - 1), (row + 1, cell - 1), (row - 1, cell), (row + 1, cell)]
      self.add_one(pairs)
    if cell != 0 and cell < row_length: # middle
      ## Update the whole star
      pairs = [(row, cell - 1), (row, cell + 1), (row - 1, cell), (row + 1, cell), (row - 1, cell - 1), (row + 1, cell - 1), (row - 1, cell + 1), (row + 1, cell + 1)]
      self.add_one(pairs)

  def add_one(self, pairs):
    ## Iterate through the pairs of coords
    for(r, c) in pairs:
      if self.grid[r][c] != "#":
        self.grid[r][c] = str(int(self.grid[r][c]) + 1)

  def resolve_grid(self):
    for (r, c) in self.mines:
      if r == 0: # first row
        self.is_first_row(r, c, len(self.grid[r]) - 1)
      if r == len(self.grid) - 1: # last row
        self.is_last_row(r, c, len(self.grid[r]) - 1)
      if r < len(self.grid) - 1 and r != 0: # middle
        self.is_middle_row(r, c, len(self.grid[r]) - 1)
    self.print_grid()

data = [
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]

grid = MineSweeper(data)
grid.print_grid()
grid.print_mines()
grid.resolve_grid()
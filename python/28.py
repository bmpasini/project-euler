from math import *
from pprint import pprint

class Solve(object):

  def __init__(self, n):
    self.n = n
    self.M = [ [ 0 for _ in range(self.n) ] for _ in range(self.n) ]
    self.size = 0
    self.val = 1
    self.i = self.n // 2
    self.j = self.n // 2
    self.set_val()
    self.go = True

  def set_val(self):
    self.M[self.j][self.i] = self.val

  def right(self):
    self.size += 1
    for _ in range(self.size):
      self.i += 1
      self.val += 1
      if self.keep_going():
        self.set_val()

  def down(self):
    for _ in range(self.size):
      self.j += 1
      self.val += 1
      self.set_val()

  def left(self):
    self.size += 1
    for _ in range(self.size):
      self.i -= 1
      self.val += 1
      self.set_val()

  def up(self):
    for _ in range(self.size):
      self.j -= 1
      self.val += 1
      self.set_val()

  def keep_going(self):
    if self.M[0][self.n-1] == 0:
      return True
    return False

  def around_square(self):
    self.right()
    if self.keep_going():
      self.down()
    if self.keep_going():
      self.left()
    if self.keep_going():
      self.up()
    # pprint(self.M)

  def populate_grid(self):
    while self.keep_going():
      self.around_square()

  def diagonal_sum(self):
    total = -1
    for k in range(self.n):
      total += self.M[k][k]
    for k in range(self.n):
      total += self.M[self.n-k-1][k]
    return total

  def solve(self):
    self.populate_grid()
    return self.diagonal_sum()


if __name__ == "__main__":
  n = 1001
  s = Solve(n)
  print(s.solve())


# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from math import factorial as fact

def S(n):
  N = n+1
  numbers = [ i for i in range(N) ]
  r = ''
  p = 1000000-1
  for i in range(1, N):
    j = p // fact(N-i)
    p %= fact(N-i)
    r += str(numbers.pop(j))
    if p == 0:
      break
  for n in numbers:
    r += str(n)
  return r

print(S(9))
from math import *

primes = set()
N = 0
x = None
primes.add(2)
primes.add(3)

def is_prime(n):
  if n < 2:
    return False
  if n in primes:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, ceil(sqrt(abs(n)))+1):
    if n % i == 0:
      return False
  primes.add(n)
  return True

def func(a, b, n):
  return n*n+a*n+b

def try_it(a, b):
  global N
  global x
  n = 0
  while is_prime(func(a, b, n)):
    n += 1
    if n > N:
      N = n
      x = a * b

for a in range(-999, 1000):
  for b in range(-1000, 1001):
    try_it(a, b)

print(x)
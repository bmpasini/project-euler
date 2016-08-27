# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def d(n):
  divisors = list()
  i = 1
  while i < n:
    if n % i == 0:
      divisors.append(i)
    i += 1
  # print(divisors)
  return sum(divisors)

def S(N):
  cache = [ 0 ]
  for i in range(1, N):
    cache.append(d(i))
  print(cache)
  result = 0
  for i in range(N):
    if cache[i] < N:
      if i == cache[cache[i]] and i != cache[i]:
        print(i, cache[i], cache[cache[i]])
        result += i
  return result
    
print(S(10001))
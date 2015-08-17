# (1)
# It can be shown that the polynomial n4 + 4n3 + 2n2 + 5n is a multiple of 6 for every integer n.
# It can also be shown that 6 is the largest integer satisfying this property.
# Define M(a, b, c) as the maximum m such that n4 + an3 + bn2 + cn is a multiple of m for all integers n. For example, M(4, 2, 5) = 6.
# (2)
# Also, define S(N) as the sum of M(a, b, c) for all 0 < a, b, c <= N.
# We can verify that S(10) = 1972 and S(10000) = 2024258331114.
# (3)
# Let Fk be the Fibonacci sequence:
# F0 = 0, F1 = 1 and
# Fk = Fk-1 + Fk-2 for k >= 2.
# Find the last 9 digits of sum S(Fk) for 2 <= k <= 1234567890123.

from datetime import datetime

# Start defining M(a,b,c)...
def M(a,b,c):
  return M3(a,b,c) * M8(a,b,c)

def M3(a,b,c):
  if Mm(a,b,c,3): return 3
  else: return 1

def M8(a,b,c):
  if Mm(a,b,c,8): return 8
  elif Mm(a,b,c,4): return 4
  elif Mm(a,b,c,2): return 2
  else: return 1

def Mm(a,b,c,m):
  for n in range(m):
    p = n*(n*(n*(n+a)+b)+c)
    if (p % m): return False
  return True

def S(N):
  S = Scube()
  k = N // 24
  r = N % 24
  return S['0'] * k**3 + \
        (S['a'][r] + S['b'][r] + S['c'][r]) * k**2 + \
        (S['ab'][r] + S['ac'][r] + S['bc'][r]) * k + \
         S['abc'][r]

def Scube():
  S = {               \
    '0'   : 0       , \
    'a'   : 24 * [0], \
    'b'   : 24 * [0], \
    'c'   : 24 * [0], \
    'ab'  : 24 * [0], \
    'ac'  : 24 * [0], \
    'bc'  : 24 * [0], \
    'abc' : 24 * [0]  \
  }
  for a in range(1,25):
    for b in range(1,25):
      for c in range(1,25):
        m = M(a,b,c)
        S['0'] += m
        for r in range(a,24): S['a'][r] += m
        for r in range(b,24): S['b'][r] += m
        for r in range(c,24): S['c'][r] += m
        for r in range(max((a,b)),24): S['ab'][r] += m
        for r in range(max((a,c)),24): S['ac'][r] += m
        for r in range(max((b,c)),24): S['bc'][r] += m
        for r in range(max((a,b,c)),24): S['abc'][r] += m
  return S

if __name__ == "__main__":
 start_time = datetime.now()
 print M(4, 2, 5)
 print S(10)
 print S(10000)
 c = datetime.now() - start_time
 print "It took", c


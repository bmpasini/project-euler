def fact(n):
  cache = [1,1] + [ False for i in range(n-1) ]
  def calc(x):
    if cache[x]:
      return cache[x]
    cache[x] = x * calc(x-1)
    return cache[x]
  return calc(n)

def S(n):
  s = fact(n)
  r = 0
  while s != 0:
    r += s % 10
    s //= 10
  return r

print(S(100))
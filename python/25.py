# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fib():
  a = b = 1
  i = 2
  while len(str(a)) < 1000:
    i += 1
    a, b = a + b, a
  return i

print(fib())
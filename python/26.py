def S(d):
  n = 0
  res = None
  for i in range(2, d+1):
    remainders = list()
    remainder = 10 % i
    while remainder not in remainders and remainder != 0:
      remainders.append(remainder)
      remainder = (10 * remainder) % i
    if remainder in remainders and len(remainders) > n:
      n = len(remainders)
      res = i
  return res

print(S(1000))
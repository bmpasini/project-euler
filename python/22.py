def get_score(fp):
  with open(fp, 'r') as f:
    for row_str in f:
      names = [ name.strip('"') for name in row_str.split(',') ]
  total = 0
  for i, name in enumerate(sorted(names)):
    values = [ ord(l) - 64 for l in list(name) ]
    total += (i + 1) * sum(values)
  return total


fp = './22.txt'
print(get_score(fp))
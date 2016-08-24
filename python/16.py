# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

def S(n):
  digits_list = [ 1 ]
  for _ in range(n):
    carry = False
    new_digits_list = list()
    list_len = len(digits_list)
    for i in reversed(range(list_len)):
      digit = digits_list[i]
      tmp = 2 * digit
      if carry:
        tmp += 1
      if tmp // 10 == 0:
        carry = False
        new_digit = tmp
        new_digits_list.insert(0, new_digit)
      else:
        new_digit = tmp % 10
        new_digits_list.insert(0, new_digit)
        if i != 0:
          carry = True
        else:
          new_digits_list.insert(0, 1)
    digits_list = list(new_digits_list)
  print(digits_list)
  result = sum(digits_list)
  return result


i = 1000
print('S(', i,'):', S(i))

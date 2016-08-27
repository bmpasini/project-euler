# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from math import floor

# Gaussian algorithm
def day_of_week(year, month, day):
  m = (month - 3) % 12 + 1
  if m > 10:
    year -= 1
  y = year % 100
  c = (year - (year % 100)) // 100
  w = (day + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
  return int(w)


def months_start_range(day, year_start, year_end):
  total = 0
  for year in range(year_start, year_end + 1):
    for month in range(1, 13):
      if day_of_week(year, month, 1) == day:
        total += 1
  return total
 
total = months_start_range(0, 1901, 2000)

print(total)

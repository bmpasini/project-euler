def in_words(number)
  hash = {
    0  => 'zero',
    1  => 'one',
    2  => 'two',
    3  => 'three',
    4  => 'four',
    5  => 'five',
    6  => 'six',
    7  => 'seven',
    8  => 'eight',
    9  => 'nine',
    10 => 'ten',
    11 => 'eleven',
    12 => 'twelve',
    13 => 'thirteen',
    14 => 'fourteen',
    15 => 'fifteen',
    16 => 'sixteen',
    17 => 'seventeen',
    18 => 'eighteen',
    19 => 'nineteen',
    20  => 'twenty',
    30  => 'thirty',
    40  => 'forty',
    50  => 'fifty',
    60  => 'sixty',
    70  => 'seventy',
    80  => 'eighty',
    90  => 'ninety'
  }

  array = number.to_s.split('').map { |n| n.to_i }

  if number < 1000
    if number <= 19
      return hash[number]
    elsif number < 100 and number % 10 == 0
      return hash[array[0] * 10]
    elsif number < 100
      return hash[array[0] * 10] + ' ' + hash[array[1]]
    elsif number % 100 == 0
      return hash[array[0]] + ' hundred'
    else
      return hash[array[0]] + ' hundred and ' + in_words(array[1] * 10 + array[2])
    end
  else
    result = ''
    int = number
    while int !=0
      if int >= 1_000_000_000
        fac1 = int / 1_000_000_000
        result += in_words(int/1_000_000_000) + ' billion '
        int -= fac1 * 1_000_000_000
      elsif int >= 1_000_000
        fac2 = int / 1_000_000
        result += in_words(int/1_000_000) + ' million '
        int -= fac2 * 1_000_000
      elsif int >= 1000
        fac3 = int / 1000
        result += in_words(int/1000) + ' thousand '
        int -= fac3 * 1000
      else
        result += in_words(int)
        int = 0
      end
    end
  end
result
end

# puts in_words(2_217_309_908)


def count_letters(n)
  cnt = 0
  n.times do |i|
    puts i+1
    puts in_words(i+1)
    cnt += in_words(i+1).gsub(/\s+/, "").split('').length
  end
  cnt
end

n = 1000
puts count_letters(n)

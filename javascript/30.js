// Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
// 1634 = 14 + 64 + 34 + 44
// 8208 = 84 + 24 + 04 + 84
// 9474 = 94 + 44 + 74 + 44
// As 1 = 14 is not a sum it is not included.
// The sum of these numbers is 1634 + 8208 + 9474 = 19316.
// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

function getDigits(n) {
  var digits = [];
  var i;
  while (n >= 1) {
    i = n % 10;
    digits.push(i);
    n = Math.floor(n / 10);
  }
  return digits.reverse();
}

function getNthPowerSum(digits, N) {
  var sum = 0;
  digits.forEach(function (digit) {
    sum += Math.pow(digit, N);
  });
  return sum;
}

function isMatch(n, N) {
  var digits = getDigits(n);
  var powerSum = getNthPowerSum(digits, N);
  return n === powerSum;
}

// this could be used for optimization
// combinations of NthPowers can generate the results faster
// function mapNthPowers(N) {
//   var powers = {};
//   for (var i = 1; i < 10; i++) {
//     powers[i] = Math.pow(i, N);
//   }
//   return powers;
// }

function NDigits(digit, N) {
  var NDigits = 0;
  for (var i = 0; i < N; i++) {
    NDigits += digit * Math.pow(10, i);
  }
  return NDigits;
}

// this may be wrong, but it is good enough in this case..
function findUpperLimit(N) {
  var greaterDigit = 9;
  return Math.max(NDigits(greaterDigit, N), N * Math.pow(9, N));
}

// brute force solution
function sumOfAllPowerSumMatches(N) {
  var sum = 0;
  var upperLimit = findUpperLimit(N);
  for (var n = 2; n < upperLimit; n++) {
    if (isMatch(n, N)) {
      console.log(n);
      sum += n;
    }
  }
  return sum;
}

var N = 4;
console.log('sumOfAllPowerSumMatches, N = 4', sumOfAllPowerSumMatches(N));

var N = 5;
console.log('sumOfAllPowerSumMatches, N = 5', sumOfAllPowerSumMatches(N));





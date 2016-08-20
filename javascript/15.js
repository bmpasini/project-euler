// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

var lattice = function (N) {
  var paths = 1;
  for (var i = 1; i <= N; i++) paths *= (N + i) / i;
  return paths;
}

for (var i = 1; i <= 20; i++) console.log(i, lattice(i));

// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

function fact(n) {
  var cache = [1,1];
  function calculate(x) {
    if (cache[x]) return cache[x];
    cache[x] = x * calculate(x-1);
    return cache[x];
  }
  return calculate(n);
}

var lattice = function (N) {
  return fact(2*N) / Math.pow(fact(N), 2);
}

// for (var i = 1; i <= 20; i++) console.log(i, lattice(i));

// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

var lattice = function (N) {

  var row = [0];
  for (var i=1; i<=N; i++) row.push(1);
  var cache = [row];
  for (var i=1; i<=N; i++) {
    row = [1];
    for (var j=1; j<=N; j++) row.push(0);
    cache.push(row);
  }

  for (var i=1; i<=N; i++) {
    for (var j=1; j<=N; j++) cache[i][j] = cache[i-1][j] + cache[i][j-1];
  }

  return cache[N][N];
}

// for (var i = 1; i <= 20; i++) console.log(i, lattice(i));

// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

var lattice = function (N) {

  var cache = [];

  for (var i=0; i<=N; i++) {
    var row = [];
    for (var j=0; j<=N; j++) row.push(0);
    cache.push(row);
  }

  function recurse(i, j) {
    if (i === 0 || j === 0) return 1;
    if (cache[i][j] !== 0) return cache[i][j];
    cache[i][j] = recurse(i-1, j) + recurse(i, j-1);
    return cache[i][j];
  }

  return recurse(N, N);
}

// for (var i = 1; i <= 20; i++) console.log(i, lattice(i));

// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

var lattice = function (N) {

  var paths = 0;

  function findPaths(n, i, j) {
    if      (i == n && j == n) return paths + 1;
    else if (i <  n && j == n) return findPaths(n, i + 1, j);
    else if (i == n && j <  n) return findPaths(n, i, j + 1);
    else                       return findPaths(n, i + 1, j) + findPaths(n, i, j + 1);
  }

  return findPaths(n, 0, 0, 0);
}

// for (var i = 1; i <= 20; i++) console.log(i, lattice(i));
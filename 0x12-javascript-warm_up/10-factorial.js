#!/usr/bin/node
function factorial (n) {
  if (!n || n < 2) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));

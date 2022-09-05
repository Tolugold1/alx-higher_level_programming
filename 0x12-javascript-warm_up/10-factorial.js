#!/usr/bin/node
function factorial (n) {
  if (!n || n < 2) {
    return 1;
   }
   return console.log(n * factorial(n - 1));
}

factorial(Number(process.argv[2]));

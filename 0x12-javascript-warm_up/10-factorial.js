#!/usr/bin/node
function factorial (n) {
   if (isNaN(n) || n < 2) {
      return (1);
   } else {
      return (console.log(n * factorial(n - 1)))
   }
}

factorial(Number(process.argv[2]));

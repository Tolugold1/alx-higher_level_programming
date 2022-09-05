#!/usr/bin/node
<<<<<<< HEAD
console.log(process.argv[2] + ' is ' + process.argv[3]);
=======
if (process.argv[3] && process.argv[2]) {
   let arr = [process.argv[2], process.argv[3]];
   console.log(arr.join(' is '));
}
>>>>>>> 152031404026703f1880fcee94c4f2c8a94ab345

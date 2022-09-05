#!/usr/bin/node
if (process.argv[3] && process.argv[2]) {
   let arr = [process.argv[2], process.argv[3]];
   console.log(arr.join(' is '));
}

#!/usr/bin/node
function add(a, b) {
  return (console.log(a + b));
}

add(Number(process.argv[2]), Number(process.argv[3]));

#!/usr/bin/node
let arg = process.argv;
if (arg.length < 4) {
  console.log(0);
} else {
  let max, second_max;
  if (Number(arg[2]) > Number(arg[3])) {
    max = Number(arg[2]);
    second_max = Number(arg[3]);
  } else {
    max = Number(arg[3]);
    second_max = Number(arg[2]);
  }

  for (i = 4; i < arg.length; i++) {
    if (Number(arg[i]) > max) {
      second_max = max;
      max = Number(arg[i]);
    } else if (Number(arg[i]) > second_max) {
      second_max = Number(arg[i]);
    }
  }
  console.log(second_max);
}

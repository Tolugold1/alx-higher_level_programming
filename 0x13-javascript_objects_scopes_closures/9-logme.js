#!/usr/bin/node
let calls = 0;
exports.logMe = function (item) {
  console.log(calls + ': ' + item);
  calls++;
};

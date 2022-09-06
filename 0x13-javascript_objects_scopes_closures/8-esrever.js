#!/usr/bin/node
exports.esrever = function (list) {
  const reverse = [];
  for (const item of list) {
    reverse.unshift(item);
  }
  return reverse;
};

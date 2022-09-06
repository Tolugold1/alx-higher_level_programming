#!/usr/bin/node
const square = require("./5-square");

class Square extends square {
   charPrint (c) {
      if (!c) {
         c = 'X';
      } else {
         for (let i = 0; i < this.size; i++) {
            console.log(c.repeat(this.size));
         }
      }
   }
}

module.exports = Square;

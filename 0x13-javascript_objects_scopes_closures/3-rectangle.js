#!/usr/bin/node
class Rectangle {
   constructor(w, h) {
      if (Number(w) > 0 && Number(h) > 0) {
         this.width = w;
         this.height = h;
      }
   }

   print() {
      for (let i = 0; i < h; i++) {
         console.log('X'.repeat(w));
      }
   }
}

module.exports = Rectangle;

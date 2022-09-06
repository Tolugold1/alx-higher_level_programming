#!/usr/bin/node
class Rectangle {
   constructor (w, h) {
     if (Number(w) > 0 && Number(h) > 0) {
       this.width = w;
       this.height = h;
     }
   }
 
   double () {
      this.width = w * 2;
      this.height = h * 2;
   }

   rotate () {
      this.width = h;
      this.width = w;
   }
   
   print () {
     for (let i = 0; i < this.height; i++) {
       console.log('X'.repeat(this.width));
     }
   }
 }
 
 module.exports = Rectangle;

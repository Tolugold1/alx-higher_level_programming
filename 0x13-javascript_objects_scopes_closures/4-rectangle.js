#!/usr/bin/node
class Rectangle {
   constructor (w, h) {
     if (Number(w) > 0 && Number(h) > 0) {
       this.width = w;
       this.height = h;
     }
   }
 
   double () {
      this.width = this.width * 2;
      this.height = this.height * 2;
   }

   rotate () {
      this.width = this.height;
      this.height = this.width;
   }
   
   print () {
     for (let i = 0; i < this.height; i++) {
       console.log('X'.repeat(this.width));
     }
   }
 }
 
 module.exports = Rectangle;

#!/usr/bin/node
if (isNaN(process.argv[2])) {
   console.log('Missing number of occurrences')
} else {
   const x = Number(process.argv[2]);
   for (let i = 0; i < x.length; i++) {
      console.log('C is fun');
   }
}

#!/usr/bin/node
if (isNaN(process.argv[2])) {
   console.log('Missing number of occurrences')
} else {
   for (let i = 0; i < Number(process.argv[2]).length; i++) {
      console.log('C is fun');
   }
}

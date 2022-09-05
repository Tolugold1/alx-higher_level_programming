#!/usr/bin/node
if (isNaN(process.argv[2])) {
   console.log('Missing number of occurrences')
} else {
<<<<<<< HEAD
   const x = Number(process.argv[2]);
   for (let i = 0; i < x.length; i++) {
=======
   for (let i = 0; i < Number(process.argv[2]).length; i++) {
>>>>>>> 42ee0dfac104f2ca1b6bc66728b55d6d47d562c2
      console.log('C is fun');
   }
}

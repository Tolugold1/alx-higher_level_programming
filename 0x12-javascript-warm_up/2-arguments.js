#!/usr/bin/node
if (process.arg[3]) {
   console.log("Argument found");
} else if (process.arg[2]) {
   console.log("Argument found");
} else {
   console.log("No argument");
}

#!/usr/bin/node
const fs = require('fs');

if (process.argv[2]) {
    fs.readFile(process.argv[2], 'utf-8', (err, data) => {
        if (err) {
            console.log(err);
        } else {
            process.stdout.write(data);
        }
    });
};

#!/usr/bin/node
const fs = require('fs')

if (process.argv[2] && process.argv[3]) {
    fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err, data) => {
        if (err) {
        return err
        }
    })
}

#!/usr/bin/node
const request = require('request')

request
.get(process.argv[2])
.on('response', 'err', (err, response) => {
    if (err) {
        throw err;
    }
    process.stdout.write('code: ' + response.statusCode)
})

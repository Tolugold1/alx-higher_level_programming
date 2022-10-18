#!/usr/bin/node
const request = require('request')

request
.get(process.argv[2])
.on('response', (response) => {
    process.stdout.write('code: ' + response.statusCode)
})

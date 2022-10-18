#!/usr/bin/node
const request = require('request')

request(process.argv[2] + '/18', (error, response, body) => {
    if (error) {
        throw error
    }
    process.stdout.write(JSON.parse(body).title)
})

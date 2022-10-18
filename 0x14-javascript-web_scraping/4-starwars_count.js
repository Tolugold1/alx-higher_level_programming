#!/usr/bin/node
const request = require('request')

const id = 18
request(process.argv[2] + '/' + id, (error, response, body) => {
    if (error) {
        throw error
    }
    process.stdout.write(JSON.parse(body).title)
})

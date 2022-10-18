#!/usr/bin/node
const request = require('request')

const id = process.argv[2]
request('https://swapi-api.hbtn.io/api/films/' + id, (error, response, body) => {
    if (error) {
        throw error
    }
    process.stdout.write(JSON.parse(body).title)
})

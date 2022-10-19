#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
    if (error) {
        throw error;
    } else {
        fs.wirteFile(filePath, body, "utf8", (err, data) => {
            if (err) {
                throw err;
            }
        });
    }
});

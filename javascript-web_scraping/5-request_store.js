#!/usr/bin/node
const request = require('request');
const pathOfFile = process.argv[3];
const url = process.argv[2];
const fs = require('fs');

request(url, 'utf8', (err, response, body) => {
  if (err) throw err;
  fs.writeFile(pathOfFile, response.body, (err) => {
    if (err) throw err;
  });
});

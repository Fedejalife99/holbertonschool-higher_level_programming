#!/usr/bin/node

const request = require('request');
const api = process.argv[2];
let cnt = 0;
request(api, function (err, response, body) {
  if (err) throw err;
  const data = JSON.parse(body);
  const movies = data.results;
  for (const film of movies) {
    if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      cnt += 1;
    }
  }
  console.log(cnt);
});

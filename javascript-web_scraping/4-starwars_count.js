#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/', function (err, response, body) {
  if (err) throw err;
  const movies = JSON.parse(body);
  const characters = movies.characters;
  console.log(characters);
});

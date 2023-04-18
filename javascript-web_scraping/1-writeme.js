#!/usr/bin/node
const fs = require('fs');
const pathOfFile = process.argv[2];
const text = process.argv[3];

fs.writeFile(pathOfFile, text, (err) => {
  if (err) throw err;
});

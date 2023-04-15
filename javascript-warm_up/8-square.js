#!/usr/bin/node
const size = process.argv[2];
const simbol = 'x';
if (isNaN(size) === true) {
  console.log('Missing size');
}
let row = '';
for (let i = 0; i < size; i++) {
  row += simbol;
}

for (let i = 0; i < size; i++) {
  console.log(row);
}

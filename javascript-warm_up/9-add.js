#!/usr/bin/node

function add(a, b) {
    console.log(parseInt(a) + parseInt(b));
}

const b = process.argv[3];
const a = process.argv[2];

add(a, b);

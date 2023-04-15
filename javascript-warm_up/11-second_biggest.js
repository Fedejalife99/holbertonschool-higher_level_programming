#!/usr/bin/node

const arrayOfArgs = process.argv.slice(2).map(Number);
arrayOfArgs.sort((a, b) => (a - b));
console.log(arrayOfArgs[arrayOfArgs.length - 2]);

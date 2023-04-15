#!/usr/bin/node

const arrayOfArgs = process.argv.slice(2).map(Number);
arrayOfArgs.sort((a, b) => (a - b));
if (arrayOfArgs.length === 1) {
    console.log(arrayOfArgs[0] - 1);
}
else if (arrayOfArgs.length === 0) {
    console.log(0);
}
else {
    console.log(arrayOfArgs[arrayOfArgs.length - 2]);
}

#!/usr/bin/node
for (let i = 2; process.argv[i]; i++) {
    if (process.argv[i] && process.argv[i + 1]) {
        console.log('Arguments found');
        return;
    }
    if (process.argv[i] && !process.argv[i + 1]) {
        console.log('Argument found');
        return;
    }
    else {
        console.log('No argument');
    }
}
console.log('No argument')



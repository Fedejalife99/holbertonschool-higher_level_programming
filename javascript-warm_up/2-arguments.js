#!/usr/bin/node
for (let i = 2; process.argv[i]; i++) {
    if (process.argv[i]) {
        console.log('Argument found');
        return;
    }
    else {
        console.log('No argument')
    }
}
console.log('No argument')



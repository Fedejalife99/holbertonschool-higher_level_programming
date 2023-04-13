#!/usr/bin/node
for (let i = 2; process.argv[i]; i++) {
    if (process.argv[i]) {
        console.log(process.argv[i]);
    }
    else {
        console.log('No argument')
    }
}
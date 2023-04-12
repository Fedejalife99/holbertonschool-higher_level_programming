#!/usr/bin/node

for (let i = 1; process.argv[i]; i++) {
    if (process.argv[i]) {
        console.log('Argument found');
    }
}

if (!process.argv) {
    console.log('No argument')
}

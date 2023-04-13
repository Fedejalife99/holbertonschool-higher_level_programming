#!/usr/bin/node
for (let i = 2; process.argv[i]; i++) {
    if (process.argv[i]) {
        console.log(process.argv[i]);
        if (!process.argv[i + 1]) {
            return
        }
    }
    else {
        console.log('No argument');
        return;
    }
}
console.log('No arguments');

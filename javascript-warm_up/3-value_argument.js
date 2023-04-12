#!/usr/bin/node
if (process.argv) {
    for (let i = 1; process.argv[i]; i++) {
        console.log(process.argv[i]);
    }
}
else {
    console.log('No argument');
}
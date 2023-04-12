#!/usr/bin/node

if (process.argv.length > 1) {
    for (let i = 2; i < process.argv.length; i++) {
        console.log('Argument found');
    }
} else {
    console.log('No argument');
}
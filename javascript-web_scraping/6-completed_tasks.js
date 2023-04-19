#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cnt = 0;
const ids = [];
const completedTasks = {};

request(url, (err, response, body) => {
    if (err) throw err;
    const res = JSON.parse(body);
    // obtener ids únicos
    for (const element of res) {
        if (!ids.includes(element.userId)) {
            ids.push(element.userId);
        }
    }
    for (const id of ids) {
        cnt = 0;
        for (const element of res) {
            if (element.userId === id && element.completed === true) {
                cnt++;
            }
        }
        completedTasks[id] = cnt;
    }
    console.log(completedTasks);
});

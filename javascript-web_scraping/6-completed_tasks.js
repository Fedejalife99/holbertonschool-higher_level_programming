const request = require('request');
const url = process.argv[2];
let cnt = 0;
const ids = [];
const completed_tasks = {};

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
        completed_tasks[id] = cnt;
    }
    console.log(completed_tasks);
});

#!/usr/bin/node
exports.esrever = function (list) {
    let reverse = list.slice();
    for (let i = 0, j = list.length - 1; i < j; i++, j--) {
        let aux = reverse[i];
        reverse[i] = reverse[j];
        reverse[j] = aux;
    }
    return reverse;
};


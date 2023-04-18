#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
    constructor(size) {
        super(size, size);
        this.size = size;

    }
    charPrint(c) {
        const simbol_obj = {
            simbol: c
        };
        if (c === undefined) {
            simbol_obj.simbol = 'X'
        }
        let row = '';
        for (let i = 0; i < this.size; i++) {
            row += simbol_obj.simbol;
        }

        for (let i = 0; i < this.height; i++) {
            console.log(row);
        }
    }
};
module.exports = Square;

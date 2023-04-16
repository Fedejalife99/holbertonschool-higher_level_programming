class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
            this.width = w;
            this.height = h;
        }
        else {
            Object.assign(this, {});
        }
    }


    print() {
        const simbol = 'X';
        let row = '';
        for (let i = 0; i < this.width; i++) {
            row += simbol;
        }

        for (let i = 0; i < this.height; i++) {
            console.log(row);
        }
    }
};

module.exports = Rectangle;

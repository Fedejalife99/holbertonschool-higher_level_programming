#!/usr/bin/node
var header = document.querySelector('#toggle_header');
header.style.color = 'black'
header.addEventListener('click', function() {
    if (header.style.color == '#00FF00') {
        header.style.color = 'red';
    }
    else if(header.style.color === 'red') {
        header.style.color = '#00FF00';
    }
    else{
        header.style.color = 'red'
    }
});
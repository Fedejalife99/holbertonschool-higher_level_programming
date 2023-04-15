#!/usr/bin/node
if (isNaN(process.argv[2]) == true)
  return;
if (Math.sign(process.argv[2]) == -1)
  return;
const number = process.argv[2]
  for(let i = 0; i < number; i++){
    console.log('C is fun')
  }
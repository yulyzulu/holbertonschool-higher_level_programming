#!/usr/bin/node

let x = 'X';
let num = parseInt(process.argv[2]);
let i;
let j;

if (num) {
  for (i = 0; i < num; i++) {
    console.log(x.repeat(num));
  }
  } else {
  console.log('Missing size');
}

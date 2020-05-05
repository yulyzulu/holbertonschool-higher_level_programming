#!/usr/bin/node

const x = 'X';
const num = parseInt(process.argv[2]);
let i;

if (num) {
  for (i = 0; i < num; i++) {
    console.log(x.repeat(num));
  }
} else {
  console.log('Missing size');
}

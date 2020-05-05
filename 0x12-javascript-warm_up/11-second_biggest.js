#!/usr/bin/node

const len = process.argv.length;
const numbers = [];
let i;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (i = 2; i < len; i++) {
    numbers.push(process.argv[i]);
  }
  numbers.sort(function (a, b) { return a - b; });
  console.log(numbers);
  console.log(len);
  console.log(numbers[len - 4]);
}

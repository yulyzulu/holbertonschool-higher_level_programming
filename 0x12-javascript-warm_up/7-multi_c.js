#!/usr/bin/node

let x;
const msg = 'C is fun';

if (process.argv[2]) {
  for (x = 0; x < process.argv[2]; x++) {
    console.log(msg);
  }
} else {
  console.log('Missing number of occurrences');
}

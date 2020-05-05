#!/usr/bin/node

function factorial(num) {
  if (num < 0) {
    return -1;
  } else if (num == 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

let fact = factorial(process.argv[2]);
console.log(fact);

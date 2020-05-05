#!/usr/bin/node


function factorial(nu) {
  if (nu === NaN) {
    return 1;
  } else if (nu === 0) {
    return 1;
  } else {
    return (nu * factorial(nu - 1));
  }
}

n = process.argv[2];
let fact = factorial(n);
console.log(fact);

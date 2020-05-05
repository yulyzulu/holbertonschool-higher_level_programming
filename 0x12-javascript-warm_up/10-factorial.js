#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (num) {
  const fact = factorial(num);
  console.log(fact);
} else {
  console.log(1);
}

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

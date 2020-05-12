#!/usr/bin/node

const file = process.argv[2];

const fs = require('fs');

try {
  const data = fs.readFileSync(file, 'utf-8');
  process.stdout.write(data);
} catch (e) {
  console.log(e);
}

#!/usr/bin/node

const file = process.argv[2];
const content = process.argv[3];

const fs = require('fs');

try {
  fs.writeFileSync(file, content, 'utf-8');
} catch (e) {
  console.log(e);
}

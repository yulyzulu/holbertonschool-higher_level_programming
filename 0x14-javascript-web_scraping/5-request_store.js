#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const file = process.argv[3];
const fs = require('fs');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFileSync(file, body, 'utf-8');
});

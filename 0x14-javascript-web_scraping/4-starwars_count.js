#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const str = JSON.parse(body);
  const result = str.results;
  let count = 0;
  for (const i in result) {
    const character = result[i].characters;
    for (const j in character) {
      const num = character[j].slice(-3, -1);
      if (num === '18') {
        count = count + 1;
      }
    }
  }
  console.log(count);
});

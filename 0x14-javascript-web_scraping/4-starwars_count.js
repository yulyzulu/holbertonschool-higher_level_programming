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
      if (character[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});

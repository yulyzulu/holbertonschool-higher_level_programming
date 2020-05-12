#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const str = JSON.parse(body);
  console.log(str.title);
});

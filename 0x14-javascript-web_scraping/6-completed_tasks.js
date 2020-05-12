#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const str = JSON.parse(body);
  const len = str.length;
  let count = 0;
  for (i = 0; i < len; i++) {
    if (i.userId == //buscar cómo sumar para cada id)
    if (str.complete === true) {
      
    }
  }
  console.log(len);
  //console.log(str.completed);
});

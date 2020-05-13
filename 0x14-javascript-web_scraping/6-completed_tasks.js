#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dic = {};
  data.forEach(obj => {
    if (obj.completed) {
      if (!dic[obj.userId]) {
        dic[obj.userId] = 1;
      } else {
        dic[obj.userId] += 1;
      }
    }
  });
  console.log(dic);
});

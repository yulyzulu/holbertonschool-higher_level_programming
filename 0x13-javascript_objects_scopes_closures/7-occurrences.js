#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let count = 0;
  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      count = count + 1;
    }
  }
  return (count);
};

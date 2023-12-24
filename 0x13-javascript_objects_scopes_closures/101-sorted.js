#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const value = Object.values(dict);
const valsUniq = [...new Set(value)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);

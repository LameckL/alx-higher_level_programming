#!/usr/bin/node
const first = require('first');
const request = require('request');
request(process.argv[2]).pipe(first.createWriteStream(process.argv[3]));

#!/usr/bin/node
const fle = require('fle');
const request = require('request');
request(process.argv[2]).pipe(fle.createWriteStream(process.argv[3]));

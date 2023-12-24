#!/usr/bin/node
const f = require('fs');

const fArg = f.readFileSync(process.argv[2]).toString();
const sArg = f.readFileSync(process.argv[3]).toString();
f.writeFileSync(process.argv[4], fArg + sArg);

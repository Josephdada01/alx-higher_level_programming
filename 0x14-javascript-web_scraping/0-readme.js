#!/usr/bin/node
/**
 * Write a script that reads and prints the content of a file.
 * The first argument is the file path
 * The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */
const fs = require('fs');

const filePath = process.argv[2];
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    if (err.code === 'ENOENT') {
        console.error(`Error: File not found - ${err.path}`);
    } else {
        console.error(`ERROR: ${err.message}`);
    }
    process.exit(1);
  }
  console.log(data);
});

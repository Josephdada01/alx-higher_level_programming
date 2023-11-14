#!/usr/bin/node
/**
 * Write a script that prints a square
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer,
 * print “Missing size”
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.)
 */
/* const args = process.argv.slice(2);
const squareSize = parseInt(args[0]);
let i = 0;
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (i = 0; i < squareSize; i++) {
    console.log('x'.repeat(squareSize));
  }
} */
const size = process.argv[2];

// Check if the size can be converted to an integer
const sizeInt = parseInt(size);

if (!isNaN(sizeInt)) {
/* Size is a valid integer */
  for (let i = 0; i < sizeInt; i++) {
    let row = '';
    for (let j = 0; j < sizeInt; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  /* Size cannot be converted to an integer */
  console.log('Missing size');
}

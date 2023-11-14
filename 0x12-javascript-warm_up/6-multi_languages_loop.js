#!/usr/bin/node
/**
 * Write a script that prints 3 lines: (like 1-multi_languages.js)
 * but by using an array of string and a loop
 * The first line: “C is fun”
 * The second line: “Python is cool”
 * The third line: “JavaScript is amazing”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You are not allowed to use any if/else statement
 * You can use only one console.log
 * You must use a loop (while, for, etc.)
 */
/* let i = 0;
while (i <= 3) {
  switch (i) {
    case 1:
      console.log('C is fun');
      break;
    case 2:
      console.log('Python is cool');
      break;
    case 3:
      console.log('JavaScript is amazing');
      break;
  }
  i++;
} */
const listing = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let i = 0;
for (i = 0; i < listing.length; i++) {
  console.log(listing[i]);
}

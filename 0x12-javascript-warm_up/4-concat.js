#!/usr/bin/node
/**
 * Write a script that prints two arguments passed to it,
 * in the following format: “ is ”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
const arg1 = process.argv[2];
const arg2 = process.argv[3];

/* Check if both arguments are provided */
if (arg1 !== undefined && arg2 !== undefined) {
/* Print the arguments in the specified format */
  console.log(`${arg1} is ${arg2}`);
} else if (arg1 === undefined) {
  console.log(`undefined is ${arg2}`);
} else if (arg2 === undefined) {
  console.log(`${arg1} is undefined`);
} else {
  console.log('undefined is undefined');
}

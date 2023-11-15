#!/usr/bin/node
/**
 * Write a script that searches the second biggest
 * integer in the list of arguments.
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
let num = process.argv.splice(2);

if (num.length < 2) {
  console.log(0);
} else {
  num = num.sort(nsort).reverse();
  console.log(num[1]);
}

function nsort (num1, num2) {
  return (num1 - num2);
}

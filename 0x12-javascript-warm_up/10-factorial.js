#!/usr/bin/node
/**
 * Write a script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used
 * for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return 1;
  }
  return num * factorial(num - 1);
}
/* converting the first typein num to int */
const typeinNum = parseInt(process.argv[2]);
console.log(factorial(typeinNum));

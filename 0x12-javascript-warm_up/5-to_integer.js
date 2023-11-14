#!/usr/bin/node
/**
 * Write a script that prints My number:
 * <first argument converted in integer> if the first argument
 * can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You are not allowed to use try/catch
 */
const firstArgs = process.argv[2];
/* Convert the first argument to an integer using parseInt */
const intFirstArgs = parseInt(firstArgs, 10);

if (!isNaN(intFirstArgs)) {
  console.log(`My number: ${firstArgs}`);
} else {
  console.log('Not a number');
}

#!/usr/bin/node
/**
 * Write a class Square that defines a square and
 * inherits from Square of 5-square.js:
 * You must use the class notation for defining your class and extends
 * Create an instance method called charPrint(c) that prints the
 * rectangle using the character c
 * If c is undefined, use the character X
 */
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  constructor (size) {
    /* calling the constructor of the Rectangle class */
    super(size, size);
  }

  charPrint (c) {
    let j = 0;
    for (j = 0; j < this.height; j++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log('c'.repeat(this.width));
      }
    }
  }
};

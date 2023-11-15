#!/usr/bin/node
/**
 * Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 * The constructor must take 2 arguments: w and h
 * Initialize the instance attribute width with the value of w
 * Initialize the instance attribute height with the value of h
 * If w or h is equal to 0 or not a positive integer, create an empty object
 * Create an instance method called print() that prints the
 * rectangle using the character X
 * Create an instance method called rotate() that exchanges the width
 * and the height of the rectangle
 * Create an instance method called double() that multiples the width
 * and the height of the rectangle by 2
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || w < 1 || h === undefined || h < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let j = 0;
    for (j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }

  double () {
    this.width *= this.width;
    this.height *= this.height;
  }
};

#!/usr/bin/node
/**
 * Write a function that returns the number of occurrences in a list:
 * Prototype: exports.nbOccurences = function (list, searchElement)
 */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce(function (count, element) {
    return count + (element === searchElement ? 1 : 0);
  }, 0);
};

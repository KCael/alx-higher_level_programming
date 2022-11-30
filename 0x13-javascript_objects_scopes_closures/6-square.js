#!/usr/bin/node
const SquareParent = require('./5-square');

/**
 * Defines a Square
 */
class Square extends SquareParent {
  /**
   * Prints this Square using the character c, otherwise 'X'.
   * @param {String} c The character to print this Square with.
   */
  charPrint (c) {
    const pen = c === undefined ? 'X' : c;
    const row = new Array(this.width).fill(pen, 0, this.width);
    const rows = new Array(this.height).fill(row.join(''), 0, this.height);
    console.log(rows.join('\n'));
  }
}

module.exports = Square;

#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * Represents a Square
 */
class Square extends Rectangle {
  /**
   * Creates a Square with the given dimensions.
   * @param size The value of the width and height.
   */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

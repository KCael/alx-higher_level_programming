#!/usr/bin/node
/**
* Defines a rectangle
*/
class Rectangle {
  /**
   * Creates a rectangle with the given dimensions.
   * @param w The value of the width.
   * @param h The value of the height.
   */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

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
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

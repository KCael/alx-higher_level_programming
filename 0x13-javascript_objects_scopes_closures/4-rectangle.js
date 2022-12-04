#!/usr/bin/node
/**
 * Defines a Rectangle
 */
class Rectangle {
  /**
   * Creates a Rectangle with the given dimensions.
   * @param w The value of the width.
   * @param h The value of the height.
   */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Prints this Rectangle using the character 'X'.
   */
  print () {
    const row = new Array(this.width).fill('X', 0, this.width);
    const rows = new Array(this.height).fill(row.join(''), 0, this.height);
    console.log(rows.join('\n'));
  }

  /**
   * Exchanges the width and height of this Rectangle.
   */
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  /**
   * Multiplies the dimensions of this Rectangle.
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

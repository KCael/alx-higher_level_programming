#!/bin/bash
# takes in a URL, sends a POST resquest, displays response's body
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"

#!/bin/bash
# Gets size of body of a response from a URL
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2

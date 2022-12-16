#!/bin/bash
# Takes in a URL, sends a GET request to the URL, displays response body
curl -s "$1" -X GET -H "X-School-User-Id: 98"

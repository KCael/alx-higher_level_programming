#!/bin/bash
# Sends a rrequest to a URL and displays status code of the response
curl -s -w "%{response_code}" -o /dev/null "$1"

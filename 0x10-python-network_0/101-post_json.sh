#!/bin/bash
# Sends a JSON POST request to a URL passed
curl -sL -X POST -H 'Content-Type: application/json' -d "$([ -f "$2" ] && cat "$2")" "$1"

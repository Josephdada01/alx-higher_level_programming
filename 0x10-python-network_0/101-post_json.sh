#!/bin/bash
#Your script must send a POST request with the contents of a file, passed
curl -s POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"

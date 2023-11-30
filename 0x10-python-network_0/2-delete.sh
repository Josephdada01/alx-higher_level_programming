#!/bin/bash
#Bash script that sends a DELETE request to the URL passed as the 1st args
curl -s -X DELETE "$1"

#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response
#The size must be displayed in bytes
#You have to use curl

url=$1
curl -sI "$url" | awk '/Content-Lenght/ {print $2; exit}'


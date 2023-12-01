#!/bin/bash
#request to 0.0.0.0:5000/catch_me that makes the server to respond with a messg
curl -sL -X PUT -H "Origin: School" -d "X-School-User-Id=98" 0.0.0.0:5000/catch_me

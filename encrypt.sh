#!/bin/bash

server=$1

hash=$(curl -c 'cookie.txt' -s $server | head -n 6 | tail -n1 | cut -d '>' -f4 | cut -d '<' -f1 | tr -d '\n' | md5sum | cut -d ' ' -f1)

curl -s -X POST -b 'cookie.txt' -H 'Content-Type: application/x-www-form-urlencoded' --data "hash=$hash" $server

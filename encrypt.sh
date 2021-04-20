#!/bin/bash

server=$1

hash=$(curl -s ${server} | head -n 6 | tail -n1 | cut -d '>' -f4 | cut -d '<' -f1 | md5sum | cut -d ' ' -f1)

curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' --data "hash=$hash" $server


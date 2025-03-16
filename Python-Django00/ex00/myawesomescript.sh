#!/bin/bash

# Check if only one parameter is passed by argument

if [ "$#" -ne 1 ]; then
	echo "Error: Please provide exactly one parameter."
	exit 1
fi

# Store bit.ly link for decrypt

bitly_link="$1"

# Get curl output from bitly_link and parse the link

curl_output=$(curl -s "$bitly_link" | grep -o 'href="[^"]*"' | cut -d'"' -f2 | cut -f1-3)

# Print the decrypted and parsed link in terminal

echo "$curl_output"

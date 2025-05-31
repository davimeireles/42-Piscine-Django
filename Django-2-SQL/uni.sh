#!/bin/bash

find * -type d -name 'migrations'  -exec rm -rfv {} \;
find * -type d -name '__pycache__' -exec rm -rfv {} \;
find * -type f -name '*.sqlite3'   -exec rm -rfv {} \;

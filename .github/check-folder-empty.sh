#!/bin/bash

set -e

if [ -z "$(ls -A ./annotations/)" ]; then
   echo ":set-output name=empty::true"
else
   echo ":set-output name=empty::false"
fi

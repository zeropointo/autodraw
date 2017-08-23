#!/bin/bash

# Author Robert Bennett

for file in $@
do
  array=$(grep "\bd=" $file | sed -r "s/(-)?[0-9]+(\.)?(-)?([0-9]*)?,(-)?[0-9]+(\.)?(-)?([0-9]*)?/{ & },\n/g" | grep -o "{.*},")
  echo "$array"
done

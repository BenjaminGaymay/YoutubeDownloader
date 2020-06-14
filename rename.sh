#!/bin/bash

directory="./Musiques"

for file in $directory/*; do
  cleared=$(awk '{gsub(/-[a-zA-Z0-9_]+\.mp3$/, ".mp3");}1' <<< "$file")
  echo "move $file to $cleared"
  mv "$file" "$cleared"
done


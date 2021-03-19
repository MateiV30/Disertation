#!/bin/bash

if [ "$2" = "" ]; then
  echo Missing output name
fi

echo First should be source second should be output

gcc $1 -o $2 -lGL -lGLU -lglut -lm

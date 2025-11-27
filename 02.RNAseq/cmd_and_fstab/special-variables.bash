#!/bin/bash

echo $#
echo $*
echo $@
if [ -e $1 ]
then 
    echo "this file exist"
else
    echo "No such file"
fi

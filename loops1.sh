#!/bin/bash
arg1=$1

if [[ -z $1 ]]; then 
    echo "no param"
    exit 1
fi

length=${#arg1}
res=""

while [[ $length -gt 0 ]]; do
    ((length-=1))
    res+="${arg1:length:1}"
done
echo "$res"| tr 'A-Za-z' 'a-zA-Z'






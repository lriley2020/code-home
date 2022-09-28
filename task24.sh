#!/usr/local/bin/bash

### There isn't really a way to parse json in bash without extra packages, so just read line by line instead ###
readarray NUMBERS < numbers.db

### Options as an array ###
declare -a OPTIONS=("Smallest number" "Largest number" "Average" "Quit")

### Find min and max numbers from array, along with sum ###
MIN=0 MAX=0 SUM=0
for i in "${NUMBERS[@]}"
do
    (( $i > MAX || MAX == 0)) && MAX=$i
    (( $i < MIN || MIN == 0)) && MIN=$i
    SUM=$((SUM + i))
done

### Forever loop to ask for option and calculate it ###
while :
do
  ### Output numbered options and ask for input ###
  for i in "${!OPTIONS[@]}"
  do
    echo $((i + 1)). "${OPTIONS[i]}"
  done
  read -rp "option> " OPTION

  ### Check different options ###
  case $OPTION in
    1)
      echo $MIN ;;
    2)
      echo $MAX ;;
    3)
      echo $((SUM / ${#NUMBERS[@]})) ;;
    4)
      break ;;
  esac
done

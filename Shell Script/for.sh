#!/usr/bin/env bash

for ((i = 1; i <= 10; i++)); do
  echo "$i"
done

echo "---> For Alternativo"

for i in $(seq 10); do
  echo $i
done

echo "---> For Alternativo - 2"

#Array
FRUTAS=(
  'Laranja'
  'Ameixa'
  'Abacaxi'
  'Uva'
  )

for i in "${FRUTAS[@]}"; do
  echo $i
done


echo "---> While"

contador=0

while [[ $contador -lt ${#FRUTAS[@]} ]]; do 
  echo $contador
  contador=$(($contador+1))
done

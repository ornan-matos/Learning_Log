#! /usr/bin/env bash

echo "Hello, world!"

NOME="Ornan"
SOBRENOME="Matos"

echo "$NOME" "$SOBRENOME"

NUM1=2
NUM2=6

TOTAL=$(($NUM1 + $NUM2))

echo "$TOTAL"

echo -e "\n"
echo "Hosts no seu Linux"
SAIDA_CAT="$(cat /etc/hosts)"

echo "$SAIDA_CAT"

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

echo -e "\n"

echo "Parametro 1: $1"
echo "Parametro 2: $2"

echo "Todos os Parametros: $*"
echo "Quantos Parametros: $#"

echo -e "\n"
echo "Saida do ultimo comando: $?"
echo "PID:$$"
echo "$0"




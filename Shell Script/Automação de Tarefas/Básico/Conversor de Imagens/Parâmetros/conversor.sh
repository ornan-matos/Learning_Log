#!/bin/bash

#Constante comum mente utilizada para maioria dos casos.

LOCAL=~/Downloads/imagens-livros
SAIDA=~/Downloads/imagens-livros/PNG

#Estruta de repetição. A estrutura irá se repetir proporcionalmente
#ao número de paramentros inseridos.

#A variável imagem é declarada para armazenar os parametros.

for imagem in "$@"

#Incio do bloco de comandos.

do
	mkdir ~/Downloads/imagens-livros/PNG && convert $LOCAL/"$imagem".jpg $SAIDA/"$imagem".png

	echo Conversão concluida!

done
#---------------------------------------------------------------------------------------------
# Este código separa uma lista de números inteiros em duas listas: uma com números pares e outra
# com números ímpares. A lista original 'L' é percorrida, e cada número é verificado para saber
# se é par ou ímpar. Os números pares são adicionados à lista 'pares', enquanto os números ímpares
# são adicionados à lista 'impares'.
#---------------------------------------------------------------------------------------------

# Lista de números inteiros de 0 a 10
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializando listas vazias para armazenar números pares e ímpares
pares = []
impares = []

# Percorrendo a lista 'L' para separar números pares e ímpares
for e in L:
    # Verificando se o número é par
    if e % 2 == 0:
        pares.append(e)  # Adiciona o número à lista de pares
    else:
        impares.append(e)  # Adiciona o número à lista de ímpares

# Exibindo os números pares
print(f'Números pares: {pares}')

# Exibindo os números ímpares
print(f'Números ímpares: {impares}')

L = [0,1,2,3,4,5,6,7,8,9,10]

pares = []
impares = []

for e in L:
    if e % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)

print(f'Números pares: {pares}')

print(f'Números ímpares: {impares}')


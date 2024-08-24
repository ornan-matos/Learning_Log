#-------------------------------------------------------------------------
# Programa que permite ao usuário criar duas listas de números inteiros.
# O programa continua solicitando números até que o usuário insira 0,
# que indica o fim da entrada para cada lista. Após o término da entrada
# de ambas as listas, o programa une as duas listas em uma terceira lista
# e a exibe.
#-------------------------------------------------------------------------

# Lista para armazenar números da primeira entrada
L = []

# Loop para inserir números na primeira lista
while True:
    # Solicita ao usuário um número para a primeira lista
    l1 = int(input('\nInsira os números na primeira lista:'))

    # Verifica se o número inserido é 0; se for, encerra o loop
    if l1 == 0:
        print('\nPrimeira lista finalizada.')
        break

    # Adiciona o número à primeira lista
    L.append(l1)

# Lista para armazenar números da segunda entrada
N = []

# Loop para inserir números na segunda lista
while True:
    # Solicita ao usuário um número para a segunda lista
    l2 = int(input('\nInsira os números na segunda lista:'))

    # Verifica se o número inserido é 0; se for, encerra o loop
    if l2 == 0:
        print('\nSegunda lista finalizada.')
        break

    # Adiciona o número à segunda lista
    N.append(l2)

# Lista para armazenar a combinação das duas listas
X = []

# Adiciona todos os elementos da primeira lista à nova lista
X.extend(L)

# Adiciona todos os elementos da segunda lista à nova lista
X.extend(N)

# Exibe a lista final combinada
print(f'\nLista final:\n{X}')


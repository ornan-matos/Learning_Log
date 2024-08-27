#---------------------------------------------------------------------------------------------------
# Este código em Python permite ao usuário inserir números em duas listas distintas até que o número 0 
# seja digitado, indicando o fim da inserção. Em seguida, as duas listas são combinadas, e uma terceira 
# lista é criada para armazenar os números únicos das duas primeiras listas. Por fim, os valores únicos 
# desta terceira lista são impressos com seus respectivos índices.
#---------------------------------------------------------------------------------------------------

# Inicializa três listas vazias para armazenar os números inseridos pelo usuário.
lista_1 = []
lista_2 = []
lista_3 = []

# Variável de controle para a contagem de iterações.
x = 0

# Loop para adicionar números à primeira lista até que o número 0 seja digitado.
while True:
    n = int(input('\nInsira um número: '))  # Solicita ao usuário um número.

    if n == 0:  # Verifica se o número é 0 para encerrar a inserção.
        print('\nPrimeira lista finalizada!')
        break  # Encerra o loop.

    lista_1.append(n)  # Adiciona o número à primeira lista.
    x += 1  # Incrementa a variável de controle.

# Reinicializa a variável de controle.
x = 0

# Loop para adicionar números à segunda lista até que o número 0 seja digitado.
while True:
    n = int(input('\nInsira um número: '))  # Solicita ao usuário um número.

    if n == 0:  # Verifica se o número é 0 para encerrar a inserção.
        print('\nSegunda lista finalizada!')
        break  # Encerra o loop.

    lista_2.append(n)  # Adiciona o número à segunda lista.
    x += 1  # Incrementa a variável de controle.

# Reinicializa a variável de controle.
x = 0

# Combina as duas listas em uma nova lista chamada "duas_listas".
duas_listas = lista_1[:]
duas_listas.extend(lista_2)

# Loop para adicionar elementos únicos de "duas_listas" à "lista_3".
while x < len(duas_listas):
    y = 0

    while y < len(lista_3):  # Verifica se o elemento já está na "lista_3".
        if duas_listas[x] == lista_3[y]:
            break
        y += 1

    if y == len(lista_3):  # Se o elemento não estiver na "lista_3", ele é adicionado.
        lista_3.append(duas_listas[x])

    x += 1  # Incrementa a variável de controle.

# Reinicializa a variável de controle.
x = 0

# Loop para imprimir os valores únicos da "lista_3" com seus índices.
while x < len(lista_3):
    print(f'Índice{x}: {lista_3[x]}')  # Imprime o índice e o valor correspondente.
    x += 1  # Incrementa a variável de controle.



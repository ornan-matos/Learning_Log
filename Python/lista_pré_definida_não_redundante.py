#-----------------------------------------------------------------------------------------
# Este código combina três listas de números inteiros, removendo os valores duplicados, 
# e exibe os valores únicos junto com a contagem de itens repetidos.
#-----------------------------------------------------------------------------------------

# Listas iniciais com valores inteiros
l1 = [1, 3, 5, 8]
l2 = [5, 3, 8, 9]
l3 = [1, 2, 7, 9]

# Lista vazia para armazenar valores únicos
l4 = []

# Cria uma nova lista 'all' contendo todos os elementos de l1, l2 e l3
all = l1[:]
all.extend(l2)
all.extend(l3)

x = 0  # Índice para percorrer a lista 'all'
repetidos = 0  # Contador de itens repetidos

# Laço para percorrer todos os elementos da lista 'all'
while x < len(all):
    y = 0  # Índice para percorrer a lista 'l4'

    # Verifica se o elemento atual de 'all' já está em 'l4'
    while y < len(l4):
        if all[x] == l4[y]:
            break  # Sai do laço se o item já estiver em 'l4'
        y += 1

    # Se o item não estiver em 'l4', ele é adicionado
    if y == len(l4):
        l4.append(all[x])
    else:
        repetidos += 1  # Incrementa o contador de itens repetidos

    x += 1  # Avança para o próximo item na lista 'all'

x = 0  # Reinicia o índice para percorrer 'l4'

# Exibe os elementos únicos armazenados em 'l4'
while x < len(l4):
    print(f'Índice {x} - {l4[x]}')
    x += 1

# Exibe a quantidade de itens repetidos encontrados nas listas
print(f'\nItens repetidos nas listas: {repetidos}')


#-------------------------------------------------------------------------------
# O código abaixo demonstra a manipulação de listas em Python.
# Ele começa com uma lista de frutas com alguns espaços vazios. O usuário é 
# solicitado a inserir novos nomes de frutas para substituir os espaços vazios. 
# Após isso, o código imprime o tamanho da lista e uma fatia da lista original.
# Também faz uma cópia da lista original, altera um item na cópia e imprime 
# ambas as listas.
#-------------------------------------------------------------------------------

# Lista inicial de frutas com alguns espaços vazios
frutas = ['maça', 'banana', 'morango', '', '']

# Índices para controle da substituição dos espaços vazios
x = 0
y = 3

# Loop para preencher os espaços vazios com novos nomes de frutas
while x < 2:
    # Solicita ao usuário a inserção do nome de uma nova fruta
    frutas[y] = input('\nInsira o nome da nova fruta: ')
    x += 1  # Incrementa o contador de substituições
    y += 1  # Move para o próximo espaço vazio na lista

# Imprime o tamanho da lista após a adição de novas frutas
print('\nTamanho da lista de frutas depois da adição: ', len(frutas))

# Imprime os itens novos da lista, que foram adicionados nas posições 3 e 4
print(f'\nItens novos, fatiados da lista original: {frutas[3:5]}')

# Cria uma cópia da lista original
frutas_copia = frutas[:]

# Solicita ao usuário a inserção de um novo nome de fruta para a cópia
frutas_copia[0] = input('\nNovamente... Insira o nome de uma nova fruta: ')

# Imprime a lista original e a lista copiada para comparar as mudanças
print(f'\nLista Original: {frutas}\nCopia: {frutas_copia}')


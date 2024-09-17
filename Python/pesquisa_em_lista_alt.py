#----------------------------------------------------
# Este código busca um número específico em uma lista 
# e informa se o número foi encontrado ou não.
# O código pede ao usuário para inserir um número, 
# então verifica se o número está presente na lista 'L'.
# Se encontrar o número, exibe uma mensagem e encerra 
# o loop. Se chegar ao final da lista sem encontrar o
# número, informa que o número não foi encontrado.
#----------------------------------------------------

L = [2, 4, 5, 6]  # Lista com números a serem pesquisados

x = 0  # Índice inicial para a busca

achou = False  # Flag para verificar se o número foi encontrado

p = int(input('Insira o número a ser pesquisado:'))  # Solicita ao usuário o número a ser pesquisado

while len(L) > x:  # Loop que percorre a lista até o índice final

    if L[x] == p:  # Verifica se o número na posição 'x' da lista é igual ao número pesquisado
        print(f'Achou o número {p} na lista')  # Mensagem indicando que o número foi encontrado
        break  # Encerra o loop, pois o número foi encontrado

    elif len(L) == x + 1 and L[x] != p:  # Verifica se chegou ao final da lista e o número não foi encontrado
        print('Não achou o número!')  # Mensagem indicando que o número não foi encontrado
        break  # Encerra o loop, pois o número não está na lista

    x += 1  # Incrementa o índice para verificar o próximo elemento da lista


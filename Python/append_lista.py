#-------------------------------------------------------------------------------
# O código abaixo permite ao usuário inserir números em uma lista até que 
# ele digite 0, que encerra o processo. Após isso, o programa exibe os números
# inseridos na lista.
#-------------------------------------------------------------------------------

# Inicializa uma lista vazia para armazenar os números inseridos pelo usuário.
lista = []

# Define as variáveis de controle 'x' e 'n'.
x = 0
n = 0

# Inicia um loop infinito para solicitar números do usuário.
while True:
    
    # Solicita ao usuário para inserir um número. Se o usuário digitar '0', o programa sai do loop.
    n = int(input('\nAdicione um número à lista (0 sai do programa): '))    

    # Verifica se o usuário inseriu '0' para encerrar o loop.
    if n == 0:
        break

    # Adiciona o número inserido pelo usuário à lista.
    lista.append(n)

# Exibe a lista de números inseridos.
print('\nLista de números')

# Inicia um loop para percorrer e exibir os elementos da lista.
while x < len(lista):

    # Exibe o número atual na posição 'x' da lista.
    print(f'{lista[x]}')

    # Incrementa 'x' para passar ao próximo elemento da lista.
    x += 1



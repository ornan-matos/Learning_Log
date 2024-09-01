#-----------------------------------------------------------------------------------------------------------------------
# Este script solicita ao usuário dois números inteiros que definem o início e o fim de um intervalo.
# Ele gera uma lista contendo todos os números dentro desse intervalo (inclusive).
# Se o número inicial for maior que o número final, ele exibe uma mensagem de erro e solicita a entrada novamente.
# Após a criação da lista, o script remove todos os elementos, exceto o primeiro e o último, e exibe a lista atualizada.
#-----------------------------------------------------------------------------------------------------------------------

while True:
    # Solicita ao usuário o início do intervalo
    x = int(input('Inicio do intervalo: '))

    # Solicita ao usuário o final do intervalo
    y = int(input('Final do intervalo: '))
    
    # Cria uma lista contendo todos os números do intervalo [x, y]
    lista_intervalo = list(range(x, y + 1))

    # Verifica se o início do intervalo é maior que o final
    if x > y:
        # Exibe uma mensagem de erro e solicita novas entradas
        print('\nErro! O primeiro número não pode ser maior que o último.\nTente novamente.\n')
    else:
        # Se o intervalo é válido, sai do loop
        break

# Exibe a lista completa gerada a partir do intervalo fornecido
print(f'\nLista:\n{lista_intervalo}')

# Remove todos os elementos da lista, exceto o primeiro e o último
del lista_intervalo[1:-2]

# Exibe a lista após a remoção dos elementos intermediários
print(f'\nLista atualizada:\n{lista_intervalo}')


#--------------------------------------------------------------------------------------------
# Este código simula o gerenciamento de uma fila de pessoas em um terminal de atendimento bancário.
# O atendente pode interagir com o sistema através de um menu, realizando três tipos de operações:

# 1. Atender a próxima pessoa da fila.
# 2. Adicionar uma nova pessoa à fila.
# 3. Sair do terminal.

#O código usa uma lista para representar a fila e um loop para manter o terminal ativo até que o usuário decida sair.
#--------------------------------------------------------------------------------------------

# Solicita ao usuário o número inicial de pessoas na fila
ultimo = int(input('Pessoas na fila: '))

# Cria uma lista representando a fila com números sequenciais a partir de 1
fila = list(range(1, ultimo + 1))

# Inicia um loop infinito para o terminal de atendimento
while True:

    # Exibe a quantidade de pessoas na fila atual
    print('\n---- Terminal Informações do Caixa ----\nFila atual: ', len(fila), 'Pessoas')
    
    # Apresenta as opções disponíveis para o usuário
    print('\nOpções:\nA - Realiza um atendimento\nI - Insere mais uma pessoa a fila\nS - Sair do Terminal')
    x = input('Insira a opção: ')

    # Se o usuário escolher 'A', realiza o atendimento da próxima pessoa na fila
    if x == 'A':
        if len(fila) > 0:
            # Remove a primeira pessoa da fila e exibe a mensagem de atendimento
            atendimento = fila.pop(0)
            print(f'\nCliente {atendimento} atendido\n')
        else:
            # Caso a fila esteja vazia, informa que não há ninguém para atender
            print('\nFila vazia, ninguém para atender.')
    # Se o usuário escolher 'I', adiciona uma nova pessoa à fila
    elif x == 'I':
        ultimo += 1
        fila.append(ultimo)
    # Se o usuário escolher 'S', encerra o terminal e sai do loop
    elif x == 'S':
        print('\nAtendimento encerrado.')
        break
    # Caso o usuário insira uma opção inválida, exibe uma mensagem de erro
    else:
        print('Operação invalida. Tente novamente!')


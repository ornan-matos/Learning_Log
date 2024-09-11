#---------------------------------------------------------------------------
# Este código simula o gerenciamento de duas filas de atendimento. 
# O usuário pode realizar atendimentos em ambas as filas, 
# adicionar novas pessoas a cada fila, ou sair do programa. 
# O sistema mostra o número atual de pessoas em cada fila 
# e permite ao usuário escolher a operação desejada.
#---------------------------------------------------------------------------

# Solicita ao usuário o número inicial de pessoas em cada fila
ultimo_1 = int(input('\nPessoas na primeira fila: '))
ultimo_2 = int(input('\nPessoas na segunda fila: '))

# Cria listas para representar as filas, começando do 1 até o número especificado
fila_1 = list(range(1, ultimo_1 + 1))
fila_2 = list(range(1, ultimo_2 + 1))

while True:
    # Exibe o número atual de pessoas em cada fila
    print('\nQuantidade de pessoas na Fila N°1: ', len(fila_1)) 
    print('\nQuantidade de pessoas na Fila N°2: ', len(fila_2)) 
    
    print('\n--------------------')

    # Exibe as opções de operação disponíveis
    print('\nOpções:\nA - Realiza um atendimento (Fila N°1)\nB - Realiza um atendimento (Fila N°2)\nI - Insere mais uma pessoa a fila (Fila N°1)\nG - Insere mais uma pessoa a fila (Fila N°2)\nS - Sair do Terminal')

    print('\n--------------------')

    # Solicita ao usuário uma opção
    x = input('\nInsira a opção: ')

    # Realiza um atendimento na Fila N°1
    if x == 'A':
        if len(fila_1) > 0:
            atendido = fila_1.pop(0)  # Remove e retorna o primeiro elemento da fila
            print(f'\n(Fila N°1)\nCliente N°{atendido} atendido.')
        else:
            print('Fila vazia!')

    # Realiza um atendimento na Fila N°2
    elif x == 'B':
        if len(fila_2) > 0:
            atendido = fila_2.pop(0)  # Remove e retorna o primeiro elemento da fila
            print(f'\n(Fila N°2)\nCliente N°{atendido} atendido.')
        else:
            print('Fila vazia!')

    # Adiciona uma nova pessoa na Fila N°1
    elif x == 'I':
        ultimo_1 += 1  # Incrementa o número do último cliente
        fila_1.append(ultimo_1)  # Adiciona o novo cliente à fila
        print('\nNovo cliente adicionado a fila (Fila N°1)')

    # Adiciona uma nova pessoa na Fila N°2
    elif x == 'G':
        ultimo_2 += 1  # Incrementa o número do último cliente
        fila_2.append(ultimo_2)  # Adiciona o novo cliente à fila
        print('\nNovo cliente adicionado a fila (Fila N°2)')

    # Encerra o programa
    elif x == 'S':
        print('\nAtendimento finalizado! | Terminal Encerrado.')
        break

    # Trata a entrada inválida
    else:
        print('\nOperação inválida. Tente novamente!')


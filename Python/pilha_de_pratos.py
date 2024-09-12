#-------------------------------------------------------------------------------------
# Este programa simula o controle de uma pilha de pratos.
# O usuário pode adicionar pratos à pilha, remover (lavar) pratos do topo da pilha, 
# ou encerrar o programa. O programa segue a lógica LIFO (Last In, First Out).
#-------------------------------------------------------------------------------------

print('\n________ Controle de pilha de pratos _________')

# Pergunta ao usuário quantos pratos estão inicialmente na pilha
pratos = int(input('\nQuantos pratos existem na pilha: '))

# Cria uma pilha de pratos numerados de 1 até o número informado pelo usuário
pilha = list(range(1, pratos + 1))

# Inicia o loop principal do programa
while True:

    print('\n------------')
    # Exibe a quantidade atual de pratos na pilha
    print(f'\nStatus atual da pilha de prato: {len(pilha)}')

    # Exibe o menu de opções para o usuário
    print('\nMenu:\nE - Adiciona um novo prato a pilha.\nD - remove o prato da pilha.\nS - Encerra o programa.')

    # Captura a opção digitada pelo usuário
    x = input('\nOpção: ')

    # Se a opção for "D" (remover prato)
    if x == 'D':

        # Verifica se há pratos na pilha para remover
        if len(pilha) > 0:
            # Remove o prato do topo da pilha (último prato adicionado)
            lavado = pilha.pop(-1)
            print(f'\nPrato {lavado} lavado.')
        else:
            # Informa ao usuário que todos os pratos foram lavados
            print('\nParabéns!\nA pilha está vazia. Todos os pratos foram lavados.')
    
    # Se a opção for "E" (adicionar novo prato)
    elif x == 'E':
        # Adiciona um novo prato ao topo da pilha
        pratos += 1
        pilha.append(pratos)
        print('\nPrato adicionado a pilha.')

    # Se a opção for "S" (encerrar o programa)
    elif x == 'S':
        # Finaliza o programa
        print('\nPrograma finalizado!')
        break
    
    # Se a opção for inválida
    else:
        print('\nOpção inválida. Tente novamente.')


##########################################################################################
# Este programa permite ao usuário gerar a tabuada para diferentes operações matemáticas 
# (adição, subtração, multiplicação e divisão) de um número inteiro especificado. 
# O usuário pode escolher o tipo de operação e o número para o qual deseja gerar a tabuada.
# O programa continua executando até que o usuário escolha a opção para sair.
##########################################################################################

print('\nTabuada de números inteiros')  # Exibe o título do programa

while True:  # Loop principal que continuará até o usuário escolher sair
    print('\nInsira o numero correspondente a sua escolha.\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair')

    tipo = int(input('\nOpção: '))  # Solicita ao usuário o tipo de operação desejada

    if tipo == 0:  # Se o usuário escolher 0, o programa será finalizado
        print('\nPrograma finalizado!')
        break  # Interrompe o loop e encerra o programa

    numero = int(input('\nNúmero: '))  # Solicita ao usuário o número para gerar a tabuada

    cont = 0  # Inicializa o contador para gerar a tabuada de 1 a 10

    if tipo == 1:  # Se a opção escolhida for adição
        while cont < 10:  # Loop para gerar a tabuada de adição
            cont += 1  # Incrementa o contador
            print(f'{numero} + {cont} = {numero+cont}')  # Exibe o resultado da adição

    elif tipo == 2:  # Se a opção escolhida for subtração
        while cont < 10:  # Loop para gerar a tabuada de subtração
            cont += 1  # Incrementa o contador
            print(f'{numero} - {cont} = {numero-cont}')  # Exibe o resultado da subtração

    elif tipo == 3:  # Se a opção escolhida for multiplicação
        while cont < 10:  # Loop para gerar a tabuada de multiplicação
            cont += 1  # Incrementa o contador
            print(f'{numero} x {cont} = {numero*cont}')  # Exibe o resultado da multiplicação

    elif tipo == 4:  # Se a opção escolhida for divisão
        while cont < 10:  # Loop para gerar a tabuada de divisão
            cont += 1  # Incrementa o contador
            # Exibe o resultado da divisão com duas casas decimais
            print(f'{numero} / {cont} = {numero/cont:.2f}')

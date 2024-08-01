
print('\nTabuada de números inteiros')
while True:
    print('\nInsira o numero corespondente a sua escolha.\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair')

    tipo = int(input('\nOpção: '))

    if tipo == 0:
        print('\nPrograma finalizado!')
        break
 
    numero = int(input('\nNúmero: '))

    cont = 0

    
    if tipo == 1:

        while cont < 10:
            cont += 1
            print(f'{numero} + {cont} = {numero+cont}')

    elif tipo == 2:
        while cont < 10:
            cont += 1
            print(f'{numero} - {cont} = {numero-cont}')


    elif tipo == 3:
        while cont < 10:
            cont += 1
            print(f'{numero} x {cont} = {numero*cont}')



    elif tipo == 4:
        while cont < 10:
            cont += 1
            print(f'{numero} / {cont} = {numero/cont:.2f}')




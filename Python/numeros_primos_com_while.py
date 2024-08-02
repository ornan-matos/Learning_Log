##############################################################################################
# O programa solicita ao usuário que insira um número e determina se o número é primo ou não.
# ou não. O programa trata casos especiais e fornece feedback ao usuário sobre a primalidade
# do número fornecido.
##############################################################################################

print('\nVerifique se um número é primo')

num = 0

# Loop para garantir que o usuário insira um número válido (>= 2)
while num < 2:

    num = int(input('\nNúmero: '))

    # Verifica se o número é negativo
    if num < 0:
        print('\nNúmeros negativos não são permitidos.\nTente novamente.')

    # Verifica se o número é 0 ou 1, casos especiais
    elif num == 0 or num == 1:
        print(f'\n{num} se trata de um caso especial.\nTente novamente.')

    # Verifica se o número é 2, que é o único número primo par
    elif num == 2:
        print(f'\n{num} é um número primo. O único número par que se encaixa nessa categoria.')

    # Verifica se o número é par e maior que 2 (não é primo)
    elif num % 2 == 0:
        print(f'\n{num} não é um número primo porque é divisível por 2.')

    # Verifica se o número é ímpar e maior que 2
    else:
        x = 3  # Começa a verificação a partir do menor divisor ímpar possível

        # Verifica se o número é divisível por algum número ímpar menor que ele
        while x < num:
            if num % x == 0:
                break
            else:
                x += 2  # Incrementa para o próximo divisor ímpar

        # Se o loop termina e x é igual ao número, então o número é primo
        if x == num:
            print(f'\n{num} é um número primo.')
        else:
            print(f'\n{num} não é primo porque é divisível por {x}')


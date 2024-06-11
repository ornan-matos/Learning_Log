##########################################################################

#Este código implementa uma calculadora simples em Python que permite ao usuário 
#realizar as quatro operações matemáticas básicas:
#adição, subtração, multiplicação e divisão. 
#O programa solicita ao usuário que escolha a operação desejada e 
#insira os dois números a serem operados. 
#Em seguida, ele calcula e exibe o resultado.

##########################################################################


# Cabeçalho: Calculadora Simples
print('Operação Matemática\n') # Título do programa

# Solicita ao usuário para escolher a operação
operacao = int(input(' 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n')) 

# Solicita os dois números ao usuário
num1 = int(input('Insira o primeiro número: \n'))
num2 = int(input('Insira o segundo número: \n'))

# Bloco condicional para realizar a operação escolhida
if operacao == 1: # Adição
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}') # Exibe o resultado da adição
elif operacao == 2: # Subtração
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}') # Exibe o resultado da subtração
elif operacao == 3: # Multiplicação
    resultado = num1 * num2
    print(f'{num1} x {num2} = {resultado}') # Exibe o resultado da multiplicação
elif operacao == 4: # Divisão
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado}') # Exibe o resultado da divisão
else: # Opção inválida
    print('Desculpe, não reconheço essa opção. Tente novamente.')


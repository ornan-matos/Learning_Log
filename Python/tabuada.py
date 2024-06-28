##############################################
#Este código em Python tem como funcionalidade 
#gerar e exibir a tabuada de um número 
#específico fornecido pelo usuário. 
##############################################

# Solicita ao usuário que insira o número para o qual a tabuada será gerada
num = int(input('Tabuada de: '))

# Inicializa a variável x com o valor 1
x = 1

# Loop while para gerar a tabuada do número fornecido pelo usuário
while x <= 10:
    # Calcula o produto do número fornecido pelo usuário com o valor atual de x
    y = x * num
    # Exibe o resultado da multiplicação no formato "num x x = y"
    print(f'{num} x {x} = {y}')
    # Incrementa o valor de x em 1 para a próxima iteração
    x = x + 1


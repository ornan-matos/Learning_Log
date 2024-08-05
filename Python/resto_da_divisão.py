# -----------------------------------------------------------------------------
# Este programa realiza a operação de divisão inteira e calcula o resto
# da divisão entre dois números inteiros fornecidos pelo usuário. 
# A divisão é feita subtraindo-se o divisor do dividendo repetidamente 
# até que o dividendo seja menor que o divisor. 
# O valor restante do dividendo é o resto da divisão.
# -----------------------------------------------------------------------------

# Solicita ao usuário o dividendo
x = int(input('\nInsira o dividendo: '))

# Solicita ao usuário o divisor
y = int(input('\nInsira o divisor: '))

# Inicializa o resto da divisão como 0
r = 0

# Armazena o valor original do dividendo para exibição posterior
q = x

# Laço que realiza a subtração repetida
while True:

    #Se algum número inserido for zero o programa para
    if y or x == 0:
        print('\nNão é possível dividir zero')
        break

   # Verifica se o dividendo é menor que o divisor
    if x - y < 0:
        # Exibe o resultado final do resto da divisão
        print(f'\nO resto da divisão de {q} / {y} é igual a {x}')
        # Encerra o loop
        break
    
    # Subtrai o divisor do dividendo
    x = x - y 
    
    # Verifica se o dividendo se tornou zero
    if x == 0:
        # Exibe o resultado final do resto da divisão
        print(f'\nO resto da divisão de {q} / {y} é igual a {x}')
        # Encerra o loop
        break
   

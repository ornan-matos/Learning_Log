##############################################################################

# Programa para imprimir números pares e ímpares até um limite definido pelo usuário.

##############################################################################

# Números Pares

# Solicita ao usuário o valor limite para a impressão de números pares.
fim = int(input("Insira o último número par a ser impresso: "))

# Inicializa a variável 'x', que será usada como contador.
x = 0

# Loop 'while' que continuará enquanto 'x' for menor ou igual ao limite 'fim'.
while x <= fim:
    # Verifica se 'x' é par usando o operador módulo (%). Se o resto da divisão por 2 for 0, 'x' é par.
    if x % 2 == 0:
        # Imprime o valor de 'x' se for par.
        print(x)
    # Incrementa 'x' em 1 para passar para o próximo número.
    x = x + 1

# Números Ímpares

# Pula uma linha para separar visualmente os resultados.
print("\n")

# Reinicia o contador 'x' para 0.
x = 0

# Loop 'while' para imprimir números ímpares.
while x <= fim:
    # Verifica se 'x' é ímpar. Se o resto da divisão por 2 não for 0, 'x' é ímpar.
    if x % 2 != 0:
        # Imprime o valor de 'x' se for ímpar.
        print(x)
    # Incrementa 'x' em 1 para passar para o próximo número.
    x = x + 1

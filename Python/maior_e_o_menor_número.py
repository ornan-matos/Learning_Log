##############################################################################

# Programa para encontrar o maior e o menor número entre três entradas.
# Solicita ao usuário que insira três números inteiros e utiliza uma série de
# comparações condicionais (if) para determinar o maior e o menor valor,
# imprimindo-os em ordem decrescente.

##############################################################################

# Solicita ao usuário a entrada de três números inteiros e os armazena nas variáveis a, b e c.
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

# Primeira série de comparações: Verifica se 'a' é o maior número.
if a > b and a > c:
    print(a) # Se 'a' for o maior, imprime 'a'.

    # Comparações aninhadas para encontrar o menor:
    if b < a and b < c:
        print(b) # Se 'b' for o menor, imprime 'b'.
    if c < a and c < b:
        print(c) # Se 'c' for o menor, imprime 'c'.

# Segunda série de comparações: Verifica se 'b' é o maior número.
if b > a and b > c:
    print(b) # Se 'b' for o maior, imprime 'b'.

    # Comparações aninhadas para encontrar o menor:
    if a < b and a < c:
        print(a) # Se 'a' for o menor, imprime 'a'.
    if c < b and c < a:
        print(c) # Se 'c' for o menor, imprime 'c'.

# Terceira série de comparações: Verifica se 'c' é o maior número.
if c > a and c > b:
    print(c) # Se 'c' for o maior, imprime 'c'.

    # Comparações aninhadas para encontrar o menor:
    if b < c and b < a:
        print(b) # Se 'b' for o menor, imprime 'b'.
    if a < b and a < c:
        print(a) # Se 'a' for o menor, imprime 'a'.

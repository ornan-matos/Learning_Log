#-------------------------------------------------------------------------------------------------------
# Este código encontra o maior valor em uma lista de números inteiros.
# O código inicializa uma lista com quatro números, assume o primeiro número como o maior
# e depois itera pela lista para encontrar o maior valor. Finalmente, imprime o maior valor encontrado.
#-------------------------------------------------------------------------------------------------------

# Inicializa a lista de números
numeros = [3, 7, 23, 5]

# Assume que o primeiro número é o maior
maximo = numeros[0]

# Itera sobre cada valor na lista
for valor in numeros:
    # Se o valor atual for maior que o valor máximo conhecido
    if maximo < valor:
        # Atualiza o valor máximo
        maximo = valor

# Imprime o maior valor encontrado
print(maximo)

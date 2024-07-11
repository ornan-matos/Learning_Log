########################################################################################################
# Este programa solicita ao usuário que insira números inteiros positivos.
# O programa continua solicitando números até que o usuário insira um número negativo.
# Quando um número negativo é inserido, o programa exibe a soma de todos os números positivos inseridos.
########################################################################################################

# Inicializa o acumulador
soma = 0

print("Programa para somar números positivos.")
print("Digite números positivos para somar.")
print("Digite um número negativo para finalizar e exibir a soma.")

# Loop para receber números do usuário
while True:
    # Solicita ao usuário um número
    numero = int(input("Digite um número: "))

    # Verifica se o número é negativo
    if numero < 0:
        # Se o número é negativo, interrompe o loop
        break

    # Adiciona o número ao acumulador
    soma += numero

# Exibe a soma dos números positivos
print("A soma dos números positivos é:", soma)

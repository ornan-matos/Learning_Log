###############################################
#Programa para ler números inteiros do teclado 
#até que o usuário digite 0.
#O programa exibe a quantidade de números 
#digitados, a soma e a média aritmética.
###############################################

# Inicializa as variáveis
quantidade_numeros = 0
soma_numeros = 0

print("Digite números inteiros (0 para terminar):")

while True:
    # Lê o número do usuário
    numero = int(input())

    # Verifica se o número é 0 para terminar o loop
    if (numero == 0):
        break

    # Atualiza a quantidade e a soma dos números
    quantidade_numeros += 1
    soma_numeros += numero

# Calcula a média aritmética
if quantidade_numeros > 0:
    media = soma_numeros / quantidade_numeros
else:
    media = 0

# Exibe os resultados
print(f"\nQuantidade de números digitados: {quantidade_numeros}")
print(f"\nSoma dos números digitados: {soma_numeros}")
print(f"\nMédia aritmética dos números digitados: {media}")

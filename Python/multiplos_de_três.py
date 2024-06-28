# Geração dos 10 primeiros múltiplos de três

# Inicializa o valor de x para começar a busca por múltiplos de três
x = 0

# Inicializa o contador y com o número de múltiplos de três desejados
y = 10

# Loop continua até que 10 múltiplos de três sejam encontrados e impressos
while y >= 0:
    # Verifica se o valor atual de x é um múltiplo de três
    if x % 3 == 0:
        # Se for múltiplo de três, imprime o valor de x
        print(x)
        # Decrementa o contador y indicando que um múltiplo foi encontrado
        y = y - 1
    # Incrementa x para verificar o próximo número
    x = x + 1


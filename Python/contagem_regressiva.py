# Este pequeno programa realiza uma contagem regressiva simples para o lançamento de um foguete.
# Funcionamento: A contagem regressiva começa em 10 e diminui até chegar a 1, 
# momento em que a mensagem "Fogo!" é exibida.

# Exibe a mensagem inicial da contagem regressiva
print('Contagem regressiva para o lançamento do foguete!\n')

# Define o valor inicial da contagem regressiva
x = 10 

# Loop while para realizar a contagem regressiva
while x > 1:
    # Exibe o valor atual da contagem
    print(x)
    # Decrementa o valor de x em 1
    x = x - 1

# Exibe a mensagem final quando a contagem regressiva termina
print('\nFogo!')


##########################################################################
# Programa para calcular o número de cédulas e moedas necessárias para o 
# pagamento de um valor especificado pelo usuário.
# Ele funciona da seguinte forma:
# 1. Solicita ao usuário o valor a ser pago.
# 2. Verifica se o valor é zero; se for, encerra o programa.
# 3. Se o valor for negativo, solicita a entrada novamente.
# 4. Calcula a quantidade de cédulas e moedas necessárias para o valor usando um loop.
# 5. Exibe a quantidade de cada cédula ou moeda utilizada.
# 6. Repeats the process until the value is reduced to less than 0.01.
##########################################################################


#Inicia um loop infinito. Que oferece a alternativa ao usuário a finaliza-lo ao longo da execução do programa.
while True:

# Solicita ao usuário para digitar o valor a ser pago
    valor = float(input("\nDigite o valor a pagar:"))

# Verifica se o valor inserido foi zero. Se sim, finaliza o programa
    if valor == 0:
        print('Programa finalizado!')
        break

# Verifica se o valor é menor que zero. Se sim, o programa pede para o usuário corrigir o valor
    while valor < 0:
        print('\nValor incorreto! Números negativos não são permitdos.\nDigite novamente.')

# Solicita ao usuário para digitar o valor a ser pago
        valor = float(input("\nDigite o valor a pagar:"))

# Verifica se o valor inserido foi zero. Se sim, finaliza o programa
        if valor == 0:
            break


# Verifica se o valor inserido foi zero. Se sim, finaliza o programa
    if valor == 0:
        print('Programa finalizado!')
        break


# Inicializa o contador de cédulas e o valor da cédula/moeda atual
    cedulas = 0
    atual = 200
    apagar = valor

# Loop principal para calcular as cédulas e moedas necessárias
    while True:
    # Verifica se a cédula ou moeda atual pode ser usada para o valor restante
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
        # Exibe a quantidade de cédulas ou moedas do valor atual
            if atual >= 1:
                print(f"{cedulas} cédula(s) de R${atual}")
            else:
                print(f"{cedulas} moeda(s) de R${atual:.2f}")

        # Termina o loop se o valor restante for menor que 0.01
            if apagar < 0.01:
                break
        
        # Atualiza o valor da cédula ou moeda para o próximo menor valor
            if atual == 200:
                atual = 100
            elif atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 2
            elif atual == 2:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.25
            elif atual == 0.25:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.01

        # Reinicializa o contador de cédulas para o novo valor
            cedulas = 0

#Programa para calcular o número de cédulas e moedas necessárias para o 
#pagamento de um valor especificado pelo usuário.
#1. Solicita ao usuário o valor a ser pago.
#2. Inicializa a variável `atual` com o maior valor de cédula ou moeda (R$200).
#3. Utiliza um loop para determinar quantas cédulas ou moedas de cada valor são
#necessárias para compor o valor total.
#4. Após determinar a quantidade de cédulas ou moedas de cada valor, exibe
#a quantidade de cada tipo utilizado.
#5. O programa continua até que o valor restante a ser pago seja menor que 0.01
#(precisão para centavos).
#6. Atualiza o valor da cédula ou moeda a ser usada na próxima iteração, reduzindo
#progressivamente de acordo com as cédulas e moedas disponíveis.
#Nota: O código assume que o valor inserido pelo usuário é positivo e que o  
#sistema lida corretamente com valores até centavos.

# Solicita ao usuário para digitar o valor a ser pago
valor = float(input("\nDigite o valor a pagar:"))

# Inicializa o contador de cédulas e o valor da cédula/moneda atual
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

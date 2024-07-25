
# Solicita ao usuário para digitar o valor a ser pago
valor = int(input("\nDigite o valor a pagar:"))

# Inicializa a quantidade de cédulas e a denominação atual
cedulas = 0
atual = 100
apagar = valor

# Loop para distribuir as cédulas até que o valor total seja pago
while True:
    # Verifica se a cédula atual pode ser usada para pagar parte do valor
    if atual <= apagar:
        # Subtrai o valor da cédula atual do valor total a pagar
        apagar -= atual
        # Incrementa o contador de cédulas da denominação atual
        cedulas += 1
    
    else:
        # Imprime a quantidade de cédulas da denominação atual utilizadas
        print(f'{cedulas} cédula(s) de R$ {atual}')
        # Verifica se o valor total já foi completamente pago
        if apagar == 0:
            break
        # Atualiza a denominação da cédula para a próxima menor disponível

        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        # Reseta o contador de cédulas para a nova denominação
        cedulas = 0



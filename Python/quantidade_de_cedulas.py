
# Solicita ao usuário para digitar o valor a ser pago
valor =  float(input("\nDigite o valor a pagar:"))

# Inicializa a quantidade de cédulas e a denominação atual
cedulas = 0
atual = 200
apagar = int(valor)

atual_f = 0.50
apagar_f = float(valor - apagar)
moedas = 0

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

        # Reseta o contador de cédulas para a nova denominação
        cedulas = 0


while True:
    
    if atual_f <= apagar_f:

        apagar_f -= atual_f

        moedas += 1

    else:

        print(f'{moedas} moeda(s) de R$ {atual_f:0.2f}')
        
        if atual_f == 0:
            break

        if atual_f == 0.50:
            atual_f = 0.25
        elif atual_f == 0.25:
            atual_f = 0.10
        elif atual_f == 0.10:
            atual_f = 0.05
        elif atual_f == 0.05:
            atual_f = 0.01

        moedas = 0




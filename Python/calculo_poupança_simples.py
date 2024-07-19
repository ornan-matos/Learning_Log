###################################################
#Este programa calcula os juros simples de uma 
#poupança ao longo de 24 meses.
#O usuário informa o valor inicial do depósito 
#e a taxa de juros mensal.
#O programa então calcula e exibe o saldo e os 
#juros acumulados ao final de cada mês.
###################################################

# Solicita ao usuário o valor do primeiro depósito
deposito = float(input('Valor do Primeiro Depósito.\nR$ '))

# Solicita ao usuário a taxa de juros mensal (em porcentagem)
taxa_juros = float(input('Taxa de Juro (Porcentagem):'))

# Inicializa variáveis
mes = 1           # Contador de meses
saldo = deposito  # Saldo inicial é igual ao depósito inicial
total_juros = 0   # Acumulador de juros ganhos
deposito_mensal = 0 #Acumulador de depósitos realizados mensalmente

# Loop para calcular os juros e o saldo para cada um dos 24 meses
while mes <= 24:
 
    #Sinalização do mês impresso na tela 
    print('\n----------------------------------')
    print(f'Mês {mes}\n') 
 
    #Novos depósitos iniciam a partir do segundo mês
    if mes >= 2:
        deposito_mensal = float(input('Deposito do presente mês R$: '))

    # Calcula os juros ganhos no mês
    juros_ganhos = ((saldo + deposito_mensal) / 100) * taxa_juros

    # Atualiza o saldo com os juros ganhos
    saldo = saldo + juros_ganhos + deposito_mensal
    
    # Acumula os juros ganhos no total de juros
    total_juros = total_juros + juros_ganhos
    
    # Exibe as informações do mês atual
    print(f'\nTotal de juros ganhos \nR$ {total_juros:.2f}')
    print(f'\nSaldo \nR$ {saldo:.2f}')
    
    # Incrementa o contador de meses
    mes = mes + 1
    
# Exibe uma linha final separadora
print('----------------------------------')

#####################################################################
#Este programa é uma simulação de pagamento de dívida. O usuário 
#deve informar o valor da dívida inicial, a taxa de juros mensais,
#e o valor que ele pode pagar mensalmente. O programa calcula quanto 
#tempo levará para quitar a dívida,o total pago incluindo juros, e o 
#total de juros pagos.
#####################################################################


# Exibe a mensagem inicial
print('\n----- Simulação pagamento de dívida -----\n')

# Solicita ao usuário o valor da dívida inicial
divida = float(input('\nValor da dívida R$ '))

# Solicita ao usuário a taxa de juros mensais
juros = float(input('\nJuros mensais (Ex.: 5 para 5%): '))

# Solicita ao usuário o valor que ele pode pagar mensalmente
pagamento = float(input('\nValor a ser pago mensalmente R$ '))

# Inicializa as variáveis
mes = 0  # contador de meses
taxa = juros / 100 * divida  # calcula a taxa de juros inicial
saldo = divida  # saldo começa igual ao valor da dívida
taxa_total = 0  # acumula o total de juros pagos
pagamento_total = 0  # acumula o total pago

# Verifica se o pagamento mensal é suficiente para cobrir os juros
if pagamento < taxa:
    print(f'Sua dívida não será paga nunca.\nVocê não pode usar o valor de R$ {pagamento:.2f} para\ncobrir a taxa de juros de {taxa:.2f}%')
else:
    # Loop até que o saldo seja menor que o valor do pagamento
    while pagamento < saldo:
        # Atualiza a taxa de juros para o saldo atual
        taxa = juros / 100 * saldo
        # Atualiza o saldo subtraindo o pagamento e adicionando a taxa de juros
        saldo = saldo + taxa - pagamento
        # Acumula o total de juros pagos
        taxa_total = taxa_total + taxa
        # Acumula o total pago
        pagamento_total = pagamento_total + pagamento
        # Incrementa o contador de meses
        mes = mes + 1

# Exibe os resultados da simulação
print('\n--- Resultado da Simulação ---\n')
print(f'Total pago R$ {pagamento_total:.2f}')
print(f'Total de Juros pagos R$ {taxa_total:.2f}')
print(f'Total de meses necessários {mes} meses')
print(f"No último mês, você teria o valor de R${saldo:.2f} restante a pagar.")


##############################################################################

# Este programa simula o pagamento de uma dívida com juros compostos mensais.
# Ele calcula o tempo (em meses) para quitar a dívida, o total pago e o total de juros pagos.

##############################################################################

# Entrada de dados do usuário
valor_divida = float(input("Valor da divida: "))
juros_mensal = float(input("\nPorcentagem de juros mensal: \n"))
pag_mensal = float(input("\nValor a ser pago mensalmente: \n"))

# Inicialização de variáveis
pag_mensal_total = 0  # Total pago ao longo do tempo
cont = 0             # Contador de meses
juros_total = 0      # Total de juros pagos

# Loop principal (executa enquanto a dívida for maior ou igual a zero)
while valor_divida >= 0:

    # Cálculo dos juros do mês
    juros_final = (juros_mensal / 100) * valor_divida
    juros_total = juros_final + juros_total  # Acumula os juros

    # Atualização do valor da dívida após o pagamento e os juros
    valor_divida = (valor_divida + juros_final) - pag_mensal

    # Acumula o total pago e incrementa o contador de meses
    pag_mensal_total = pag_mensal_total + pag_mensal
    cont = cont + 1

# Correção para o último pagamento (pode ser menor que o valor mensal)
pag_mensal_total = pag_mensal_total + valor_divida

# Saída dos resultados
print(f"\nTotal pago: R${pag_mensal_total:.2f}")  # Total pago formatado com 2 casas decimais
print(f"Meses: {cont}")                         # Número de meses
print(f"Total juros pago R${juros_total:.2f}")   # Total de juros formatado

###########################################################################################################
# Programa de cálculo de poupança com juros compostos
# Este programa solicita ao usuário o valor do depósito inicial e a taxa de juros mensal de uma poupança.
# Em seguida, ele calcula e exibe o saldo mês a mês durante os primeiros 24 meses.
# No final, o programa exibe o total ganho com juros no período.
###########################################################################################################


# Solicita ao usuário o depósito inicial
deposito_inicial = float(input("Digite o valor do depósito inicial: R$ "))

# Solicita ao usuário a taxa de juros mensal
taxa_juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100

# Inicializa o saldo atual com o depósito inicial
saldo_atual = deposito_inicial

# Inicializa o total ganho com juros
total_juros = 0

# Inicializa o contador de meses
mes = 1

# Exibe o cabeçalho da tabela
print("\nMês\tSaldo")

# Loop while para calcular e exibir o saldo mês a mês durante 24 meses
while mes <= 24:
    # Calcula os juros do mês
    juros_mes = saldo_atual * taxa_juros

    # Atualiza o saldo atual com os juros do mês
    saldo_atual += juros_mes

    # Acumula o total ganho com juros
    total_juros += juros_mes

    # Exibe o mês e o saldo atual
    print(f"{mes}\tR$ {saldo_atual:.2f}")

    # Incrementa o contador de meses
    mes += 1

# Exibe o total ganho com juros no período de 24 meses
print(f"\nTotal ganho com juros em 24 meses: R$ {total_juros:.2f}")


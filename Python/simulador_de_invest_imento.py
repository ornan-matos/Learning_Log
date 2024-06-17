##############################################################################

# Simulador de Investimento com Depósitos Mensais
# Este programa calcula o saldo de um investimento ao longo de 24 meses,
# considerando um depósito inicial, uma taxa de juros mensal e depósitos
# adicionais mensais a partir do segundo mês.

##############################################################################

# Entrada de dados
dep = float(input("\nDepósito inicial: "))  # Valor inicial investido
tax = float(input("\nTaxa de Juros (mês): "))  # Taxa de juros mensal (em %)
add = float(input("\nDepósito mensal (a partir do segundo mês): "))  # Valor adicionado mensalmente

# Cálculo dos juros do primeiro mês
juros = ((dep * tax) / 100)  # Juros do primeiro mês

# Variável para controlar o mês atual
mes = 1

# Loop para simular os 24 meses
while mes <= 24:
    # Acumulador de saldo
    if mes > 1:  # A partir do segundo mês, considera o depósito mensal
        juros_mes = ((dep + add) * tax) / 100  # Calcula os juros do mês
        dep = (dep + add) + juros_mes  # Atualiza o saldo com juros e depósito
    else:  # No primeiro mês, considera apenas o depósito inicial
        dep = dep + juros  # Atualiza o saldo com os juros do primeiro mês

    # Imprime o saldo acumulado no mês atual
    print(f"\nMês {mes}\nTotal Acumulado: R${dep:.2f}\n")

    # Incrementa o contador de mês
    mes = mes + 1

##############################################################################

# Programa de Análise de Elegibilidade para Empréstimo Imobiliário

# Este programa tem como objetivo verificar se um potencial comprador de imóvel
# é elegível para um empréstimo, com base em seu salário, valor da casa e
# período de pagamento desejado. A elegibilidade é determinada pela regra de
# que a prestação mensal não pode exceder 30% da renda do comprador.

##############################################################################

# Solicita ao usuário que insira seu salário, o valor da casa e o período de pagamento em anos.
salario = float(input("Insira o seu salário: "))
casa = float(input("Insira o valor da casa: "))
anos = int(input("Insira a quantidade de anos para pagar: "))

# Calcula o valor da prestação mensal dividindo o valor da casa pelo número total de meses.
prestacao = casa / (anos * 12)

# Verifica se o valor da prestação é menor que o salário do usuário.
if prestacao < salario:
    # Se a prestação for menor que o salário, calcula a porcentagem que a prestação representa em relação ao salário.
    porcentagem = (prestacao / salario) * 100

    # Verifica se a porcentagem da prestação em relação ao salário é menor ou igual a 30%.
    if porcentagem <= 30:
        # Se a porcentagem for menor ou igual a 30%, informa ao usuário que ele é elegível para o empréstimo.
        print("Você é elegivel!")
    else:
        # Se a porcentagem for maior que 30%, informa ao usuário que o valor da parcela ultrapassou o limite máximo da sua renda.
        print("Desculpe. O valor da parcela ultrapassou o limite máximo da sua renda.")
else:
    # Se a prestação for maior ou igual ao salário, informa ao usuário que não será possível realizar o empréstimo.
    print("Desculpe. Não será possível realizar o empréstimo.")

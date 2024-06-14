##############################################################################

# Programa de Cálculo de Reajuste Salarial
# Este programa tem como objetivo calcular 
#o novo salário de um funcionário após um reajuste.
# O reajuste é de 10% para salários acima de R$ 1250 e de 15% 
#para salários iguais ou inferiores a R$ 1250.

##############################################################################

# Solicita ao usuário que insira o salário atual e armazena o valor como um número de ponto flutuante (float).
salario_atual = float(input("Insira o seu salário atual: "))

# Verifica se o salário atual é maior que R$ 1250.
if salario_atual > 1250:
    # Se for maior, calcula o novo salário aplicando um aumento de 10%.
    salario_final = (salario_atual * 0.10) + salario_atual
    # Imprime o novo salário formatado com duas casas decimais.
    print(f"Novo salário: {salario_final:.2f}")

# Se o salário atual não for maior que R$ 1250, ou seja, for menor ou igual, entra neste bloco.
if salario_atual <= 1250:
    # Calcula o novo salário aplicando um aumento de 15%.
    salario_final = (salario_atual * 0.15) + salario_atual
    # Imprime o novo salário formatado com duas casas decimais.
    print(f"Novo salário: {salario_final:.2f}")

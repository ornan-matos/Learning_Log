##############################################################################

# Programa para cálculo de multa por excesso de velocidade

# Este programa solicita ao usuário que digite sua velocidade em km/h.
# Se a velocidade ultrapassar 80 km/h, calcula e exibe o valor da multa a ser paga.

##############################################################################

# Solicita ao usuário que insira a velocidade e converte para um número inteiro
velocidade = int(input("Digite a velocidade em KM/h: "))

# Verifica se a velocidade ultrapassa o limite permitido (80 km/h)
if velocidade > 80:
    # Calcula o valor da multa: R$ 5.00 por cada km/h acima do limite
    multa = (velocidade - 80) * 5

    # Exibe a mensagem de multa formatada com duas casas decimais
    print(f"\n\tVocê foi multado em R${multa:.2f}")

    # Exibe uma mensagem adicional para efetuar o pagamento
    print("\nEfetue o pagamento o mais breve possível!")

print("\n---- Movida Aluguel de Veículos ---\n")

distancia = int(input("Informe a quantidade de KM percorrida com o veículo: "))

dias = int(input("Quantas diárias foram utilizadas: "))

valor_final = (dias * 60) + (distancia * 0.15)

print(f"\n Total aluguel do Veículo: R${valor_final:.2f}")


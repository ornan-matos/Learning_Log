distancia = int(input("\nQual a distância em KM que você vai percorrer: "))

if distancia <= 200:
    valor = distancia * 0.50
    print(f"\nValor da viagem é R$ {valor:.2f}")

else:
    valor = distancia * 0.45
    print(f"\nValor da viagem é R$ {valor:.2f}")

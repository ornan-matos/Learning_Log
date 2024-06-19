##############################################################################

# Calcular o valor de uma corrida de táxi com base na distância percorrida.
# A tarifa é de R$0,50 por km para distâncias de até 200km e R$0,45 por km para distâncias maiores.

##############################################################################

# Solicita ao usuário a distância percorrida
distancia = int(input("Insira a distância percorrida (em km): "))

# Verifica a distância para aplicar a tarifa correta
if distancia <= 200:  # Se a distância for menor ou igual a 200km
    valor = distancia * 0.50  # Calcula o valor com a tarifa de R$0.50/km
    print(f"O valor final da viagem de {distancia}km é R${valor:.2f}")  # Exibe o valor formatado com 2 casas decimais
else:  # Se a distância for maior que 200km
    valor = distancia * 0.45  # Calcula o valor com a tarifa de R$0.45/km
    print(f"O valor final da viagem de {distancia}km é R${valor:.2f}")  # Exibe o valor formatado com 2 casas decimais

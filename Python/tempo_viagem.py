#Calcular tempo de viagem de veiculo

print("\n -- Tempo de Viagem --\n")

distancia = int(input("Qual a distancia em KM: "))
velocidade = int(input("Qual a velocidade media Km/h: "))

tempo = distancia // velocidade

print("\nVocê chegara em seu destino em", tempo, "horas")

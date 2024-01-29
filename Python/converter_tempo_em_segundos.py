print("Converso de Tempo em Segundos\n")

dia = int(input("Dia(s): "))

dia = dia * 24 * 60 * 60

hora = int(input("Hora(s): "))

hora = hora * 60 * 60

minutos = int(input("Minuto(s): "))

minutos = minutos * 60

segundos = int(input("segundo(s): "))

print("\nO total de segundos é ", dia + hora + minutos + segundos, "segundos")

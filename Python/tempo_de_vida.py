print ("\n -- Tempo de vida perdido -- \n")

cigarros_dia = int(input("Quantidade de cigarros por dia: "))

anos_fumandos = int(input("Anos usando cigarro: "))

tempo_minutos: float = (cigarros_dia * 10) * 365 * anos_fumandos

tempo_dias: float = tempo_minutos / 1440

print("\n--- Resultatos ---")

print(f"Você perdeu {tempo_minutos} minutos de vida ")

print(f"Você perdeu {tempo_dias:.0f} dias de vida ")


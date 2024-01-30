preco = float(input("Valor da Mercadoria: "))

porcentagem = float(input("Porcentagem: ")[:-1])

varlo_desconto = preco * (porcentagem/100)

valor_final = preco - varlo_desconto

print(f"Valor do desconto R${varlo_desconto:.2f}")

print(f"Total final = R${valor_final:.2f}")






velocidade = int(input("Velocidade do veiculo:"))

if velocidade > 80:
    
    multa = (velocidade - 80) * 5
    print("\nMulta Aplicada!")
    print("Velocidade máxima permitida 80km/h")
    print(f"Valor à pagar: R${multa}")

else :
    print("\nVelocidade permitida. Boa viagem!")



###############################################
#Este programa é um sistema simples de registro 
#de compras que calcula o total a pagar 
#com base no código e na quantidade das 
#mercadorias. O usuário deve inserir o código 
#da mercadoria e a quantidade desejada. 
#O programa permite que o usuário continue 
#registrando mercadorias até que insira o código#0, que encerra a operação e exibe o total a pagar.
###############################################

apagar = 0  # Inicializa a variável que acumulará o valor total a pagar

while True:  # Inicia um loop infinito
    # Solicita ao usuário o código da mercadoria. O loop continua até que o usuário 
    # insira 0, que termina o programa.
    código = int(input("Código da mercadoria (0 para sair): "))  
    preço = 0  # Inicializa a variável preço para cada iteração do loop

    if código == 0:
        break  # Encerra o loop se o código inserido for 0
    elif código == 1:
        preço = 0.50  # Define o preço para o código 1
    elif código == 2:
        preço = 1.00  # Define o preço para o código 2
    elif código == 3:
        preço = 4.00  # Define o preço para o código 3
    elif código == 5:
        preço = 7.00  # Define o preço para o código 5
    elif código == 9:
        preço = 8.00  # Define o preço para o código 9
    else:
        print("Código inválido!")  # Exibe mensagem de erro para códigos não reconhecidos

    if preço != 0:
        # Solicita ao usuário a quantidade da mercadoria e calcula o total a pagar 
        # para a mercadoria atual, adicionando ao total acumulado.
        quantidade = int(input("Quantidade: "))  
        apagar = apagar + (preço * quantidade)

# Exibe o total acumulado a pagar no formato monetário.
print(f"Total a pagar R${apagar:8.2f}")  

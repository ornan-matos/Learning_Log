##############################################################################

# Programa para Correção de Teste de Múltipla Escolha

# Este programa corrige um teste de múltipla escolha com três questões,
# comparando as respostas fornecidas pelo usuário com o gabarito pré-definido.
# Ele calcula e exibe o total de pontos obtidos pelo aluno.

##############################################################################

pontos = 0   # Inicializa a variável 'pontos' para armazenar o total de acertos.
questao = 1  # Inicializa a variável 'questao' para controlar o número da questão atual.

while questao <= 3:  # Repete o bloco de código enquanto o número da questão for menor ou igual a 3.
    print("Insira a letra da resposta.\n")  # Solicita ao usuário que insira a resposta da questão.

    resposta = input(f"{questao} - Questão: ")  # Lê a resposta fornecida pelo usuário e armazena na variável 'resposta'.

    # Verifica se a resposta está correta para cada questão, considerando letras maiúsculas e minúsculas:
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1  # Se a resposta da questão 1 for "b" ou "B", adiciona 1 ponto.
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1  # Se a resposta da questão 2 for "a" ou "A", adiciona 1 ponto.
    if questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1  # Se a resposta da questão 3 for "d" ou "D", adiciona 1 ponto.

    questao = questao + 1  # Incrementa o número da questão para a próxima iteração do loop.

print(f"\nO aluno fez {pontos} ponto(s)")  # Exibe o total de pontos obtidos pelo aluno.



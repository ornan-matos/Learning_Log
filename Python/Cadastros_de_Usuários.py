# Lista para guardar os usuários cadastrados
usuarios = []

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    # Pede o nome do usuário
    nome = input("Digite o nome: ")
    # Pede o e-mail do usuário
    email = input("Digite o e-mail: ")
    # Pede a idade do usuário
    idade = input("Digite a idade: ")
    # Cria um dicionário com os dados do usuário
    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    # Adiciona o usuário na lista de usuários
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!\n")

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    print("\n--- Lista de Usuários ---")
    # Verifica se a lista está vazia
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        # Se tiver usuários, mostra cada um deles
        for idx, usuario in enumerate(usuarios):
            print(f"{idx+1}. Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")
        print()

# Função para buscar um usuário pelo nome
def buscar_usuario():
    print("\n--- Buscar Usuário ---")
    # Pede o nome para buscar
    nome_busca = input("Digite o nome para buscar: ")
    encontrado = False
    # Procura na lista de usuários
    for usuario in usuarios:
        # Compara ignorando maiúsculas e minúsculas
        if usuario["nome"].lower() == nome_busca.lower():
            print(f"Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}\n")
            encontrado = True
            break
    # Se não encontrar, avisa
    if not encontrado:
        print("Usuário não encontrado.\n")

# Função principal com o menu do sistema
def menu():
    while True:
        print("==== Menu ====")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Buscar Usuário")
        print("4 - Sair")
        # Pede para escolher uma opção
        opcao = input("Escolha uma opção: ")
        # Chama a função de acordo com a opção escolhida
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!\n")

# Iniciar o programa chamando a função do menu
menu()


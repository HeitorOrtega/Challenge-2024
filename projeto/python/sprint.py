# Função para cadastro de Clientes
def cadastrar_cliente():
    print("\nCadastro de Clientes\n")

    # Solicitação do CPF do cliente com um loop
    while True:
        cpf = input("CPF (11 caracteres): ")
        if len(cpf) == 11:
            break
        else:
            print("CPF deve conter 11 caracteres.")

    # Solicitação das informações do cliente
    nome = input("Nome: ")
    email = input("Email: ")
    idade = int(input("Idade: "))
    telefone = int(input("Telefone: "))
    
    # Criação do dicionário 
    cliente = {"Nome": nome, "Email": email, "Idade": idade, "CPF": cpf, "Telefone": telefone}
    print(f"\nCliente cadastrado com sucesso!\n{cliente}")

# Função para cadastro de veículos
def cadastrar_veiculo():
    print("\nCadastro de Veículos\n")
    modelo = input("Modelo do veículo: ")

    # Solicitação da placa com um loop
    while True:
        placa = input("Placa do veículo: ")
        if len(placa) == 7:
            break
        else:
            print("Placa deve conter 7 caracteres.")
            
    # Solicitação das informações do carro do cliente
    cor = input("Cor do veículo: ")
    veiculo = {"Modelo": modelo, "Placa": placa, "Cor": cor}
    print(f"\nVeículo cadastrado com sucesso!\n{veiculo}")

# Função para cadastro de oficinas
def cadastrar_oficina():
    print("\nCadastro de Oficinas\n")
    cep = input("CEP: ")
    endereco = input("Endereço: ")
    nome_oficina = input("Nome da Oficina: ")
    telefone_oficina = input("Telefone: ")
    oficina = {"CEP": cep, "Endereço": endereco, "Nome da Oficina": nome_oficina, "Telefone_oficina": telefone_oficina}
    print(f"\nOficina cadastrada com sucesso!\n{oficina}")

# Função de menu
def menu():
    while True:
        print("\nPortoConnect Car Atendimentos\n")
        print("---Menu Principal---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Veículo")
        print("3. Cadastrar Oficina")
        print("4. Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_veiculo()
        elif opcao == "3":
            cadastrar_oficina()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()

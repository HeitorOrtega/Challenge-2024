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

# Função para cadastro de Funcionários
def cadastrar_funcionario():
    print("\nCadastro de Oficinas\n")
    nome_funcionario = input("Nome: ")
    cargo = input("Cargo: ")
    data_contrata = input("Data de contratação: ")
    salario = input("Salário: ")
    setor = int(input("Setor: "))
    tempo_empresa = int(input("Tempo de empresa: "))
    funcionario = {"nome": nome_funcionario,"Cargo":cargo, "Data de contratação": data_contrata, "Salário": salario, "Setor": setor, "tempo_empresa": tempo_empresa}
    print(f"\nOficina cadastrada com sucesso!\n{funcionario}")

# Função para gerenciar estoque
def gerenciar_estoque():
    print("\nGerenciamento de Estoque de Peças\n")
    nome_peca = input("Nome da peça: ")
    quant = int(input("Quantidade disponível: "))
    preco = float(input("Preço unitário: R$ "))
    fornecedor = input("Fornecedor: ")
    estoque = {"Nome da Peça": nome_peca, "Quantidade Disponível": quant, "Preço Unitário": preco, "Fornecedor": fornecedor}
    print(f"\nEstoque de peças atualizado com sucesso!\n{estoque}")

# Função para agendar manunteção
def agendar_manutencao():

    # Solicitação da placa com um loop
    while True:
        placa = input("Placa do veículo: ")
        if len(placa) == 7:
            break
        else:
            print("Placa deve conter 7 caracteres.")

    print("\nAgendamento de Serviço de Manutenção\n")
    data = input("Data do serviço: ")
    horario = input("Horário do serviço: ")
    cliente = input("CPF: ")
    descricao_servico = input("Descrição do serviço: ")
    
    print("Serviço de manutenção agendado com sucesso!")
    print("Data:", data)
    print("Horário:", horario)
    print("Cliente:", cliente)
    print("Veículo:", placa)
    print("Descrição do serviço:", descricao_servico)

# Função Menu
def menu():
    while True:
        print("\n╭──────────────────────────────────╮")
        print("│   SmartConnect Car Atendimento   │")
        print("├──────────────────────────────────┤")
        print("│          Menu Principal          │")
        print("├──────────────────────────────────┤")
        print("│ 1. Cadastrar Clientes            │")
        print("│ 2. Cadastrar Veículos            │")
        print("│ 3. Cadastrar Oficinas            │")
        print("│ 4. Cadastrar Funcionários        │")
        print("│ 5. Agendar Serviço de Manutenção │")
        print("│ 6. Sair                          │")
        print("╰──────────────────────────────────╯")

        opcao = input("Digite sua opção: ")
        # Escohla do Usuário
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_veiculo()
        elif opcao == "3":
            cadastrar_oficina()
        elif opcao == "4":
            cadastrar_funcionario()
        elif opcao == "5":
            agendar_manutencao()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()

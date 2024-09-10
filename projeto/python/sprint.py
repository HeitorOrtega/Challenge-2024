from crud import *

# Listas simulando bancos de dados para armazenar os registros do sistema
clientes = []
veiculos = []
oficinas = []
funcionarios = []
estoque = []
servicos_agendados = []

# Função para exibir subtítulos com espaçamento
def exibir_subtitulos(texto):
    print(texto)
    print()

# Função para cadastrar clientes
def cadastrar_cliente():
    exibir_subtitulos("\n📋 **Cadastro de Clientes**\n")
    
    # Loop para garantir que o cadastro seja feito corretamente
    while True:
        try:
            # Solicita e valida o CPF
            cpf = input("Digite o CPF do cliente (11 dígitos): ")
            if len(cpf) != 11:
                exibir_subtitulos("⚠️ O CPF deve ter exatamente 11 dígitos.")
                continue
            
            # Verifica se o CPF já está cadastrado
            if any(cliente['CPF'] == cpf for cliente in clientes):
                exibir_subtitulos("⚠️ Este CPF já está cadastrado.")
                continue

            # Solicita os demais dados do cliente
            nome = input("Nome completo: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            telefone = input("Número de telefone: ")
            nome_usuario = input("Escolha um nome de usuário: ")

            # Verifica se o nome de usuário já está em uso
            if any(cliente['Usuário'] == nome_usuario for cliente in clientes):
                exibir_subtitulos("⚠️ Este nome de usuário já está em uso.")
                continue

            # Solicita e confirma a senha
            senha = input("Crie uma senha forte: ")
            senha_confirmada = input("Confirme a senha: ")

            # Verifica se as senhas coincidem
            if senha != senha_confirmada:
                exibir_subtitulos("⚠️ As senhas não coincidem.")
                continue

            # Cria o dicionário do cliente e o adiciona à lista
            cliente = {
                "Nome": nome, 
                "Email": email, 
                "Idade": idade, 
                "CPF": cpf, 
                "Telefone": telefone, 
                "Usuário": nome_usuario, 
                "Senha": senha
            }
            clientes.append(cliente)
            exibir_subtitulos(f"\n🎉 Cliente cadastrado com sucesso!\n{cliente}")
            break
        # Trata erros de conversão de tipo
        except ValueError as ve:
            exibir_subtitulos(f"⚠️ Erro: {ve}")
        # Trata qualquer outro tipo de exceção
        except Exception as e:
            exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para cadastrar veículos
def cadastrar_veiculo():
    exibir_subtitulos("\n🚗 **Cadastro de Veículos**\n")
    try:
        # Solicita os dados do veículo
        modelo = input("Modelo do veículo: ")

        # Loop para validar a placa do veículo
        while True:
            placa = input("Placa do veículo (7 caracteres): ")
            if len(placa) != 7:
                exibir_subtitulos("⚠️ A placa deve ter exatamente 7 caracteres.")
                continue
            # Verifica se a placa já está cadastrada
            elif any(veiculo['Placa'] == placa for veiculo in veiculos):
                exibir_subtitulos("⚠️ Esta placa já está cadastrada.")
                continue
            else:
                break

        # Solicita a cor do veículo e o cadastra na lista de veículos
        cor = input("Cor do veículo: ")
        veiculo = {"Modelo": modelo, "Placa": placa, "Cor": cor}
        veiculos.append(veiculo)
        exibir_subtitulos(f"\n🎉 Veículo cadastrado com sucesso!\n{veiculo}")
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para cadastrar oficinas
def cadastrar_oficina():
    exibir_subtitulos("\n🔧 **Cadastro de Oficinas**\n")
    try:
        # Solicita os dados da oficina
        cep = input("CEP: ")
        endereco = input("Endereço completo: ")
        nome_oficina = input("Nome da Oficina: ")
        telefone_oficina = input("Número de telefone: ")

        # Cria o dicionário da oficina e o adiciona à lista de oficinas
        oficina = {
            "CEP": cep, 
            "Endereço": endereco, 
            "Nome da Oficina": nome_oficina, 
            "Telefone": telefone_oficina
        }
        oficinas.append(oficina)
        exibir_subtitulos(f"\n🎉 Oficina cadastrada com sucesso!\n{oficina}")
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para cadastrar funcionários
def cadastrar_funcionario():
    exibir_subtitulos("\n👨‍💼 **Cadastro de Funcionários**\n")
    try:
        # Solicita os dados do funcionário
        nome_funcionario = input("Nome completo: ")
        cargo = input("Cargo: ")
        data_contrata = input("Data de contratação (DD/MM/AAAA): ")
        salario = float(input("Salário (R$): "))
        setor = int(input("Setor: "))
        tempo_empresa = int(input("Tempo de empresa (em anos): "))

        # Cria o dicionário do funcionário e o adiciona à lista de funcionários
        funcionario = {
            "Nome": nome_funcionario,
            "Cargo": cargo,
            "Data de contratação": data_contrata,
            "Salário": salario,
            "Setor": setor,
            "Tempo de empresa": tempo_empresa
        }
        funcionarios.append(funcionario)
        exibir_subtitulos(f"\n🎉 Funcionário cadastrado com sucesso!\n{funcionario}")
    # Trata erro de conversão de tipo
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro de valor: {ve}")
    # Trata qualquer outro tipo de exceção
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para gerenciar o estoque de peças
def gerenciar_estoque():
    exibir_subtitulos("\n🛠️ **Gerenciamento de Estoque de Peças**\n")
    try:
        # Solicita os dados da peça
        nome_peca = input("Nome da peça: ")
        quant = int(input("Quantidade disponível: "))
        preco = float(input("Preço unitário (R$): "))
        fornecedor = input("Fornecedor: ")

        # Cria o dicionário da peça e o adiciona ao estoque
        peca = {
            "Nome da Peça": nome_peca,
            "Quantidade Disponível": quant,
            "Preço Unitário": preco,
            "Fornecedor": fornecedor
        }
        estoque.append(peca)
        exibir_subtitulos(f"\n🎉 Estoque de peças atualizado com sucesso!\n{peca}")
    # Trata erro de conversão de tipo
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro de valor: {ve}")
    # Trata qualquer outro tipo de exceção
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")


# Função para agendar serviços de manutenção
def agendar_manutencao():
    exibir_subtitulos("\n🗓️ **Agendamento de Serviço de Manutenção**\n")
    try:
        # Valida a placa do veículo
        while True:
            placa = input("Placa do veículo (7 caracteres): ")
            if len(placa) != 7:
                exibir_subtitulos("⚠️ A placa deve ter exatamente 7 caracteres.")
                continue
            elif not any(veiculo['Placa'] == placa for veiculo in veiculos):
                exibir_subtitulos("⚠️ Veículo não encontrado. Verifique a placa e tente novamente.")
                continue
            else:
                break

        # Solicita e valida os demais dados do serviço
        data = input("Data do serviço (DD/MM/AAAA): ")
        horario = input("Horário do serviço: ")
        cpf = input("CPF do cliente: ")

        # Verifica se o CPF do cliente está cadastrado
        if not any(cliente['CPF'] == cpf for cliente in clientes):
            exibir_subtitulos("⚠️ CPF do cliente não encontrado. Verifique e tente novamente.")
            return

        descricao_servico = input("Descrição do serviço: ")

        # Cria o dicionário do serviço agendado e o adiciona à lista
        servico = {
            "Data": data,
            "Horário": horario,
            "CPF": cpf,
            "Placa": placa,
            "Descrição do Serviço": descricao_servico
        }
        servicos_agendados.append(servico)
        exibir_subtitulos(f"\n🎉 Serviço de manutenção agendado com sucesso!\n{servico}")
    # Trata erro de conversão de tipo
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro: {ve}")
    # Trata qualquer outro tipo de exceção
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para visualizar os serviços agendados
def mostrar_servicos_agendados():
    exibir_subtitulos("\n📅 **Serviços Agendados**\n")
     # Verifica se há serviços agendados na lista
    if not servicos_agendados:
        exibir_subtitulos("🚫 Nenhum serviço agendado no momento.")
    else:
         # Exibe todos os serviços agendados
        for servico in servicos_agendados:
            print(f"\n📆 Data: {servico['Data']}")
            print(f"⏰ Horário: {servico['Horário']}")
            print(f"🆔 CPF do Cliente: {servico['CPF']}")
            print(f"🚗 Placa do Veículo: {servico['Placa']}")
            print(f"📝 Descrição do Serviço: {servico['Descrição do Serviço']}")

# Função para o usuário fazer login na plataforma
def login():
    exibir_subtitulos("\n🔐 **Tela de Login**\n")
    while True:
        nome_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        
        # Verifica se o usuário e a senha são válidos
        usuario_valido = next((cliente for cliente in clientes if cliente['Usuário'] == nome_usuario and cliente['Senha'] == senha), None)
        
        if usuario_valido:
            # Solicita a placa e o modelo do veículo
            while True:
                placa = input("Placa do veículo (7 caracteres): ")
                if len(placa) != 7:
                    exibir_subtitulos("⚠️ A placa deve ter exatamente 7 caracteres.")
                elif not any(veiculo['Placa'] == placa for veiculo in veiculos):
                    exibir_subtitulos("⚠️ Placa não encontrada. Verifique e tente novamente.")
                else:
                    # Verifica se a placa pertence ao veículo do cliente
                    veiculo_associado = next((veiculo for veiculo in veiculos if veiculo['Placa'] == placa), None)
                    if veiculo_associado:
                        exibir_subtitulos(f"\n🔓 Login bem-sucedido! Bem-vindo(a), {usuario_valido['Nome']}!")
                        return True
                    else:
                        exibir_subtitulos("⚠️ A placa informada não corresponde a um veículo registrado.")
        else:
            exibir_subtitulos("⚠️ Nome de usuário ou senha incorretos. Tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ")
            if continuar.lower() != 's':
                break

# Função para exibir o menu principal com as opções de CRUD e outras funcionalidades
def menu():
    while True:
        print("\n╭────────────────────────────────────────────────╮")
        print("│           SmartConnect Car Atendimento         │")
        print("├────────────────────────────────────────────────┤")
        print("│                Menu Principal                  │")
        print("├────────────────────────────────────────────────┤")
        print("│ 1. Login                                       │")
        print("│ 2. Cadastrar Veiculos                          │")
        print("│ 3. Cadastrar Clientes                          │")
        print("│ 4. Cadastrar Oficinas                          │")
        print("│ 5. Cadastrar Funcionários                      │")
        print("│ 6. Gerenciar Estoque                           │")
        print("│ 8. Agendar Serviço de Manutenção               │")
        print("│ 9. Mostrar Serviços Agendados                  │")
        print("│ 0. Sair                                        │")
        print("╰────────────────────────────────────────────────╯")

        opcao = input("Escolha uma opção (1-9): ")

        match opcao:

            case "1":
                login()
            case "2":
                cadastrar_veiculo()
            case "3":
                cadastrar_cliente()
            case "4":
                cadastrar_oficina()
            case "5":
                cadastrar_funcionario()
            case "6":
                gerenciar_estoque()
            case "7":
                agendar_manutencao()
            case "8":
                mostrar_servicos_agendados()
            case  "0":
                print("👋 Saindo do sistema. Até a próxima!")
                break
            case _ :
                print("⚠️ Opção inválida. Por favor, escolha um número entre 1 e 9.")

menu()

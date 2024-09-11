import random
import string
from crud import *

# Listas simulando bancos de dados para armazenar os registros do sistema
clientes = []
veiculos = []
oficinas = []
funcionarios = []
estoque = []
servicos_agendados = []

# Função para gerar uma senha forte
def gerar_sugestao_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_sugerida = ''.join(random.choice(caracteres) for i in range(12))
    return senha_sugerida

# Função para exibir subtítulos com espaçamento
def exibir_subtitulos(texto):
    print(texto)
    print()

# Função para login
def login():
    exibir_subtitulos("\n🔒 **Login**\n")
    while True:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        # Verifica se o usuário e a senha correspondem a algum cliente cadastrado
        for cliente in clientes:
            if cliente["Usuário"] == usuario and cliente["Senha"] == senha:
                exibir_subtitulos(f"Bem-vindo, {cliente['Nome']}!")
                return True

        exibir_subtitulos("⚠️ Usuário ou senha inválidos. Tente novamente.")

# Função para cadastrar clientes
def cadastrar_cliente():
    exibir_subtitulos("\n📋 **Cadastro de Clientes**\n")
    
    while True:
        try:
            cpf = input("Digite o CPF do cliente (11 dígitos): ")
            if len(cpf) != 11:
                exibir_subtitulos("⚠️ O CPF deve ter exatamente 11 dígitos.")
                continue
            
            if any(cliente['CPF'] == cpf for cliente in clientes):
                exibir_subtitulos("⚠️ Este CPF já está cadastrado.")
                continue

            nome = input("Nome completo: ")
            email = input("Email: ")
            idade = int(input("Idade: "))
            telefone = input("Número de telefone: ")
            nome_usuario = input("Escolha um nome de usuário: ")

            if any(cliente['Usuário'] == nome_usuario for cliente in clientes):
                exibir_subtitulos("⚠️ Este nome de usuário já está em uso.")
                continue

            # Pergunta se o usuário quer uma sugestão de senha forte
            senha = input("Crie uma senha forte ou digite 's' para sugerir uma: ")
            if senha.lower() == 's':
                senha = gerar_sugestao_senha()
                print(f"Sugestão de senha: {senha}")
            senha_confirmada = input("Confirme a senha: ")

            if senha != senha_confirmada:
                exibir_subtitulos("⚠️ As senhas não coincidem.")
                continue

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
        except ValueError as ve:
            exibir_subtitulos(f"⚠️ Erro: {ve}")
        except Exception as e:
            exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para cadastrar veículos
def cadastrar_veiculo():
    exibir_subtitulos("\n🚗 **Cadastro de Veículos**\n")
    try:
        modelo = input("Modelo do veículo: ")

        while True:
            placa = input("Placa do veículo (7 caracteres): ")
            if len(placa) != 7:
                exibir_subtitulos("⚠️ A placa deve ter exatamente 7 caracteres.")
                continue
            elif any(veiculo['Placa'] == placa for veiculo in veiculos):
                exibir_subtitulos("⚠️ Esta placa já está cadastrada.")
                continue
            else:
                break

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
        cep = input("CEP: ")
        endereco = input("Endereço completo: ")
        nome_oficina = input("Nome da Oficina: ")
        telefone_oficina = input("Número de telefone: ")

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
        nome_funcionario = input("Nome completo: ")
        cargo = input("Cargo: ")
        data_contrata = input("Data de contratação (DD/MM/AAAA): ")
        salario = float(input("Salário (R$): "))
        setor = input("Setor: ")
        tempo_empresa = int(input("Tempo de empresa (em anos): "))

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
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro de valor: {ve}")
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para gerenciar o estoque de peças
def gerenciar_estoque():
    exibir_subtitulos("\n🛠️ **Gerenciamento de Estoque de Peças**\n")
    try:
        nome_peca = input("Nome da peça: ")
        quant = int(input("Quantidade disponível: "))
        preco = float(input("Preço unitário (R$): "))
        fornecedor = input("Fornecedor: ")

        peca = {
            "Nome da Peça": nome_peca,
            "Quantidade Disponível": quant,
            "Preço Unitário": preco,
            "Fornecedor": fornecedor
        }
        estoque.append(peca)
        exibir_subtitulos(f"\n🎉 Estoque de peças atualizado com sucesso!\n{peca}")
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro de valor: {ve}")
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para agendar serviços de manutenção
def agendar_manutencao():
    exibir_subtitulos("\n🗓️ **Agendamento de Serviço de Manutenção**\n")
    try:
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

        data = input("Data do serviço (DD/MM/AAAA): ")
        horario = input("Horário do serviço: ")
        cpf = input("CPF do cliente: ")

        if not any(cliente['CPF'] == cpf for cliente in clientes):
            exibir_subtitulos("⚠️ CPF do cliente não encontrado. Verifique e tente novamente.")
            return

        descricao_servico = input("Descrição do serviço: ")

        servico = {
            "Data": data,
            "Horário": horario,
            "CPF": cpf,
            "Placa": placa,
            "Descrição do Serviço": descricao_servico
        }
        servicos_agendados.append(servico)
        exibir_subtitulos(f"\n🎉 Serviço de manutenção agendado com sucesso!\n{servico}")
    except ValueError as ve:
        exibir_subtitulos(f"⚠️ Erro: {ve}")
    except Exception as e:
        exibir_subtitulos(f"⚠️ Ocorreu um erro inesperado: {e}")

# Função para mostrar serviços agendados
def mostrar_servicos_agendados():
    exibir_subtitulos("\n📅 **Serviços Agendados**\n")
    if not servicos_agendados:
        exibir_subtitulos("Não há serviços agendados.")
    for servico in servicos_agendados:
        print(servico)

# Função para exibir o menu principal com as opções de CRUD e outras funcionalidades
def menu():
    while True:
        print("\n╭────────────────────────────────────────────────╮")
        print("│           SmartConnect Car Atendimento         │")
        print("├────────────────────────────────────────────────┤")
        print("│                Menu Principal                  │")
        print("├────────────────────────────────────────────────┤")
        print("│ 1. Login                                       │")
        print("│ 2. Cadastrar Clientes                          │")
        print("│ 3. Cadastrar Veiculos                          │")
        print("│ 4. Cadastrar Oficinas                          │")
        print("│ 5. Cadastrar Funcionários                      │")
        print("│ 6. Gerenciar Estoque                           │")
        print("│ 7. Agendar Serviço de Manutenção               │")
        print("│ 8. Mostrar Serviços Agendados                  │")
        print("│ 0. Sair                                        │")
        print("╰────────────────────────────────────────────────╯")

        opcao = input("Escolha uma opção (1-9): ")

        match opcao:

            case "1":
                login()
            case "2":
                cadastrar_cliente()
            case "3":
                cadastrar_veiculo()
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


if __name__ == "__main__":
    menu()

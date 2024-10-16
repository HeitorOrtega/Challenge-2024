import cx_Oracle
import datetime as dt

# Conexão com o banco de dados
def conexao():
    usuario = "rm557825"
    senha = "170506"
    db = "oracle.fiap.com.br:1521/orcl"

    # Criar a conexão
    connection = cx_Oracle.connect(
        user=usuario,
        password=senha,
        dsn=db
    )
    return connection

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Dados")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_gerenciamento()
        elif opcao == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def menu_gerenciamento():
    while True:
        print("\nMenu de Gerenciamento:")
        print("1. Inserir Dados")
        print("2. Alterar Dados")
        print("3. Excluir Dados")
        print("4. Consultar Dados")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_dados()
        elif opcao == '2':
            alterar_dados()
        elif opcao == '3':
            excluir_dados()
        elif opcao == '4':
            consultar_dados()
        elif opcao == '5':
            break
        else:
            print("Opção inválida! Tente novamente.")

# Funções CRUD para clientes
def inserir_cliente(nome_usuario,nome,email,idade,cpf,telefone,senha):
    connection = conexao()
    cur = connection.cursor()

    nome_usuario = input("Digite o nome de usuário: ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    idade = input("Digite a idade: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")
    senha = input("Digite a senha: ")

    cur.execute("INSERT INTO CLIENTES (nome_usuario, nome, email, idade, cpf, telefone, senha, data_cadastro) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)", 
                (nome_usuario, nome, email, idade, cpf, telefone, senha, dt.datetime.now()))
    connection.commit()

    print("Cliente inserido com sucesso!")

    cur.close()
    connection.close()

def alterar_cliente():
    connection = conexao()
    cur = connection.cursor()

    id_cliente = input("Digite o ID do cliente a ser alterado: ")
    novo_nome = input("Digite o novo nome: ")

    cur.execute("UPDATE CLIENTES SET nome = :1 WHERE id = :2", (novo_nome, id_cliente))
    connection.commit()

    print("Cliente alterado com sucesso!")

    cur.close()
    connection.close()

def excluir_cliente():
    connection = conexao()
    cur = connection.cursor()

    id_cliente = input("Digite o ID do cliente a ser excluído: ")

    cur.execute("DELETE FROM CLIENTES WHERE id = :1", (id_cliente,))
    connection.commit()

    print("Cliente excluído com sucesso!")

    cur.close()
    connection.close()

def consultar_clientes():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM CLIENTES")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Funções CRUD para veículos
def inserir_veiculo():
    connection = conexao()
    cur = connection.cursor()

    nome_cliente = input("Digite o nome do cliente: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    placa = input("Digite a placa do veículo: ")
    descricao_problema = input("Digite a descrição do problema: ")

    cur.execute("INSERT INTO VEICULOS (nome_cliente, modelo, ano, placa, descricao_problema, data) VALUES (:1, :2, :3, :4, :5, :6)", 
                (nome_cliente, modelo, ano, placa, descricao_problema, dt.datetime.now()))
    connection.commit()

    print("Veículo inserido com sucesso!")

    cur.close()
    connection.close()

def alterar_veiculo():
    connection = conexao()
    cur = connection.cursor()

    id_veiculo = input("Digite o ID do veículo a ser alterado: ")
    novo_modelo = input("Digite o novo modelo: ")

    cur.execute("UPDATE VEICULOS SET modelo = :1 WHERE id = :2", (novo_modelo, id_veiculo))
    connection.commit()

    print("Veículo alterado com sucesso!")

    cur.close()
    connection.close()

def excluir_veiculo():
    connection = conexao()
    cur = connection.cursor()

    id_veiculo = input("Digite o ID do veículo a ser excluído: ")

    cur.execute("DELETE FROM VEICULOS WHERE id = :1", (id_veiculo,))
    connection.commit()

    print("Veículo excluído com sucesso!")

    cur.close()
    connection.close()

def consultar_veiculos():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM VEICULOS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Funções CRUD para oficinas
def inserir_oficina():
    connection = conexao()
    cur = connection.cursor()

    cep = input("Digite o CEP da oficina: ")
    endereco = input("Digite o endereço da oficina: ")
    nome_oficina = input("Digite o nome da oficina: ")
    telefone_oficina = input("Digite o telefone da oficina: ")

    cur.execute("INSERT INTO OFICINAS (cep, endereco, nome_oficina, telefone_oficina) VALUES (:1, :2, :3, :4)", 
                (cep, endereco, nome_oficina, telefone_oficina))
    connection.commit()

    print("Oficina inserida com sucesso!")

    cur.close()
    connection.close()

def alterar_oficina():
    connection = conexao()
    cur = connection.cursor()

    id_oficina = input("Digite o ID da oficina a ser alterada: ")
    novo_nome = input("Digite o novo nome da oficina: ")

    cur.execute("UPDATE OFICINAS SET nome_oficina = :1 WHERE id = :2", (novo_nome, id_oficina))
    connection.commit()

    print("Oficina alterada com sucesso!")

    cur.close()
    connection.close()

def excluir_oficina():
    connection = conexao()
    cur = connection.cursor()

    id_oficina = input("Digite o ID da oficina a ser excluída: ")

    cur.execute("DELETE FROM OFICINAS WHERE id = :1", (id_oficina,))
    connection.commit()

    print("Oficina excluída com sucesso!")

    cur.close()
    connection.close()

def consultar_oficinas():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM OFICINAS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Funções CRUD para funcionários
def inserir_funcionario():
    connection = conexao()
    cur = connection.cursor()

    nome_funcionario = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo: ")
    data_contrata = input("Digite a data de contratação (YYYY-MM-DD): ")
    salario = input("Digite o salário: ")
    setor = input("Digite o setor: ")
    tempo_empresa = input("Digite o tempo de empresa: ")

    cur.execute("INSERT INTO FUNCIONARIOS (nome_funcionario, cargo, data_contrata, salario, setor, tempo_empresa) VALUES (:1, :2, :3, :4, :5, :6)", 
                (nome_funcionario, cargo, data_contrata, salario, setor, tempo_empresa))
    connection.commit()

    print("Funcionário inserido com sucesso!")

    cur.close()
    connection.close()

def alterar_funcionario():
    connection = conexao()
    cur = connection.cursor()

    id_funcionario = input("Digite o ID do funcionário a ser alterado: ")
    novo_nome = input("Digite o novo nome do funcionário: ")

    cur.execute("UPDATE FUNCIONARIOS SET nome_funcionario = :1 WHERE id = :2", (novo_nome, id_funcionario))
    connection.commit()

    print("Funcionário alterado com sucesso!")

    cur.close()
    connection.close()

def excluir_funcionario():
    connection = conexao()
    cur = connection.cursor()

    id_funcionario = input("Digite o ID do funcionário a ser excluído: ")

    cur.execute("DELETE FROM FUNCIONARIOS WHERE id = :1", (id_funcionario,))
    connection.commit()

    print("Funcionário excluído com sucesso!")

    cur.close()
    connection.close()

def consultar_funcionarios():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM FUNCIONARIOS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Funções CRUD para estoque
def inserir_estoque():
    connection = conexao()
    cur = connection.cursor()

    nome_produto = input("Digite o nome do produto: ")
    quantidade = input("Digite a quantidade: ")
    valor_unitario = input("Digite o valor unitário: ")

    cur.execute("INSERT INTO ESTOQUE (nome_produto, quantidade, valor_unitario) VALUES (:1, :2, :3)", 
                (nome_produto, quantidade, valor_unitario))
    connection.commit()

    print("Produto inserido no estoque com sucesso!")

    cur.close()
    connection.close()

def alterar_estoque():
    connection = conexao()
    cur = connection.cursor()

    id_produto = input("Digite o ID do produto a ser alterado: ")
    nova_quantidade = input("Digite a nova quantidade: ")

    cur.execute("UPDATE ESTOQUE SET quantidade = :1 WHERE id = :2", (nova_quantidade, id_produto))
    connection.commit()

    print("Produto alterado no estoque com sucesso!")

    cur.close()
    connection.close()

def excluir_estoque():
    connection = conexao()
    cur = connection.cursor()

    id_produto = input("Digite o ID do produto a ser excluído: ")

    cur.execute("DELETE FROM ESTOQUE WHERE id = :1", (id_produto,))
    connection.commit()

    print("Produto excluído do estoque com sucesso!")

    cur.close()
    connection.close()

def consultar_estoque():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM ESTOQUE")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Funções CRUD para serviços agendados
def inserir_servico():
    connection = conexao()
    cur = connection.cursor()

    id_cliente = input("Digite o ID do cliente: ")
    id_veiculo = input("Digite o ID do veículo: ")
    id_oficina = input("Digite o ID da oficina: ")
    data_servico = input("Digite a data do serviço (YYYY-MM-DD): ")
    descricao_servico = input("Digite a descrição do serviço: ")

    cur.execute("INSERT INTO SERVIÇOS_AGENDADOS (id_cliente, id_veiculo, id_oficina, data_servico, descricao_servico) VALUES (:1, :2, :3, :4, :5)", 
                (id_cliente, id_veiculo, id_oficina, data_servico, descricao_servico))
    connection.commit()

    print("Serviço agendado com sucesso!")

    cur.close()
    connection.close()

def alterar_servico():
    connection = conexao()
    cur = connection.cursor()

    id_servico = input("Digite o ID do serviço a ser alterado: ")
    nova_descricao = input("Digite a nova descrição do serviço: ")

    cur.execute("UPDATE SERVIÇOS_AGENDADOS SET descricao_servico = :1 WHERE id = :2", (nova_descricao, id_servico))
    connection.commit()

    print("Serviço alterado com sucesso!")

    cur.close()
    connection.close()

def excluir_servico():
    connection = conexao()
    cur = connection.cursor()

    id_servico = input("Digite o ID do serviço a ser excluído: ")

    cur.execute("DELETE FROM SERVIÇOS_AGENDADOS WHERE id = :1", (id_servico,))
    connection.commit()

    print("Serviço excluído com sucesso!")

    cur.close()
    connection.close()

def consultar_servicos():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM SERVIÇOS_AGENDADOS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta:")
    for row in resultados:
        print(row)

    cur.close()
    connection.close()

# Função principal para inserir, alterar, excluir e consultar dados
def inserir_dados():
    print("1. Inserir Cliente")
    print("2. Inserir Veículo")
    print("3. Inserir Oficina")
    print("4. Inserir Funcionário")
    print("5. Inserir Produto no Estoque")
    print("6. Inserir Serviço Agendado")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_cliente()
    elif opcao == '2':
        inserir_veiculo()
    elif opcao == '3':
        inserir_oficina()
    elif opcao == '4':
        inserir_funcionario()
    elif opcao == '5':
        inserir_estoque()
    elif opcao == '6':
        inserir_servico()
    else:
        print("Opção inválida! Tente novamente.")

def alterar_dados():
    print("1. Alterar Cliente")
    print("2. Alterar Veículo")
    print("3. Alterar Oficina")
    print("4. Alterar Funcionário")
    print("5. Alterar Produto no Estoque")
    print("6. Alterar Serviço Agendado")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        alterar_cliente()
    elif opcao == '2':
        alterar_veiculo()
    elif opcao == '3':
        alterar_oficina()
    elif opcao == '4':
        alterar_funcionario()
    elif opcao == '5':
        alterar_estoque()
    elif opcao == '6':
        alterar_servico()
    else:
        print("Opção inválida! Tente novamente.")

def excluir_dados():
    print("1. Excluir Cliente")
    print("2. Excluir Veículo")
    print("3. Excluir Oficina")
    print("4. Excluir Funcionário")
    print("5. Excluir Produto do Estoque")
    print("6. Excluir Serviço Agendado")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        excluir_cliente()
    elif opcao == '2':
        excluir_veiculo()
    elif opcao == '3':
        excluir_oficina()
    elif opcao == '4':
        excluir_funcionario()
    elif opcao == '5':
        excluir_estoque()
    elif opcao == '6':
        excluir_servico()
    else:
        print("Opção inválida! Tente novamente.")

def consultar_dados():
    print("1. Consultar Clientes")
    print("2. Consultar Veículos")
    print("3. Consultar Oficinas")
    print("4. Consultar Funcionários")
    print("5. Consultar Produtos em Estoque")
    print("6. Consultar Serviços Agendados")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        consultar_clientes()
    elif opcao == '2':
        consultar_veiculos()
    elif opcao == '3':
        consultar_oficinas()
    elif opcao == '4':
        consultar_funcionarios()
    elif opcao == '5':
        consultar_estoque()
    elif opcao == '6':
        consultar_servicos()
    else:
        print("Opção inválida! Tente novamente.")

# Iniciar o programa
if __name__ == "__main__":
    menu_principal()

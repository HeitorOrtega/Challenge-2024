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
def inserir_cliente():
    connection = conexao()
    cur = connection.cursor()

    nome_usuario = input("Digite o nome de usuário: ")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    idade = input("Digite a idade: ")
    cpf = input("Digite o CPF: ")
    telefone = input("Digite o telefone: ")
    senha = input("Digite a senha: ")

    cur.execute("INSERT INTO CLIENTES (nome_usuario, nome, email, idade, cpf, telefone, senha, data_cadastro) "
                "VALUES (:1, :2, :3, :4, :5, :6, :7, :8)", 
                (nome_usuario, nome, email, idade, cpf, telefone, senha, dt.datetime.now()))
    connection.commit()

    print("Cliente inserido com sucesso!")

    cur.close()
    connection.close()

def alterar_cliente():
    connection = conexao()
    cur = connection.cursor()

    try:
        # Garantindo que o ID do cliente seja um número inteiro
        id_cliente = int(input("Digite o ID do cliente a ser alterado: "))

        print("Selecione o que deseja alterar:")
        print("1. Nome")
        print("2. Email")
        print("3. Idade")
        print("4. CPF")
        print("5. Telefone")
        print("6. Senha")
        opcao = input("Escolha a opção que deseja alterar: ")

        if opcao == '1':
            novo_nome = input("Digite o novo nome: ")
            cur.execute("UPDATE CLIENTES SET nome = :1 WHERE id = :2", (novo_nome, id_cliente))
        
        elif opcao == '2':
            novo_email = input("Digite o novo email: ")
            cur.execute("UPDATE CLIENTES SET email = :1 WHERE id = :2", (novo_email, id_cliente))
        
        elif opcao == '3':
            nova_idade = input("Digite a nova idade: ")
            cur.execute("UPDATE CLIENTES SET idade = :1 WHERE id = :2", (nova_idade, id_cliente))
        
        elif opcao == '4':
            novo_cpf = input("Digite o novo CPF: ")
            cur.execute("UPDATE CLIENTES SET cpf = :1 WHERE id = :2", (novo_cpf, id_cliente))
        
        elif opcao == '5':
            novo_telefone = input("Digite o novo telefone: ")
            cur.execute("UPDATE CLIENTES SET telefone = :1 WHERE id = :2", (novo_telefone, id_cliente))
        
        elif opcao == '6':
            nova_senha = input("Digite a nova senha: ")
            cur.execute("UPDATE CLIENTES SET senha = :1 WHERE id = :2", (nova_senha, id_cliente))
        
        else:
            print("Opção inválida! Tente novamente.")
            return

        connection.commit()
        print("Cliente alterado com sucesso!")

    except ValueError:
        print("Erro: O ID do cliente deve ser um número inteiro.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao atualizar o banco de dados: {e}")
    finally:
        cur.close()
        connection.close()


def excluir_cliente():
    connection = conexao()
    cur = connection.cursor()

    try:
      
        id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
        confirmacao = input(f"Você realmente deseja excluir o cliente com ID {id_cliente}? (s/n): ")
        if confirmacao.lower() != 's':
            print("Exclusão cancelada.")
            return

        cur.execute("DELETE FROM CLIENTES WHERE id = :1", (id_cliente,))
        connection.commit()

        if cur.rowcount > 0:
            print("Cliente excluído com sucesso!")
        else:
            print("Nenhum cliente encontrado com esse ID.")

    except ValueError:
        print("Erro: O ID do cliente deve ser um número inteiro.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao excluir o cliente no banco de dados: {e}")
    finally:
        cur.close()
        connection.close()


def consultar_clientes():
    connection = conexao()
    cur = connection.cursor()

    try:
        cur.execute("SELECT * FROM CLIENTES")
        resultados = cur.fetchall()

        # Obtendo os nomes das colunas
        colunas = [col[0] for col in cur.description]

        print("\nResultados da Consulta:")
        print(f"{' | '.join(colunas)}")  
        print("-" * 50)  
        for row in resultados:
            print(f"{' | '.join(map(str, row))}")  

    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao consultar os clientes no banco de dados: {e}")
    finally:
        cur.close()
        connection.close()

# Funções CRUD para veículos
def inserir_veiculo():
    connection = conexao()
    cur = connection.cursor()

   
    nome_cliente = input("Digite o nome do cliente: ")
    cur.execute("SELECT id_cliente FROM CLIENTES WHERE nome = :1", (nome_cliente,))
    id_cliente = cur.fetchone()

    # Verificando se o cliente existe no banco de dados
    if id_cliente is None:
        print("Cliente não encontrado!")
        return
    
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    placa = input("Digite a placa do veículo: ")
    descricao_problema = input("Digite a descrição do problema: ")

    cur.execute("INSERT INTO VEICULOS (modelo, ano, placa, descricao_problema, data_entrada, id_cliente) "
                "VALUES (:1, :2, :3, :4, :5, :6)", 
                (modelo, ano, placa, descricao_problema, dt.datetime.now(), id_cliente[0]))
    connection.commit()

    print("Veículo inserido com sucesso!")


    cur.close()
    connection.close()

def alterar_veiculo():
    connection = conexao()
    cur = connection.cursor()

    id_veiculo = input("Digite o ID do veículo a ser alterado: ")

    # Exibir opções de atributos a serem alterados
    print("Escolha o que deseja alterar:")
    print("1. Modelo")
    print("2. Ano")
    print("3. Placa")
    print("4. Descrição do Problema")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        novo_modelo = input("Digite o novo modelo: ")
        cur.execute("UPDATE VEICULOS SET modelo = :1 WHERE id = :2", (novo_modelo, id_veiculo))

    elif opcao == '2':
        novo_ano = input("Digite o novo ano: ")
        cur.execute("UPDATE VEICULOS SET ano = :1 WHERE id = :2", (novo_ano, id_veiculo))

    elif opcao == '3':
        nova_placa = input("Digite a nova placa: ")
        cur.execute("UPDATE VEICULOS SET placa = :1 WHERE id = :2", (nova_placa, id_veiculo))

    elif opcao == '4':
        nova_descricao_problema = input("Digite a nova descrição do problema: ")
        cur.execute("UPDATE VEICULOS SET descricao_problema = :1 WHERE id = :2", (nova_descricao_problema, id_veiculo))

    else:
        print("Opção inválida! Tente novamente.")
        cur.close()
        connection.close()
        return

    connection.commit()
    print("Veículo alterado com sucesso!")

    cur.close()
    connection.close()

def excluir_veiculo():
    connection = conexao()
    cur = connection.cursor()

    id_veiculo = input("Digite o ID do veículo a ser excluído: ")
    cur.execute("SELECT * FROM VEICULOS WHERE id = :1", (id_veiculo,))
    resultado = cur.fetchone()

    if resultado:
        cur.execute("DELETE FROM VEICULOS WHERE id = :1", (id_veiculo,))
        connection.commit()
        print("Veículo excluído com sucesso!")
    else:
        print("Veículo com ID especificado não encontrado.")

    cur.close()
    connection.close()


def consultar_veiculos():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT * FROM VEICULOS")
    resultados = cur.fetchall()

    colunas = [desc[0] for desc in cur.description]

    print("\nResultados da Consulta de Veículos:")
    print(f"{' | '.join(colunas)}")  
    print("-" * 50)  #

    for row in resultados:
        print(f"{' | '.join(map(str, row))}") 

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

    cur.execute("INSERT INTO OFICINAS (cep, endereco, nome_oficina, telefone_oficina) "
                "VALUES (:1, :2, :3, :4)", 
                (cep, endereco, nome_oficina, telefone_oficina))
    connection.commit()

    print("Oficina inserida com sucesso!")

    cur.close()
    connection.close()

def alterar_oficina():
    connection = conexao()
    cur = connection.cursor()

    id_oficina = input("Digite o ID da oficina a ser alterada: ")
    
    # Exibir opções de campos para alterar
    print("Quais dados você deseja alterar?")
    print("1. Nome da Oficina")
    print("2. Endereço")
    print("3. Telefone")
    
    opcao = input("Escolha a opção (1-3): ")

    if opcao == '1':
        novo_nome = input("Digite o novo nome da oficina: ")
        cur.execute("UPDATE OFICINAS SET nome_oficina = :1 WHERE id = :2", (novo_nome, id_oficina))
    elif opcao == '2':
        novo_endereco = input("Digite o novo endereço da oficina: ")
        cur.execute("UPDATE OFICINAS SET endereco = :1 WHERE id = :2", (novo_endereco, id_oficina))
    elif opcao == '3':
        novo_telefone = input("Digite o novo telefone da oficina: ")
        cur.execute("UPDATE OFICINAS SET telefone_oficina = :1 WHERE id = :2", (novo_telefone, id_oficina))
    else:
        print("Opção inválida! Nenhuma alteração foi feita.")
        cur.close()
        connection.close()
        return

    connection.commit()
    print("Oficina alterada com sucesso!")

    cur.close()
    connection.close()


def excluir_oficina():
    connection = conexao()
    cur = connection.cursor()

    id_oficina = input("Digite o ID da oficina a ser excluída: ")

    # Verificar se a oficina existe
    cur.execute("SELECT COUNT(*) FROM OFICINAS WHERE id = :1", (id_oficina,))
    existe = cur.fetchone()[0]

    if existe == 0:
        print("Nenhuma oficina encontrada com esse ID. Nenhuma exclusão realizada.")
    else:
        cur.execute("DELETE FROM OFICINAS WHERE id = :1", (id_oficina,))
        connection.commit()
        print("Oficina excluída com sucesso!")

    cur.close()
    connection.close()


def consultar_oficinas():
    connection = conexao()
    cur = connection.cursor()

    # Executar a consulta
    cur.execute("SELECT id, cep, endereco, nome_oficina, telefone_oficina FROM OFICINAS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta de Oficinas:")
    
    # Verificar se há resultados
    if not resultados:
        print("Nenhuma oficina encontrada.")
    else:

        print(f"{'ID':<5} {'CEP':<10} {'Endereço':<30} {'Nome da Oficina':<25} {'Telefone':<15}")
        print("-" * 95)  # Linha de separação
        for row in resultados:
            print(f"{row[0]:<5} {row[1]:<10} {row[2]:<30} {row[3]:<25} {row[4]:<15}")

    cur.close()
    connection.close()


# Funções CRUD para funcionários
def inserir_funcionario():
    connection = conexao()
    cur = connection.cursor()

    nome_funcionario = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo: ")
    
    # Solicitando a data de contratação e convertendo para o formato de data do Oracle
    data_contrata = input("Digite a data de contratação (YYYY-MM-DD): ")
    data_contrata_formatada = dt.datetime.strptime(data_contrata, '%Y-%m-%d').date()
    
    salario = float(input("Digite o salário: "))  # Garantindo que o salário seja um valor numérico
    setor = input("Digite o setor: ")
    tempo_empresa = int(input("Digite o tempo de empresa (em anos): "))  # Garantindo que o tempo seja um número inteiro

    cur.execute("""
        INSERT INTO FUNCIONARIOS (nome_funcionario, cargo, data_contrata, salario, setor, tempo_empresa) 
        VALUES (:1, :2, :3, :4, :5, :6)
    """, 
    (nome_funcionario, cargo, data_contrata_formatada, salario, setor, tempo_empresa))
    
    connection.commit()

    print("Funcionário inserido com sucesso!")


    cur.close()
    connection.close()

def alterar_funcionario():
    connection = conexao()
    cur = connection.cursor()

    id_funcionario = input("Digite o ID do funcionário a ser alterado: ")

    # Verificar se o funcionário existe antes de tentar atualizar
    cur.execute("SELECT * FROM FUNCIONARIOS WHERE id = :1", (id_funcionario,))
    funcionario = cur.fetchone()

    if funcionario is None:
        print("Funcionário não encontrado.")
        cur.close()
        connection.close()
        return

    novo_nome = input("Digite o novo nome do funcionário: ")
    novo_cargo = input("Digite o novo cargo do funcionário: ")
    novo_salario = input("Digite o novo salário do funcionário: ")
    novo_setor = input("Digite o novo setor do funcionário: ")
    novo_tempo_empresa = input("Digite o novo tempo de empresa do funcionário: ")

    cur.execute("""
        UPDATE FUNCIONARIOS
        SET nome_funcionario = :1, cargo = :2, salario = :3, setor = :4, tempo_empresa = :5
        WHERE id = :6
    """, (novo_nome, novo_cargo, novo_salario, novo_setor, novo_tempo_empresa, id_funcionario))

    connection.commit()

    print("Funcionário alterado com sucesso!")

    cur.close()
    connection.close()


def excluir_funcionario():
    connection = conexao()
    cur = connection.cursor()

    id_funcionario = input("Digite o ID do funcionário a ser excluído: ")

    # Verificar se o funcionário existe antes de tentar excluir
    cur.execute("SELECT * FROM FUNCIONARIOS WHERE id = :1", (id_funcionario,))
    funcionario = cur.fetchone()

    if funcionario is None:
        print("Funcionário não encontrado.")
    else:
        cur.execute("DELETE FROM FUNCIONARIOS WHERE id = :1", (id_funcionario,))
        connection.commit()
        print("Funcionário excluído com sucesso!")

    cur.close()
    connection.close()


def consultar_funcionarios():
    connection = conexao()
    cur = connection.cursor()

    cur.execute("SELECT id, nome_funcionario, cargo, data_contrata, salario, setor, tempo_empresa FROM FUNCIONARIOS")
    resultados = cur.fetchall()

    print("\nResultados da Consulta de Funcionários:")
    print(f"{'ID':<5} {'Nome':<20} {'Cargo':<15} {'Data Contrata':<12} {'Salário':<10} {'Setor':<10} {'Tempo de Empresa':<15}")
    print("-" * 95)

    for row in resultados:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<12} {row[4]:<10} {row[5]:<10} {row[6]:<15}")

    cur.close()
    connection.close()


# Funções CRUD para estoque
def inserir_estoque():
    connection = conexao()
    cur = connection.cursor()

    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    valor_unitario = float(input("Digite o valor unitário: "))

    cur.execute("""
        INSERT INTO ESTOQUE (nome_produto, quantidade, valor_unitario) 
        VALUES (:1, :2, :3)
    """, 
    (nome_produto, quantidade, valor_unitario))
    
    connection.commit()

    print("Produto inserido no estoque com sucesso!")

    cur.close()
    connection.close()

def alterar_estoque():
    connection = conexao()
    cur = connection.cursor()

    id_produto = input("Digite o ID do produto a ser alterado: ")
    novo_nome_produto = input("Digite o novo nome do produto (deixe em branco para não alterar): ")
    nova_quantidade = input("Digite a nova quantidade (deixe em branco para não alterar): ")
    novo_valor_unitario = input("Digite o novo valor unitário (deixe em branco para não alterar): ")

    campos_atualizacao = []
    valores = []

    if novo_nome_produto:
        campos_atualizacao.append("nome_produto = :1")
        valores.append(novo_nome_produto)

    if nova_quantidade:
        campos_atualizacao.append("quantidade = :2")
        valores.append(nova_quantidade)

    if novo_valor_unitario:
        campos_atualizacao.append("valor_unitario = :3")
        valores.append(novo_valor_unitario)

    # Certifique-se de que pelo menos um campo foi alterado
    if campos_atualizacao:
        set_clause = ", ".join(campos_atualizacao)
        valores.append(id_produto)
        cur.execute(f"UPDATE ESTOQUE SET {set_clause} WHERE id = :{len(valores)}", tuple(valores))
        connection.commit()
        print("Produto alterado no estoque com sucesso!")
    else:
        print("Nenhuma alteração foi realizada.")

    cur.close()
    connection.close()


def excluir_estoque():
    connection = conexao()
    cur = connection.cursor()

    id_produto = input("Digite o ID do produto a ser excluído: ")

    # Verificar se o produto existe antes de excluí-lo
    cur.execute("SELECT COUNT(*) FROM ESTOQUE WHERE id = :1", (id_produto,))
    if cur.fetchone()[0] == 0:
        print("Produto não encontrado. Nenhuma exclusão realizada.")
    else:
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
    print("{:<5} {:<20} {:<15} {:<15}".format("ID", "Nome do Produto", "Quantidade", "Valor Unitário"))
    print("-" * 60)
    
    for row in resultados:
        id_produto, nome_produto, quantidade, valor_unitario = row
        print("{:<5} {:<20} {:<15} {:<15}".format(id_produto, nome_produto, quantidade, valor_unitario))

    cur.close()
    connection.close()


# Funções CRUD para serviços agendados
def inserir_servico():
    connection = conexao()
    cur = connection.cursor()

    try:
        # Garantindo que os IDs sejam números inteiros
        id_cliente = int(input("Digite o ID do cliente: "))
        id_veiculo = int(input("Digite o ID do veículo: "))
        id_oficina = int(input("Digite o ID da oficina: "))

        # Solicitando a data do serviço e formatando para o tipo correto
        data_servico = input("Digite a data do serviço (YYYY-MM-DD): ")
        data_servico_formatada = dt.datetime.strptime(data_servico, '%Y-%m-%d').date()

        descricao_servico = input("Digite a descrição do serviço: ")

        # Inserindo os dados na tabela SERVIÇOS_AGENDADOS
        cur.execute("""
            INSERT INTO SERVICOS_AGENDADOS (id_cliente, id_veiculo, id_oficina, data_servico, descricao_servico) 
            VALUES (:1, :2, :3, :4, :5)
        """, 
        (id_cliente, id_veiculo, id_oficina, data_servico_formatada, descricao_servico))
        
        connection.commit()

        print("Serviço agendado com sucesso!")
    
    except ValueError:
        print("Erro: Certifique-se de que os IDs e a data estão corretos.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao inserir no banco de dados: {e}")
    finally:
        cur.close()
        connection.close()


def alterar_servico():
    connection = conexao()
    cur = connection.cursor()

    id_servico = input("Digite o ID do serviço a ser alterado: ")

    # Verifica se o ID do serviço existe
    cur.execute("SELECT * FROM SERVIÇOS_AGENDADOS WHERE id = :1", (id_servico,))
    resultado = cur.fetchone()

    if resultado is None:
        print("Serviço não encontrado!")
        cur.close()
        connection.close()
        return

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

    # Verifica se o serviço existe antes de tentar excluir
    cur.execute("SELECT * FROM SERVIÇOS_AGENDADOS WHERE id = :1", (id_servico,))
    resultado = cur.fetchone()

    if resultado is None:
        print("Serviço não encontrado! Verifique o ID e tente novamente.")
    else:
        cur.execute("DELETE FROM SERVIÇOS_AGENDADOS WHERE id = :1", (id_servico,))
        connection.commit()
        print("Serviço excluído com sucesso!")

    cur.close()
    connection.close()


def consultar_servicos():
    connection = conexao()
    cur = connection.cursor()

    # Executa a consulta para buscar todos os serviços agendados
    cur.execute("SELECT * FROM SERVIÇOS_AGENDADOS")
    resultados = cur.fetchall()

    if not resultados:
        print("Nenhum serviço agendado encontrado.")
    else:
        colunas = [desc[0] for desc in cur.description]
        print("\nResultados da Consulta:")
        print(", ".join(colunas))
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

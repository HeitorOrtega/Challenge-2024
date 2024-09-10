import datetime as dt

# Listas para armazenar os dados
clientes = []
veiculos = []
oficinas = []
funcionarios = []
estoque = []
servicos_agendados = []

# Função para encontrar o índice de um cliente pelo nome de usuário
def procurar_cliente(nome_usuario):
    """
    Retorna o índice do cliente com base no nome de usuário.
    """
    for i, cliente in enumerate(clientes):
        if cliente["Usuário"] == nome_usuario:
            return i
    return -1

# Função para adicionar um novo cliente
def criar_cliente(nome_usuario, nome, email, idade, cpf, telefone, senha):
    """
    Adiciona um novo cliente à lista de clientes e retorna o número total de clientes.
    """
    data_cadastro = dt.datetime.now()
    cliente = {
        "Usuário": nome_usuario,
        "Nome": nome,
        "Email": email,
        "Idade": idade,
        "CPF": cpf,
        "Telefone": telefone,
        "Senha": senha,
        "Data de Cadastro": data_cadastro
    }
    clientes.append(cliente)
    return len(clientes)

# Função para ler informações de um cliente específico ou todos os clientes
def ler_cliente(indice=-1):
    """
    Retorna as informações de um cliente específico ou de todos os clientes se o índice não for fornecido.
    """
    if 0 <= indice < len(clientes):
        return clientes[indice]
    else:
        return clientes

# Função para atualizar informações de um cliente
def atualizar_cliente(indice, nome_usuario=None, nome=None, email=None, idade=None, cpf=None, telefone=None):
    """
    Atualiza as informações de um cliente com base no índice fornecido.
    """
    if 0 <= indice < len(clientes):
        if nome_usuario is not None:
            clientes[indice]["Usuário"] = nome_usuario
        if nome is not None:
            clientes[indice]["Nome"] = nome
        if email is not None:
            clientes[indice]["Email"] = email
        if idade is not None:
            clientes[indice]["Idade"] = idade
        if cpf is not None:
            clientes[indice]["CPF"] = cpf
        if telefone is not None:
            clientes[indice]["Telefone"] = telefone
        return True
    else:
        return False

# Função para excluir um cliente
def deletar_cliente(indice):
    """
    Remove um cliente da lista com base no índice fornecido.
    """
    if 0 <= indice < len(clientes):
        clientes.pop(indice)
        return True
    else:
        return False

# Funções para veículos
def criar_veiculo(nome_cliente, modelo, ano, placa, descricao_problema):
    """
    Adiciona um veículo à lista de veículos.
    """
    data = dt.datetime.now()
    veiculo = {
        "Nome": nome_cliente,
        "Data": data,
        "Modelo": modelo,
        "Ano": ano,
        "Placa": placa,
        "Descricao problema": descricao_problema
    }
    veiculos.append(veiculo)
    return len(veiculos)

def ler_veiculo(indice=-1):
    """
    Retorna as informações de um veículo específico ou de todos os veículos.
    """
    if 0 <= indice < len(veiculos):
        return veiculos[indice]
    else:
        return veiculos

def atualizar_veiculo(indice, nome_cliente=None, modelo=None, ano=None, placa=None, descricao_problema=None, desc_reparo=None):
    """
    Atualiza as informações de um veículo com base no índice fornecido.
    """
    if 0 <= indice < len(veiculos):
        if nome_cliente is not None:
            veiculos[indice]["Nome"] = nome_cliente
        if modelo is not None:
            veiculos[indice]["Modelo"] = modelo
        if ano is not None:
            veiculos[indice]["Ano"] = ano
        if placa is not None:
            veiculos[indice]["Placa"] = placa
        if descricao_problema is not None:
            veiculos[indice]["Descricao problema"] = descricao_problema
        if desc_reparo is not None:
            veiculos[indice]["Desc_reparo"] = desc_reparo
            veiculos[indice]["Saida"] = dt.datetime.now()
        return True
    else:
        return False

def deletar_veiculo(indice):
    """
    Remove um veículo da lista com base no índice fornecido.
    """
    if 0 <= indice < len(veiculos):
        veiculos.pop(indice)
        return True
    else:
        return False

# Funções para oficinas
def criar_oficina(cep, endereco, nome_oficina, telefone_oficina):
    """
    Adiciona uma oficina à lista de oficinas.
    """
    oficina = {
        "CEP": cep,
        "Endereço": endereco,
        "Nome da Oficina": nome_oficina,
        "Telefone": telefone_oficina
    }
    oficinas.append(oficina)
    return len(oficinas)

def ler_oficina(indice=-1):
    """
    Retorna as informações de uma oficina específica ou de todas as oficinas.
    """
    if 0 <= indice < len(oficinas):
        return oficinas[indice]
    else:
        return oficinas

def atualizar_oficina(indice, cep=None, endereco=None, nome_oficina=None, telefone_oficina=None):
    """
    Atualiza as informações de uma oficina com base no índice fornecido.
    """
    if 0 <= indice < len(oficinas):
        if cep is not None:
            oficinas[indice]["CEP"] = cep
        if endereco is not None:
            oficinas[indice]["Endereço"] = endereco
        if nome_oficina is not None:
            oficinas[indice]["Nome da Oficina"] = nome_oficina
        if telefone_oficina is not None:
            oficinas[indice]["Telefone"] = telefone_oficina
        return True
    else:
        return False

def deletar_oficina(indice):
    """
    Remove uma oficina da lista com base no índice fornecido.
    """
    if 0 <= indice < len(oficinas):
        oficinas.pop(indice)
        return True
    else:
        return False

# Funções para funcionários
def criar_funcionario(nome_funcionario, cargo, data_contrata, salario, setor, tempo_empresa):
    """
    Adiciona um funcionário à lista de funcionários.
    """
    funcionario = {
        "Nome": nome_funcionario,
        "Cargo": cargo,
        "Data de contratação": data_contrata,
        "Salário": salario,
        "Setor": setor,
        "Tempo de empresa": tempo_empresa
    }
    funcionarios.append(funcionario)
    return len(funcionarios)

def ler_funcionario(indice=-1):
    """
    Retorna as informações de um funcionário específico ou de todos os funcionários.
    """
    if 0 <= indice < len(funcionarios):
        return funcionarios[indice]
    else:
        return funcionarios

def atualizar_funcionario(indice, nome_funcionario=None, cargo=None, data_contrata=None, salario=None, setor=None, tempo_empresa=None):
    """
    Atualiza as informações de um funcionário com base no índice fornecido.
    """
    if 0 <= indice < len(funcionarios):
        if nome_funcionario is not None:
            funcionarios[indice]["Nome"] = nome_funcionario
        if cargo is not None:
            funcionarios[indice]["Cargo"] = cargo
        if data_contrata is not None:
            funcionarios[indice]["Data de contratação"] = data_contrata
        if salario is not None:
            funcionarios[indice]["Salário"] = salario
        if setor is not None:
            funcionarios[indice]["Setor"] = setor
        if tempo_empresa is not None:
            funcionarios[indice]["Tempo de empresa"] = tempo_empresa
        return True
    else:
        return False

def deletar_funcionario(indice):
    """
    Remove um funcionário da lista com base no índice fornecido.
    """
    if 0 <= indice < len(funcionarios):
        funcionarios.pop(indice)
        return True
    else:
        return False

# Funções para estoque
def adicionar_peca_estoque(nome_peca, quantidade, preco, fornecedor):
    """
    Adiciona uma peça ao estoque.
    """
    peca = {
        "Nome da Peça": nome_peca,
        "Quantidade Disponível": quantidade,
        "Preço Unitário": preco,
        "Fornecedor": fornecedor
    }
    estoque.append(peca)
    return len(estoque)

def ler_estoque(indice=-1):
    """
    Retorna as informações de uma peça específica ou de todas as peças no estoque.
    """
    if 0 <= indice < len(estoque):
        return f"Peça {indice + 1}: {estoque[indice]}"
    else:
        estoque_formatado = []
        for i, peca in enumerate(estoque):
            estoque_formatado.append(f"Peça {i + 1}: {peca}")
        return "\n".join(estoque_formatado) if estoque_formatado else "⚠️ Estoque vazio."
  
def atualizar_estoque(indice, nome_peca=None, quantidade=None, preco=None, fornecedor=None):
    """
    Atualiza as informações de uma peça no estoque com base no índice fornecido.
    """
    if 0 <= indice < len(estoque):
        if nome_peca is not None:
            estoque[indice]["Nome da Peça"] = nome_peca
        if quantidade is not None:
            estoque[indice]["Quantidade Disponível"] = quantidade
        if preco is not None:
            estoque[indice]["Preço Unitário"] = preco
        if fornecedor is not None:
            estoque[indice]["Fornecedor"] = fornecedor
        return True
    else:
        return False

def deletar_peca_estoque(indice):
    """
    Remove uma peça do estoque com base no índice fornecido.
    """
    if 0 <= indice < len(estoque):
        estoque.pop(indice)
        return True
    else:
        return False

# Funções para serviços agendados
def agendar_servico(nome_cliente, nome_funcionario, data_agendamento, veiculo_placa, descricao_servico):
    """
    Agenda um serviço para um cliente com base nas informações fornecidas.
    """
    servico = {
        "Nome do Cliente": nome_cliente,
        "Nome do Funcionário": nome_funcionario,
        "Data de Agendamento": data_agendamento,
        "Placa do Veículo": veiculo_placa,
        "Descrição do Serviço": descricao_servico
    }
    servicos_agendados.append(servico)
    return len(servicos_agendados)

def ler_servico_agendado(indice=-1):
    """
    Retorna as informações de um serviço agendado específico ou de todos os serviços.
    """
    if 0 <= indice < len(servicos_agendados):
        return servicos_agendados[indice]
    else:
        return servicos_agendados

def atualizar_servico_agendado(indice, nome_cliente=None, nome_funcionario=None, data_agendamento=None, veiculo_placa=None, descricao_servico=None):
    """
    Atualiza as informações de um serviço agendado com base no índice fornecido.
    """
    if 0 <= indice < len(servicos_agendados):
        if nome_cliente is not None:
            servicos_agendados[indice]["Nome do Cliente"] = nome_cliente
        if nome_funcionario is not None:
            servicos_agendados[indice]["Nome do Funcionário"] = nome_funcionario
        if data_agendamento is not None:
            servicos_agendados[indice]["Data de Agendamento"] = data_agendamento
        if veiculo_placa is not None:
            servicos_agendados[indice]["Placa do Veículo"] = veiculo_placa
        if descricao_servico is not None:
            servicos_agendados[indice]["Descrição do Serviço"] = descricao_servico
        return True
    else:
        return False

def deletar_servico_agendado(indice):
    """
    Remove um serviço agendado da lista com base no índice fornecido.
    """
    if 0 <= indice < len(servicos_agendados):
        servicos_agendados.pop(indice)
        return True
    else:
        return False

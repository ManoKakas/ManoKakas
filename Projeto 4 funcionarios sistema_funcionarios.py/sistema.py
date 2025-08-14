# Bem-vindo à empresa de Kauã dos Santos
print("Bem-vindo à empresa de Kauã dos Santos")

lista_funcionarios = []
id_global = 5122296

def cadastrar_funcionario(id):
    print("\n--- Cadastrar Funcionário ---")
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = input("Digite o salário do funcionário: ")
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }
    lista_funcionarios.append(funcionario.copy())
    print("Funcionário cadastrado com sucesso!\n")

def consultar_funcionarios():
    while True:
        print("\n--- Consultar Funcionários ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Setor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            for f in lista_funcionarios:
                print(f)
        elif opcao == "2":
            id_busca = input("Digite o ID do funcionário: ")
            encontrado = False
            for f in lista_funcionarios:
                if str(f["id"]) == id_busca:
                    print(f)
                    encontrado = True
            if not encontrado:
                print("Funcionário não encontrado.")
        elif opcao == "3":
            setor_busca = input("Digite o setor: ")
            encontrados = [f for f in lista_funcionarios if f["setor"].lower() == setor_busca.lower()]
            if encontrados:
                for f in encontrados:
                    print(f)
            else:
                print("Nenhum funcionário encontrado nesse setor.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")

def remover_funcionario():
    while True:
        id_remover = input("Digite o ID do funcionário a ser removido: ")
        for f in lista_funcionarios:
            if str(f["id"]) == id_remover:
                lista_funcionarios.remove(f)
                print("Funcionário removido com sucesso!")
                return
        print("ID inválido. Tente novamente.")

# Menu principal
while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Remover Funcionário")
    print("4. Encerrar Programa")
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif escolha == "2":
        consultar_funcionarios()
    elif escolha == "3":
        remover_funcionario()
    elif escolha == "4":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

#-----Variaveis globais------

Lista_Funcionario = []
Codigo_Funcionario = 0

# ------- Fim das variaveis globais--------






#---------inicio cadastramento de funcionarios--------

def Cadastrar_Funcionario(Codigo):
    print("*"* 15,"MENU DE CADASTRAMENTO", "*"* 15)
    print("Codigo do Funcionario: {}".format(Codigo))
    Nome = input("Entre com o nome do funcionario:")
    Setor = input("Entre com o setor do Funcionario:")
    Salario = input("entre com o salario do funcionario:")

    Dicionario_Funcionario = {"Codigo"     : Codigo,
                              "Nome"       : Nome,
                              "Setor"      : Setor,
                              "Salario"    : Salario}
    Lista_Funcionario.append(Dicionario_Funcionario.copy())

    print("*"*15, "Cadastro concluido com sucesso",  "*"* 15)

    #---------Fim casatramento de funcionarios -----

    #---------Consultar funcionarios ---------

def Consultar_Funcionario():
    print("Bem-Vindo ao Menu de Consulta")
    while True:
        Opcao_Consulta = input("Escolha a opção desejada:\n" +
            "1 - Consultar todos os funcionarios:\n" +
            "2 - Consultar funcionario por ID:\n" +
            "3 - Consultar funcionario por setor\n" +
            "4 - Retomar:\n" +
            ">>>")
        
        if Opcao_Consulta == "1":
            print("Você escolheu a opção consultar funcionarios")
            for Funcionario in Lista_Funcionario:
                for key, value in Funcionario.items():
                    print("{}: {}".format(key, value))
        elif Opcao_Consulta == "2":
            print("Você escolheu a opção consultar funcionario por ID")
        elif Opcao_Consulta == "3":
            print("Você escolheu a opção consultar funcionario por setor")
        elif Opcao_Consulta == "4":
            print("Você escolheu a opção retomar")
            return
        else:
            print("Opção inválida, tente novamente")



        
        
       




#--------fim do consultar funcionario --------


# ------- inicio remover funcionarios -------

def Remover_Funcionario():
    print("Bem-Vindo ao menu remover funcionário")
    id_para_remover = input("Digite o ID do funcionário que deseja remover: ")

    # Procurar o funcionário pelo ID na lista
    for funcionario in Lista_Funcionario:
        if funcionario.get("Codigo") == id_para_remover:
            Lista_Funcionario.remove(funcionario)
            print(f"Funcionário com ID {id_para_remover} foi removido com sucesso.")
            return

    print(f"Funcionário com ID {id_para_remover} não encontrado na lista.")



# --------FIM DO REMOVER FUNCIONARIO --------

# --------INICIO DO MAIN -----------
print("BEM-VINDO AO CONTROLE DE FUNCIONARIOS DO LEVYY BRAGA")
print("*"*25, "*" * 26)
while True:
    Opcao_Principal = input("Escolha a opçaõ desejada\n"+
                            "1 - Cadastrar funcionarios\n" +
                            "2 - Consultar funcionarios\n" +
                            "3 - Remover funcionario\n" +
                            "4 - Sair\n" +
                            ">>>")

    if Opcao_Principal == "1":
        Codigo_Funcionario = Codigo_Funcionario + 1
        Cadastrar_Funcionario(Codigo_Funcionario)
    elif Opcao_Principal == "2":
      Consultar_Funcionario()
    elif Opcao_Principal == "3":
        Remover_Funcionario()
    elif Opcao_Principal == "4":
        break
    else:
        print("Opção invalida, tente novamente")
        continue














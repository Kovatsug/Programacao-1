class Pessoa:
    def __init__(self,nome,email,telefone):
        self.nome=nome
        self.email=email
        self.telefone=telefone

    def __str__(self):
        return f"Nome: {self.nome}\tE-mail: {self.email}\tTelefone: {self.telefone}"

ListaPessoas=[]

def menu():
    while True:
        print('''
--------MENU--------
1 - Listar Pessoas
2 - Cadastrar Pessoa
3 - Sair 
''')
        opc=int(input("Opção: "))

        if opc>3 or opc<1:
            print("Escolha uma opção válida:\n\n")
            continue
        elif opc==3:
            break

        elif opc==1:
            if ListaPessoas!=[]:
                for pessoa in ListaPessoas:
                    print(pessoa)
            else:
                print("Nenhuma pessoa foi cadastrada.")

        elif opc==2:
            nome=input("Nome: ")
            email=input("E-mail: ")
            telefone=input("Telefone: ")
            cadastro=Pessoa(nome,email,telefone)
            ListaPessoas.append(cadastro)
            print("Pessoa cadastrada.")

menu()
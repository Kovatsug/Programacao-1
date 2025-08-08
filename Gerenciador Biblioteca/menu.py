from operacoes import Operacoes_Administrador, Operacoes_Leitor, Operacoes

class MenuLeitor:
    def __init__(self, id_leitor):
        self.id_leitor = id_leitor
        self.opcoes = ["1. Listar livros","2. Emprestar","3. Devolver","4. Sair"]


    def exibir_menu(self, biblioteca, pessoas):
        for p in pessoas:
            if p.id == self.id_leitor:
                print(f"\nBem-Vindo, {p.nome}!")
                break
        while True:
            print("")
            for opcao in self.opcoes:
                print(opcao)
            opcao = input("Escolha: ")

            if opcao == "1":
                Operacoes_Leitor.listar_livros(biblioteca)
            elif opcao == "2":
                Operacoes_Leitor.emprestar_livro(biblioteca, pessoas, self.id_leitor)
            elif opcao == "3":
                Operacoes_Leitor.devolver_livro(biblioteca, pessoas, self.id_leitor)
            elif opcao == "4":
                break
            else:
                print("Opção inválida.")

class MenuADM:
    def __init__(self):
        self.opcoes = ["1. Cadastrar livro", "2. Listar livros", "3. Emprestar", "4. Devolver","5. Excluir livro", "6. Cadastrar Leitor", "7. Listar Leitores", "8. Sair"]

    def exibir_menu(self, biblioteca, pessoas):

        while True:
            print("")
            for opcao in self.opcoes:
                print(opcao)
            opcao = input("Escolha: ")

            if opcao == "1":
                Operacoes_Administrador.cadastrar_livro(biblioteca)
            elif opcao == "2":
                Operacoes_Administrador.listar_livros(biblioteca)
            elif opcao == "3":
                Operacoes_Administrador.emprestar_livro(biblioteca, pessoas)
            elif opcao == "4":
                Operacoes_Administrador.devolver_livro(biblioteca, pessoas)
            elif opcao == "5":
                Operacoes_Administrador.excluir_livro(biblioteca)
            elif opcao == "6":
                Operacoes_Administrador.cadastrar_leitor(pessoas)
            elif opcao == "7":
                Operacoes_Administrador.listar_leitores(pessoas)
            elif opcao == "8":
                break
            else:
                print("Opção inválida.")

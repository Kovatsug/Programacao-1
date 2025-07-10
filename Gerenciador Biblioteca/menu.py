from operacoes import Operacoes

class MenuLeitor:
    def __init__(self, id_leitor):
        self.id_leitor = id_leitor
        self.opcoes = ["1. Listar livros","2. Emprestar","3. Devolver","4. Reservar","5. Sair"] 


    def exibir_menu(self, biblioteca):

        while True:
            for opcao in self.opcoes:
                print(opcao,"\n")
            opcao = input("Escolha: ")

            if opcao == "1":
                Operacoes.listar_livros(biblioteca)
            elif opcao == "2":
                Operacoes.emprestar_livro(biblioteca, self.id_leitor)
            elif opcao == "3":
                Operacoes.devolver_livro(biblioteca)
            elif opcao == "4":
                Operacoes.reservar_livro(biblioteca, self.id_leitor)
            elif opcao == len(self.opcoes):
                break
            else:
                print("Opção inválida.")

class MenuADM:
    def __init__(self, id_adm):
        self.id_adm = id_adm
        self.opcoes = ["1. Cadastrar livro", "2. Listar livros", "3. Emprestar", "4. Devolver", "5. Reservar","6. Excluir livro", "7. Cadastrar Leitor", "8. Listar Leitores", "9. Sair"]

    def exibir_menu(self, biblioteca, pessoas):
        while True:
            for opcao in self.opcoes:
                print(opcao,"\n")
            opcao = input("Escolha: ")

            if opcao == "1":
                Operacoes.cadastrar_livro(biblioteca)
            elif opcao == "2":
                Operacoes.listar_livros(biblioteca)
            elif opcao == "3":
                Operacoes.emprestar_livro(biblioteca, pessoas)
            elif opcao == "4":
                Operacoes.devolver_livro(biblioteca)
            elif opcao == "5":
                Operacoes.reservar_livro(biblioteca, pessoas)
            elif opcao == "6":
                Operacoes.excluir_livro(biblioteca)
            elif opcao == "7":
                Operacoes.cadastrar_leitor(pessoas)
            elif opcao == "8":
                Operacoes.listar_leitores(pessoas)
            elif opcao == len(self.opcoes):
                break
            else:
                print("Opção inválida.")

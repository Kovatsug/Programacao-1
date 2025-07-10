from pessoas import Leitor, Bibliotecario
from operacoes import cadastrar_livro, listar_livros, emprestar_livro, devolver_livro
from menu import MenuADM, MenuLeitor

def main():

    biblioteca = []
    pessoas = [Bibliotecario("root", "000"), Leitor("João", "001")]

    menu_adm = MenuADM()
    menu_leitor = MenuLeitor()

    while True:
        print("1. Acesso como Administrador\n2. Acesso como Leitor\n3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            login = input("Digite o ID do administrador: ")
            for p in pessoas:
                if p.id == login and p.admin:
                    menu_adm.exibir_menu(biblioteca, pessoas)
                    break
            else:
                print("Acesso negado. ID inválido.")


        elif opcao == "2":
            menu_leitor.exibir_menu(biblioteca, pessoas)



        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
from pessoas import Pessoa, Bibliotecario
from operacoes import cadastrar_livro, listar_livros, emprestar_livro, devolver_livro

def main():
    joao = Pessoa("João", "001")
    root = Bibliotecario("root", "000")
    
    biblioteca = []
    pessoas = [joao,root]

    while True:
        print("\n1. Cadastrar livro\n2. Listar livros\n3. Emprestar\n4. Devolver\n5. Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_livro(biblioteca)
        elif opcao == "2":
            listar_livros(biblioteca)
        elif opcao == "3":
            emprestar_livro(biblioteca, pessoas)
        elif opcao == "4":
            devolver_livro(biblioteca)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
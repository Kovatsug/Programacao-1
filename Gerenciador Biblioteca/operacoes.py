from livro import Livro
from pessoas import Leitor

class Operacoes:
    
    def listar_livros(biblioteca):
        if biblioteca == []:
            print("Nenhum livro cadastrado.")
        for livro in biblioteca:
            print(livro)

    def L_emprestar_livro(biblioteca, pessoas, id_leitor):
        try:
            titulo = input("Titulo do livro: ")
            for l in biblioteca:
                if l.titulo == titulo:
                    livro = l
                    break
            for p in pessoas:
                if p.id == id_leitor:
                    leitor = p
                    break
            livro.emprestar(leitor)
            print("Livro emprestado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
    
    def L_devolver_livro(biblioteca, pessoas, id_leitor):
        try:
            titulo = input("Titulo do livro: ")
            for p in pessoas:
                if p.id == id_leitor:
                    leitor = p
                    break
            for l in leitor.livros_emprestados:
                if l.titulo == titulo:
                    livro = l
                    break
            livro.devolver(leitor)
            print("Livro devolvido com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")


    #------------------------------Operações Administrativas--------------------------------------

    def emprestar_livro(biblioteca, pessoas):
        try:
            titulo = input("Titulo do livro: ")
            
            id_pessoa = input("ID da pessoa: ")
            for l in biblioteca:
                if l.titulo == titulo:
                    livro = l
                    break
            for p in pessoas:
                if p.id == id_pessoa:
                    pessoa = p
                    break
            livro.emprestar(pessoa)
            print("Livro emprestado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def devolver_livro(biblioteca, pessoas):
        try:
            id_pessoa = input("ID da pessoa: ")
            for p in pessoas:
                if p.id == id_pessoa:
                    pessoa = p
                    break
            titulo = input("Titulo do livro: ")
            for l in pessoa.livros_emprestados:
                if l.titulo == titulo:
                    livro = l
                    break
            livro.devolver()
            print("Livro devolvido com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

     #Exclusivo Administrador

    def cadastrar_livro(biblioteca):
        try:
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            livro = Livro(titulo, autor, categoria)
            biblioteca.append(livro)
            print("Livro cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def excluir_livro(biblioteca):
        try:
            titulo = input("Título do livro a ser excluído: ")
            for l in biblioteca:
                if l.titulo == titulo:
                    livro = l
            biblioteca.remove(livro)
            print("Livro excluído com sucesso!")
        except StopIteration:
            print("Livro não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")

    def cadastrar_leitor(pessoas):
        nome = input("Nome do leitor: ")
        id = f"00{len(pessoas) + 1}"
        leitor = Leitor(nome, id)
        pessoas.append(leitor)
        print("Leitor cadastrado com sucesso!")

    def listar_leitores(pessoas):
        if not pessoas:
            print("Nenhum leitor cadastrado.")
        for p in pessoas:
            print(p)
            print("\n-----------------\n")

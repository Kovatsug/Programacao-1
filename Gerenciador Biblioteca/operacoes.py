from livro import Livro
from pessoas import Leitor

class OperacoesBiblioteca:
    
    def listar_livros(biblioteca):
        if biblioteca == []:
            print("Nenhum livro cadastrado.")
        for livro in biblioteca:
            print(livro)

    def emprestar_livro(biblioteca, pessoa):
        try:
            titulo = input("Titulo do livro: ")
            
            id_pessoa = input("ID da pessoa: ")
            for l in biblioteca:
                if l.titulo == titulo:
                    livro = l
            for p in pessoa:
                if p.id == id_pessoa:
                    pessoa = p
            livro.emprestar(pessoa)
            print("Livro emprestado com sucesso!")
        except StopIteration:
            print("Livro ou pessoa não encontrados.")
        except Exception as e:
            print(f"Erro: {e}")

    def devolver_livro(biblioteca):
        try:
            titulo = input("Titulo do livro: ")
            livro = next(l for l in biblioteca if l.titulo == titulo)
            livro.devolver()
            print("Livro devolvido com sucesso!")
        except StopIteration:
            print("Livro não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")

    def reservar_livro(biblioteca, pessoa):
        try:
            titulo = input("Titulo do livro: ")
            id_pessoa = input("ID da pessoa: ")
            for l in biblioteca:
                if l.titulo == titulo:
                    livro = l
            for p in pessoa:
                if p.id == id_pessoa:
                    pessoa = p
            livro.reservar(pessoa)
            print("Livro reservado com sucesso!")
        except StopIteration:
            print("Livro ou pessoa não encontrados.")
        except Exception as e:
            print(f"Erro: {e}")

    #Operações Administrativas

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

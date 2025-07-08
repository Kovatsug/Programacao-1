from livro import Livro

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

def listar_livros(biblioteca):
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    for livro in biblioteca:
        print(livro)

def emprestar_livro(biblioteca, pessoas):
    try:
        titulo = input("Titulo do livro: ")
        id_pessoa = input("ID da pessoa: ")
        livro = next(l for l in biblioteca if l.titulo == titulo)
        pessoa = next(p for p in pessoas if p.id == id_pessoa)
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
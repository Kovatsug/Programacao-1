import pandas as pd
import ast
from livro import Livro
from pessoas import Leitor

def carregar_dados():
    df_livros = pd.read_csv('Gerenciador Biblioteca/data/livros.csv')
    df_pessoas = pd.read_csv('Gerenciador Biblioteca/data/leitores.csv')

    # Recriando objetos Leitor
    pessoas = [Leitor(
        row.nome,
        str(row.id),
        (row.admin),
        ast.literal_eval(row.livros_emprestados)
    ) for row in df_pessoas.itertuples()]

    # Recriando objetos Livro
    livros = [Livro(
        row.titulo,
        row.autor,
        (row.disponivel),
        row.emprestado_para
    ) for row in df_livros.itertuples()]

    return livros, pessoas


def salvar_dados(livros, pessoas):
    if livros:
        df_livros = pd.DataFrame([livro.__dict__ for livro in livros])
    else:
        colunas = ['titulo', 'autor', 'disponivel', 'emprestado_para']
        df_livros = pd.DataFrame(columns=colunas)
    df_pessoas = pd.DataFrame([pessoa.to_dict() for pessoa in pessoas])
    df_livros.to_csv('Gerenciador Biblioteca/data/livros.csv', index=False)
    df_pessoas.to_csv('Gerenciador Biblioteca/data/leitores.csv', index=False)


class Livro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponivel = True
        self.emprestado_para = None

    def emprestar(self, pessoa):
        if self.disponivel == False:
            raise Exception("Livro já emprestado.")
        pessoa.livros_emprestados.append(self.titulo)
        self.disponivel = False
        self.emprestado_para = pessoa

    def devolver(self, pessoa):
        if self.disponivel:
            raise Exception("Livro não está emprestado.")
        pessoa.livros_emprestados.remove(self)
        self.disponivel = True
        self.emprestado_para = None



    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para.nome}" 
        return f"{self.titulo} - {self.autor} - {self.categoria} - {status}"
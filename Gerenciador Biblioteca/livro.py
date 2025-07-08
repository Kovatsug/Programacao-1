class Livro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponivel = True
        self.emprestado_para = None

    def emprestar(self, pessoa):
        if not self.disponivel:
            raise Exception("Livro já emprestado.")
        self.disponivel = False
        self.emprestado_para = pessoa

    def devolver(self):
        if self.disponivel:
            raise Exception("Livro não está emprestado.")
        self.disponivel = True
        self.emprestado_para = None

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para.nome}"
        return f"{self.titulo} - {self.autor} - {self.categoria} - {status}"
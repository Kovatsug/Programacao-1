class Livro:
    def __init__(self, titulo, autor, categoria):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponivel = True
        self.reservado = False
        self.reservado_por = None
        self.emprestado_para = None

    def emprestar(self, pessoa):
        if self.disponivel == False:
            raise Exception("Livro já emprestado.")
        self.disponivel = False
        self.emprestado_para = pessoa

    def devolver(self):
        if self.disponivel:
            raise Exception("Livro não está emprestado.")
        self.disponivel = True
        self.emprestado_para = None

    def reservar(self, pessoa):
        if self.disponivel == False:
            raise Exception("Livro já emprestado.")
        elif self.reservado == True:
            raise Exception("Livro já reservado.")
        self.disponivel = False
        self.reservado = True
        self.reservado_por = pessoa

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para.nome}" if self.emprestado_para else f"Reservado por {self.reservado_por.nome}"
        return f"{self.titulo} - {self.autor} - {self.categoria} - {status}"
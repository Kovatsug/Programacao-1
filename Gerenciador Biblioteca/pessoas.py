from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome


class Leitor(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome)
        self.__id = id
        self.__admin = False
        self.__livros_reservados = []
        self.__livros_emprestados = []  

    @property
    def id(self):
        return self.__id
    @property
    def admin(self):
        return self.__admin

    @property
    def livros_reservados(self):
        return self.__livros_reservados

    def __str__(self):
        return f"Leitor: {self.nome}, ID: {self.id}, Livros Reservados: {self.livros_reservados}, Livros Emprestados: {self.livros_emprestados}"

class Bibliotecario(Pessoa):
    def __init__(self, nome, id, senha):
        super().__init__(nome)
        self.__id = id
        self.__admin = True

    @property
    def id(self):
        return self.__id

    @property
    def admin(self):
        return self.__admin
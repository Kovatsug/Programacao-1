from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome


class Leitor(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome)
        self.__id = id
        self.__admin = False
        self.livros_emprestados = []  

    @property
    def id(self):
        return self.__id
    @property
    def admin(self):
        return self.__admin


    def __str__(self):
        livros=[]
        for l in self.livros_emprestados:
            livros.append(l.titulo)
        return f"Leitor: {self.nome}, ID: {self.id}, Livros Emprestados: {livros}"

class Bibliotecario(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome)
        self.__id = id
        self.__admin = True

    @property
    def id(self):
        return self.__id

    @property
    def admin(self):
        return self.__admin
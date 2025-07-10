from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, id):
        self.nome = nome
        self.__id = id

    def id(self):
        return self.__id


class Bibliotecario(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome, id)

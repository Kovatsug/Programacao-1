from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

@abstractmethod
class Leitor(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome, id)
        self.adm=False
@abstractmethod
class Bibliotecario(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome, id)
        self.adm=True
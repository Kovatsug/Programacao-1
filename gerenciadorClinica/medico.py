from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome:str,senha:str, email:str, dt_nasc,numCRM:str, especialidade:str):
        super().__init__(nome, email, dt_nasc, senha)
        self.especialidade = especialidade
        self.numCRM = numCRM
    
    def __repr__ (self)->str:
        return self.nome + ":" + self.numCRM
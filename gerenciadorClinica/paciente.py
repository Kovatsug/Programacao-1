from pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome,senha, email, dt_nasc, telefone, tps):
        super().__init__(nome, email, dt_nasc,senha)
        self.telefone = telefone
        self.tipo_sanguineo = tps

    def __repr__(self):
        return f'''
        Contato: {self.telefone}, 
        Tipo sanguíneo: {self.tipo_sanguineo}'''

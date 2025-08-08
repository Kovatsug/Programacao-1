class Pessoa(object):
    
    def __init__(self, nome, email, dt_nasc, senha):
        self.nome = nome
        self.email = email
        self.data_nascimento = dt_nasc
        self.senha = senha
        self.login = nome

    def __str__(self):
        return f'''
        Nome: {self.nome}, 
        Email: {self.email}, 
        Nascido(a) em: {self.data_nascimento}'''
    
    def __lt__(self,ob):
        return self.nome < ob.nome
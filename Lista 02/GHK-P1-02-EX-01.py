class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def apresentar(self):
        return f'''
Nome: {self.nome}
Idade: {self.idade}
'''
    
a=Pessoa("paulo",22)
print(a.apresentar())
        
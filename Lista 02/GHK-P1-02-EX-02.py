class MinhaLista:
    def __init__(self):
        self.itens=[]

    def adicionar(self,item):
        self.itens.append(item)
    
    def apresentar(self):
        return f'''
Minha Lista: {" ".join(self.itens)}
'''
    
a=MinhaLista()
a.adicionar("item 1")
a.adicionar("item 2")
a.adicionar("item 3")
print(a.apresentar())
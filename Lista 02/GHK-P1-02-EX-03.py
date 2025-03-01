class ContaBancaria:
    def __init__(self,titular,saldo=0.0):
        self.titular=titular
        self.saldo=saldo

    def depositar(self, valor):
        self.saldo+=valor

    def sacar(self, valor):
        self.saldo-=valor

    def apresentar(self):
        return f'''
Titular: {self.titular}
Saldo: R$ {self.saldo:.2f}
'''
    
a=ContaBancaria("Paulo",1.99)
a.depositar(1.50)
print(a.apresentar())

b=ContaBancaria("Joaquim",1234567.89)
b.sacar(1234567)
b.depositar(0.11)
print(b.apresentar())
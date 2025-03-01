import math

class circulo:
    def __init__(self,raio):
        self.raio=raio

    def CalcularArea(self):
        return (self.raio*self.raio)*math.pi

    def CalcularPerimetro(self):
        return self.raio*math.pi*2
    
    def imprimir(self):
        area=self.CalcularArea()
        perimetro=self.CalcularPerimetro()
        return f'''
Raio: {self.raio}
Area: {"%.2f"%area}
Perimetro: {"%.2f"%perimetro}
'''
    
for i in range(1,6):
    print(circulo(i).imprimir())
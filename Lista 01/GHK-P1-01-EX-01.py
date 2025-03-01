class quadrado:
    def __init__(self,lado):
        self.lado=lado

    def CalcularArea(self):
        return self.lado*self.lado

    def CalcularPerimetro(self):
        return self.lado*4
    
    def imprimir(self):
        area=self.CalcularArea()
        perimetro=self.CalcularPerimetro()
        return f'''
lado: {self.lado}
Area: {area}
Perimetro: {perimetro}
'''
    
for i in range(1,6):
    print(quadrado(i).imprimir())
class Menu(object):

    def __init__(self) -> None:
        self.opcoes = ["1. Verificar consultas", "2. Cancelar consultas", "3. Sair"]

    def ativarMenu(self) ->int:
        self.desenharMenu()
        return self.caputarOpcao()
        

    def definirOpcoes(self,opcoes:list[str]):
        self.opcoes = opcoes    
    
    def desenharMenu(self):
        
        largura_menu = 30
        
        print("+" + "-" * (largura_menu - 2) + "+")
        for opcao in self.opcoes:
            espacos_opcao = largura_menu - 2 - len(opcao) - 2 
            print("| " + opcao + " " * espacos_opcao + " |")

        print("+" + "-" * (largura_menu - 2) + "+")

    def caputarOpcao(self) -> int:
        entrada = False
        opcao = -1
        opcao = int(input("Digite o número da opção(1-"+str(len(self.opcoes))+"):"))
        while not entrada:

            if opcao >0 and opcao <= len(self.opcoes):
                entrada = True
                
                
            else:
                opcao = int(input("Digite o número da opção válida:"))

        return opcao


from medico import Medico
from paciente import Paciente
from menu import Menu
from consulta import Consulta

class Gerenciador:

    def __init__(self) -> None:
        self.pacientes = []
        self.medicos = []
        self.consultas = []
        self.medicoLogado = None
        self.pacienteLogado = None

    def criarMedico(self, nome:str,  email:str, dt_nasc,
                    numCRM:str, especialidade:str, senha:str="123"):
        self.medicos.append(Medico(nome,senha,email,dt_nasc,numCRM,especialidade))

    def criarPaciente(self, nome:str, email:str, dt_nasc:str, 
                      telefone:str, tps:str,senha:str):
        self.pacientes.append(Paciente(nome,senha,email,dt_nasc,telefone,tps))

    def buscarPaciente(self, nome:str)->Paciente:
        for paciente in self.pacientes:
            if paciente.nome == nome:
                return paciente
    
    def logarPaciente(self,login:str, senha:str)->Paciente:
        for paciente in self.pacientes:
            if (paciente.senha == senha) and (paciente.login == login) :
                return paciente

    def logarMedico(self,login:str, senha:str)->Medico:
        for medico in self.medicos:
            if medico.senha == senha and medico.login == login:
                return medico

    def buscarMedico(self, nome:str)->Medico:
        for medico in self.medicos:
            if medico.nome == nome:
                return medico

    def removerPaciente(self,nome:str)->bool:
        paciente = self.buscarPaciente(nome)
        if(paciente != None):
            self.pacientes.remove(paciente)

    def listarPacientes(self,nome):
        for paciente in self.pacientes:
            print(paciente)

    def marcarConsulta(self,nome,data,horario):
        if self.medicoLogado != None:
            paciente = self.buscarPaciente(nome)
            if(paciente != None):
                self.consultas.append(Consulta(self.medicoLogado,paciente,horario,data))

    def listarConsultas(self):
        if self.medicoLogado != None:
            for consulta in self.consultas:
                if consulta.medico.nome == self.medicoLogado.nome:
                    print(consulta)
        elif self.pacienteLogado != None:
            for consulta in self.consultas:
                if consulta.paciente.nome == self.pacienteLogado.nome:
                    print(consulta)

    def removerConsulta(self,nome,data,horario):
        if self.medicoLogado != None:
            for c in self.consultas:
                if (c.medico.nome == self.medicoLogado.nome) and (c.pacinete.nome == nome) and (c.data == data) and (c.horario == horario):
                    c.status = "Desmarcada - Médico"
        elif self.pacienteLogado != None:
            for c in self.consultas:
                if (c.paciente.nome == self.pacienteLogado.nome) and (c.medico.nome == nome) and (c.data == data) and (c.horario == horario):
                    c.status = "Desmarcada - Paciente"

    def executar(self):
        logado = False
        while logado != True:
            op = input("Você é médico(M) ou paciente(P)")
            login = input("Digite seu login")
            senha = input("Digite sua senha")
            
            if (op.lower()) == "m":
                self.medicoLogado = self.logarMedico(login, senha)
                opcoes = ["1. Cadastrar pacientes", "2. Cadastrar consultas", "3. Remover pacientes", "4.Remover consulta", "5. Cadastrar Médico", "6.Sair"]
            
            elif (op.lower()) == "p":
                self.pacienteLogado = self.logarPaciente(login, senha)
                opcoes = ["1. Verificar consultas", "2. Cancelar consultas", "3. Sair"]
            
            else:
                print("\n-----Opção inválida-----\n")
            
            
            if(self.medicoLogado != self.pacienteLogado):
                logado = True

        while True:
            men = Menu()
            men.definirOpcoes(opcoes)
            op = men.ativarMenu()
            if op == len(opcoes):
                self.medicoLogado==None
                self.pacienteLogado==None
                print("\n---SAINDO DO SISTEMA---\n")
                g.executar()
                
            if self.medicoLogado!=None:
                if op==1:
                    nome=input("Nome: ")
                    email=input("Email: ")
                    dt_nasc=input("Nascimento: ")
                    telefone=input("Telefone: ")
                    tps=input("Tipo Sanguineo: ")
                    senh=input("Senha")
                    self.criarPaciente(nome,email,dt_nasc,telefone,tps,senh)
                    print("\n--FEITO--\n")

                elif op ==2:
                    nome=input("Paciente: ")
                    data=input("Data:")
                    horario=input("Horario: ")
                    self.marcarConsulta(nome,data,horario)
                    print("\n--FEITO--\n")

                elif op ==3:
                    nome=input("Paciente: ")
                    self.removerPaciente(nome)
                    print("\n--FEITO--\n")
                    
                elif op==4:
                    nome=input("Paciente: ")
                    data=input("Data:")
                    horario=input("Horario: ")
                    self.removerConsulta()
                    print("\n--FEITO--\n")
                    
                elif op ==5:
                    nome=input("Nome: ")
                    email=input("Email: ")
                    nasc=input("Nascimento: ")
                    numCRM=input("CRM: ")
                    esp=input("Especialidade: ")
                    senh=input("Senha")
                    self.criarMedico(nome,email,nasc,numCRM,esp,senh)
                    print("\n--FEITO--\n")

            if self.pacienteLogado!=None:
                if op==1:
                    self.listarConsultas()
                elif op ==2:
                    nome=input("Paciente: ")
                    data=input("Data:")
                    horario=input("Horario: ")
                    self.removerConsulta(nome,data,horario)
                    print("\n--FEITO--\n")



if __name__ == "__main__":
    g = Gerenciador()
    g.medicos.append(g.criarMedico("root","root@root","02/02/1999","231231","Gerente"))
    g.executar()
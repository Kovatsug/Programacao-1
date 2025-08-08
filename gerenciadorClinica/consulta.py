class Consulta:

    def __init__(self, medico, paciente, horario:str,data:str):
        self.medico = medico
        self.paciente = paciente
        self.horario = horario
        self.data = data
        self.status = "Marcada"

    def __repr__(self) -> str:
        return f"Medico:{self.medico}, Paciente:{self.paciente.nome}, {self.data}-{self.horario}"
from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome, cpf, idade, matricula, curso, semestre):
        super().__init__(nome,cpf,idade)
        self.matricula = matricula
        self.curso = curso
        self.semestre = semestre

    def __str__(self):
        return f"{super() .__str__()}, Matricula: {self.matricula}, Curso: {self.curso}, Semestre: {self.semestre}"

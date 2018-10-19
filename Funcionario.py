# Classe Funcionario
#Importar classe Pessoa
from Pessoa import Pessoa

class Funcionario(Pessoa):


    #metodo construtor
    def __init__(self, nome, cpf, idade, matricula, salario, setor):

        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor

    def __str__(self):
        return f"{super() .__str__()}, Matricula: {self.matricula}, Salario: {self.salario}, Setor: {self.setor}"
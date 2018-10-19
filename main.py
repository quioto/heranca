from Pessoa import Pessoa
from Funcionario import Funcionario
from Aluno import Aluno
# Objeto da classe PEssoa
p1 = Pessoa("João", '123', 20)
#Imprimir dados do objeto
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
print(p1)

f1 = Funcionario('José', '456', 40, '0099', 2526.54, 'Biblioteca')
print(f1.get_nome())
print(f1)



a1 = Aluno("Joao", '456', 20, '0099', "CdC", "21803575")
print(a1)
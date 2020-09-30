class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30


p1 = Programador("Tulio", 29, 1200)
print(p1.nome)
print(p1.salario)
p1.aumenta_salario()
print(p1.salario)

a1 = Analista("Gisele", 28, 4000)
print(a1.nome)
print(a1.salario)
a1.aumenta_salario()
print(a1.salario)
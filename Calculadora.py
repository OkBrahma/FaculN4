class Calculadora:
    def __init__(self, valorA=None, valorB=None, operacao=None):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, operacao):
        return operacao in ['+', '-', '*', '/']

    def calcular(self):
        if not self.validarOperacao(self.__operacao):
            print("Operação inválida.")
            return None

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Divisão por zero não é permitida.")
                return None
            return self.__valorA / self.__valorB

    def mostrarResultado(self):
        resultado = self.calcular()
        if resultado is not None:
            print(f"{self.__valorA} {self.__operacao} {self.__valorB} = {resultado}")

    def entradaDados(self):
        try:
            self.__valorA = float(input("Digite o valor A: "))
            self.__valorB = float(input("Digite o valor B: "))
            self.__operacao = input("Digite a operação (+, -, *, /): ")
        except ValueError:
            print("Entrada inválida. Por favor, insira números para os valores.")
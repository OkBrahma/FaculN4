from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, dataAberturaEmpresa, cnpj, status=False):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAberturaEmpresa = dataAberturaEmpresa
        self.__cnpj = cnpj

    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa

    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, dataAberturaEmpresa):
        self.__dataAberturaEmpresa = dataAberturaEmpresa

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracteres (no formato 00.000.000/0001-00).")
        self.__cnpj = cnpj
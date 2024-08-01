from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("Empresa X", "12345-6", "2022-01-01", False)
pessoa.imprimir_atributos()

## Pessoa física
pessoa_fisica = PessoaFisica("João", "98765-4", "2023-02-02", "1990-01-01", "000.111.222-33", "15975388-1", True)
pessoa_fisica.imprimir_atributos()

## Pessoa jurídica
pessoa_juridica = PessoaJuridica("Empresa Y", "54321-7", "2023-03-03", "2020-05-05", "12.345.678/0001-90", True)
pessoa_juridica.imprimir_atributos()


try:
    pessoa.nome = "Empresa Z"
    pessoa.numeroConta = "12345-7"
    pessoa.dataAberturaConta = "2023-04-04"
    pessoa.status = True
    pessoa.imprimir_atributos()

    pessoa_fisica.nome = "Ana"
    pessoa_fisica.numeroConta = "87654-3"
    pessoa_fisica.dataAberturaConta = "2022-11-11"
    pessoa_fisica.dataNascimento = "1985-05-15"
    pessoa_fisica.cpf = "123.456.789-0"
    pessoa_fisica.rg = "98765432-1"
    pessoa_fisica.status = False
    pessoa_fisica.imprimir_atributos()
except ValueError as e:
    print(e)

try:
    pessoa_fisica.cpf = "123.456.789-00"
    pessoa_fisica.imprimir_atributos()
except ValueError as e:
    print(e)


try:
    pessoa_juridica.cnpj = "12.345.678/0001-9"
    pessoa_juridica.imprimir_atributos()
except ValueError as e:
    print(e)

try:
    pessoa_juridica.cnpj = "12.345.678/0001-90"
    pessoa_juridica.imprimir_atributos()
except ValueError as e:
    print(e)
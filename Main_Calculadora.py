from Calculadora import Calculadora

def main():
    calc = Calculadora()
    while True:
        calc.entradaDados()
        calc.mostrarResultado()
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
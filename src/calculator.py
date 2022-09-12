class Calculator:

    def addition(self, a, b):
        return a + b
    
    def subtraction(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def division(self, a, b):
        return a / b


if __name__ == '__main__':
    # criação do objeto
    calc = Calculator()

    # ====================
    # Test #1
    # ====================
    # comportamento observado
    result = calc.addition(2, 2)    
    # comportamento esperado
    esperado = 4
    # teste
    tcname = "Test Addition (2,2)"
    print(tcname)
    if result == esperado:
        print("Passou!")  # teste passa
    else:
        print("Falhou!")  # teste falha
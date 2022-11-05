class Calculos:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        resultado = self.num1 + self.num2

        print("La suma de los valores es: ", resultado)

    def resta(self):
        resultado = self.num1 - self.num2

        print("La resta de los valores es: ", resultado)

    def multiplicacion(self):
        resultado = self.num1 * self.num2

        print("La multiplicación de los valores es: ", resultado)

    def division(self):
        resultado = self.num1 / self.num2

        print("La división de los valores es: ", resultado)
        

valor1 = int(input("Ingrese el primer valor: "))

valor2 = int(input("Ingrese el segundo valor: "))


micalculo=Calculos(valor1, valor2)
micalculo.suma()
micalculo.resta()
micalculo.multiplicacion()
micalculo.division()


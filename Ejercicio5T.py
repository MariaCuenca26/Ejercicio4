from math import sqrt
class Ecuaciones2Grado():
    def __init__(self):
        self.interfaz()
    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("La solución de la ecuación es con números complejos")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print("""\
Las soluciones de la ecuación son:
x1 = {}
x2 = {} """.format(x1, x2))
    def interfaz(self):
        A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
        B = int(input("Ingrese el coeficiente de la variable lineal\n"))
        C = int(input("Ingrese el término independiente\n"))
        
        self.calcular(A, B, C)
Ecuaciones2Grado()
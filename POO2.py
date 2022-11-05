class Alumno:

    def __init__(self):
        self.nombre = ""
        self.nota = 0

    def ingresa(self):
        self.nombre = input("Ingrese el nombre del alumno: ")
        self.nota = int(input("Ingrese la nota del alumno entre 0 a 10: "))

    def ver_calificacion(self):
        if self.nota>=3:
            print("El alumno ", self.nombre, ", ha aprobado.")
        else:
            print("El alumno ", self.nombre, ", ha reprobado.")

alumno1=Alumno()
alumno1.ingresa()
alumno1.ver_calificacion()

    
    

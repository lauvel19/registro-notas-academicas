class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def registrar_nota(self, materia, nota, semestre):
        if not isinstance(nota, (int, float)):
            raise ValueError("La nota debe ser un número.")
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        if semestre not in self.notas:
            self.notas[semestre] = {}
        self.notas[semestre][materia] = nota
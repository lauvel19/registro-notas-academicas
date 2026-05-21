class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}

    def registrar_nota(self, materia, nota, semestre):
        if not isinstance(nota, (int, float)):
            raise ValueError(f"La nota '{nota}' no es un número válido.")
        if nota < 0.0 or nota > 5.0:
            raise ValueError(
                f"La nota {nota} está fuera del rango permitido (0.0 – 5.0)."
            )
        if semestre not in self.notas:
            self.notas[semestre] = {}
        self.notas[semestre][materia] = nota

    def aprobo(self, materia, semestre):
        if semestre not in self.notas or materia not in self.notas[semestre]:
            raise ValueError(
                f"No existe nota para '{materia}' en el semestre '{semestre}'."
            )
        return self.notas[semestre][materia] >= 3.0
    
    def calcular_promedio(self):
        todas = [
            nota
            for semestre in self.notas.values()
            for nota in semestre.values()
        ]
        if not todas:
            return 0.0
        return sum(todas) / len(todas)
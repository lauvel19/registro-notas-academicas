import pytest
from src.registro_notas import Estudiante


# --- REQ-1: Validación de nota entre 0.0 y 5.0 ---

def test_registrar_nota_valida_rango_medio():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Matemáticas", 3.5, "2025-1")
    assert "Matemáticas" in estudiante.notas["2025-1"]

def test_registrar_nota_en_limite_inferior():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Física", 0.0, "2025-1")
    assert estudiante.notas["2025-1"]["Física"] == 0.0

def test_registrar_nota_en_limite_superior():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Química", 5.0, "2025-1")
    assert estudiante.notas["2025-1"]["Química"] == 5.0

def test_rechazar_nota_bajo_minimo():
    estudiante = Estudiante("Laura")
    with pytest.raises(ValueError):
        estudiante.registrar_nota("Historia", -0.1, "2025-1")

def test_rechazar_nota_sobre_maximo():
    estudiante = Estudiante("Laura")
    with pytest.raises(ValueError):
        estudiante.registrar_nota("Arte", 5.1, "2025-1")
        
        

# --- REQ-2: Aprobar o reprobar ---

def test_estudiante_aprueba_con_nota_exacta_limite():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Biología", 3.0, "2025-1")
    assert estudiante.aprobo("Biología", "2025-1") is True

def test_estudiante_reprueba_con_nota_bajo_limite():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Biología", 2.9, "2025-1")
    assert estudiante.aprobo("Biología", "2025-1") is False

def test_estudiante_aprueba_con_nota_alta():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Inglés", 4.5, "2025-1")
    assert estudiante.aprobo("Inglés", "2025-1") is True
    
    
# --- REQ-3: Cálculo de promedio ---

def test_promedio_con_varias_notas():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Matemáticas", 3.0, "2025-1")
    estudiante.registrar_nota("Física", 4.0, "2025-1")
    estudiante.registrar_nota("Química", 5.0, "2025-1")
    assert estudiante.calcular_promedio() == 4.0

def test_promedio_con_una_sola_nota():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Cálculo", 3.5, "2025-1")
    assert estudiante.calcular_promedio() == 3.5

def test_promedio_sin_notas_registradas():
    estudiante = Estudiante("Laura")
    assert estudiante.calcular_promedio() == 0.0
    

# --- REQ-4: No duplicar nota en misma materia y semestre ---

def test_rechazar_nota_duplicada_misma_materia_mismo_semestre():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Cálculo", 3.5, "2025-1")
    with pytest.raises(ValueError):
        estudiante.registrar_nota("Cálculo", 4.0, "2025-1")

def test_permitir_misma_materia_en_semestre_diferente():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Cálculo", 3.5, "2025-1")
    estudiante.registrar_nota("Cálculo", 4.0, "2025-2")
    assert estudiante.notas["2025-2"]["Cálculo"] == 4.0

def test_permitir_materias_distintas_mismo_semestre():
    estudiante = Estudiante("Laura")
    estudiante.registrar_nota("Cálculo", 3.5, "2025-1")
    estudiante.registrar_nota("Física", 4.0, "2025-1")
    assert estudiante.notas["2025-1"]["Física"] == 4.0
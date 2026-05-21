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
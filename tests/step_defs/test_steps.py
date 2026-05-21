import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.registro_notas import Estudiante

scenarios("../features/registro_notas.feature")


@pytest.fixture
def estudiante():
    return Estudiante("Ana")


@given(parsers.parse('un estudiante llamado "{nombre}"'), target_fixture="estudiante")
def estudiante_con_nombre(nombre):
    return Estudiante(nombre)


@when(parsers.parse('registra la nota {nota:f} en "{materia}" para el semestre "{semestre}"'))
def registrar_nota(estudiante, nota, materia, semestre):
    estudiante.registrar_nota(materia, nota, semestre)


@then(parsers.parse('el resultado para "{materia}" en "{semestre}" es que aprueba'))
def verificar_aprueba(estudiante, materia, semestre):
    assert estudiante.aprobo(materia, semestre) is True


@then(parsers.parse('el resultado para "{materia}" en "{semestre}" es que reprueba'))
def verificar_reprueba(estudiante, materia, semestre):
    assert estudiante.aprobo(materia, semestre) is False


@then(parsers.parse("el promedio del estudiante es {esperado:f}"))
def verificar_promedio(estudiante, esperado):
    assert estudiante.calcular_promedio() == esperado


@then(parsers.parse('registrar la nota {nota:f} en "{materia}" para el semestre "{semestre}" lanza un error'))
def verificar_error_duplicado(estudiante, nota, materia, semestre):
    with pytest.raises(ValueError):
        estudiante.registrar_nota(materia, nota, semestre)
# language: es
Feature: Registro de notas académicas
  Como estudiante de la Universidad Regional del Sur
  Quiero registrar mis notas por materia y semestre
  Para conocer mi rendimiento académico y saber si apruebo cada materia

  Background:
    Given un estudiante llamado "Ana"

  @smoke
  Scenario: El estudiante aprueba una materia con nota exactamente en el límite
    When registra la nota 3.0 en "Biología" para el semestre "2025-1"
    Then el resultado para "Biología" en "2025-1" es que aprueba

  @smoke
  Scenario: El estudiante reprueba una materia con nota bajo el límite
    When registra la nota 2.9 en "Historia" para el semestre "2025-1"
    Then el resultado para "Historia" en "2025-1" es que reprueba

  @critical
  Scenario: El sistema calcula el promedio de varias notas
    When registra la nota 3.0 en "Matemáticas" para el semestre "2025-1"
    And registra la nota 4.0 en "Física" para el semestre "2025-1"
    And registra la nota 5.0 en "Química" para el semestre "2025-1"
    Then el promedio del estudiante es 4.0

  @regression
  Scenario: El promedio de un estudiante sin notas es cero
    Then el promedio del estudiante es 0.0

  @critical
  Scenario: El sistema rechaza registrar una nota duplicada en la misma materia y semestre
    When registra la nota 3.5 en "Cálculo" para el semestre "2025-1"
    Then registrar la nota 4.0 en "Cálculo" para el semestre "2025-1" lanza un error

  @regression
  Scenario: Se permite registrar la misma materia en semestres diferentes
    When registra la nota 3.5 en "Cálculo" para el semestre "2025-1"
    And registra la nota 4.0 en "Cálculo" para el semestre "2025-2"
    Then el promedio del estudiante es 3.75

  @regression
  Scenario Outline: El sistema determina correctamente si el estudiante aprueba o reprueba
    When registra la nota <nota> en "<materia>" para el semestre "2025-1"
    Then el resultado para "<materia>" en "2025-1" es que <resultado>

    Examples:
      | nota | materia    | resultado |
      | 5.0  | Inglés     | aprueba   |
      | 3.0  | Arte       | aprueba   |
      | 2.9  | Deportes   | reprueba  |
      | 0.0  | Filosofía  | reprueba  |
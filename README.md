# Registro de Notas Académicas

Sistema para registrar y gestionar notas académicas de estudiantes universitarios.

## Tecnología elegida

- **Lenguaje:** Python 3.11+
- **Gestor de entorno:** venv + pip
- **Tests unitarios:** pytest + pytest-cov
- **BDD:** pytest-bdd con Gherkin
- **CI/CD:** GitHub Actions

**¿Por qué Python?** Permite ciclos TDD rápidos, tiene excelente soporte para BDD con pytest-bdd, y la sintaxis limpia facilita que los tests sean legibles como documentación.

---

## Parte 1 — Análisis previo

### 1.1 Particiones de equivalencia (Requerimiento 1: nota entre 0.0 y 5.0)

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida — rango normal bajo | 0.0 – 2.9 | 2.5 | Nota registrada, estudiante reprueba |
| Válida — rango normal alto | 3.0 – 5.0 | 4.0 | Nota registrada, estudiante aprueba |
| Inválida — por debajo del mínimo | < 0.0 | -1.0 | Error: nota fuera de rango |
| Inválida — por encima del máximo | > 5.0 | 6.0 | Error: nota fuera de rango |
| Inválida — tipo incorrecto | No numérico | "abc" | Error: tipo de dato inválido |

### 1.2 Análisis de valores límite (Requerimiento 1)

| Valor | Posición respecto al límite | Dentro del rango | Resultado esperado |
|---|---|---|---|
| -0.1 | Justo antes del mínimo | No | Error: nota fuera de rango |
| 0.0 | Límite inferior exacto | Sí | Nota registrada correctamente |
| 0.1 | Justo después del mínimo | Sí | Nota registrada correctamente |
| 4.9 | Justo antes del máximo | Sí | Nota registrada correctamente |
| 5.0 | Límite superior exacto | Sí | Nota registrada correctamente |
| 5.1 | Justo después del máximo | No | Error: nota fuera de rango |

### 1.3 Preguntas al Product Owner (Requerimiento 4: no duplicar nota)

**Pregunta 1:** ¿Qué define un "semestre" en el sistema — es un campo explícito que el usuario ingresa (ej. "2025-1"), o el sistema lo determina automáticamente por fecha?

*Justificación:* Si el semestre es un campo libre, dos registros con el mismo nombre de materia pero semestres escritos diferente ("2025-1" vs "2025I") podrían no detectarse como duplicados. Esto cambia completamente cómo diseñar el caso de prueba de duplicado y qué validación implementar.

**Pregunta 2:** Si un estudiante registra una nota incorrecta y necesita corregirla en el mismo semestre, ¿existe un flujo de actualización o siempre se considera un intento de duplicado?

*Justificación:* Si no hay flujo de corrección, el sistema debe ser especialmente claro en el mensaje de error para que el usuario entienda que no puede re-registrar. Si sí existe, necesitamos casos de prueba que distingan entre "duplicado inválido" y "actualización válida", lo cual duplica el conjunto de pruebas del requerimiento 4.

---

## Parte 2 — Casos de prueba

| ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| TC-01 | REQ-1 | Registrar nota válida en rango medio | Estudiante sin notas | materia="Matemáticas", nota=3.5, semestre="2025-1" | 1. Crear estudiante 2. Registrar nota | Nota registrada exitosamente | Positivo |
| TC-02 | REQ-1 | Registrar nota en valor mínimo del rango | Estudiante sin notas | materia="Física", nota=0.0, semestre="2025-1" | 1. Crear estudiante 2. Registrar nota | Nota registrada exitosamente | Borde |
| TC-03 | REQ-1 | Registrar nota en valor máximo del rango | Estudiante sin notas | materia="Química", nota=5.0, semestre="2025-1" | 1. Crear estudiante 2. Registrar nota | Nota registrada exitosamente | Borde |
| TC-04 | REQ-1 | Rechazar nota por debajo del mínimo | Estudiante sin notas | materia="Historia", nota=-0.1, semestre="2025-1" | 1. Crear estudiante 2. Intentar registrar nota | Se lanza ValueError con mensaje claro | Negativo |
| TC-05 | REQ-1 | Rechazar nota por encima del máximo | Estudiante sin notas | materia="Arte", nota=5.1, semestre="2025-1" | 1. Crear estudiante 2. Intentar registrar nota | Se lanza ValueError con mensaje claro | Negativo |
| TC-06 | REQ-2 | Estudiante aprueba con nota exactamente en el límite | Estudiante sin notas | materia="Biología", nota=3.0, semestre="2025-1" | 1. Registrar nota 2. Consultar estado | Retorna "aprueba" | Borde |
| TC-07 | REQ-2 | Estudiante reprueba con nota justo bajo el límite | Estudiante sin notas | materia="Biología", nota=2.9, semestre="2025-1" | 1. Registrar nota 2. Consultar estado | Retorna "reprueba" | Borde |
| TC-08 | REQ-2 | Estudiante aprueba con nota alta | Estudiante sin notas | materia="Inglés", nota=4.5, semestre="2025-1" | 1. Registrar nota 2. Consultar estado | Retorna "aprueba" | Positivo |
| TC-09 | REQ-3 | Calcular promedio con varias notas | Estudiante sin notas | notas=[3.0, 4.0, 5.0] en materias distintas | 1. Registrar 3 notas 2. Calcular promedio | Retorna 4.0 | Positivo |
| TC-10 | REQ-3 | Calcular promedio con una sola nota | Estudiante sin notas | materia="Cálculo", nota=3.5 | 1. Registrar 1 nota 2. Calcular promedio | Retorna 3.5 | Positivo |
| TC-11 | REQ-3 | Calcular promedio sin notas registradas | Estudiante recién creado, sin notas | ninguno | 1. Crear estudiante 2. Calcular promedio | Retorna 0.0 | Negativo |
| TC-12 | REQ-4 | Rechazar nota duplicada en la misma materia y semestre | Estudiante con nota ya registrada en "Cálculo" semestre "2025-1" | materia="Cálculo", nota=4.0, semestre="2025-1" | 1. Registrar primera nota 2. Intentar registrar segunda nota | Se lanza ValueError indicando duplicado | Negativo |
| TC-13 | REQ-4 | Permitir misma materia en semestre diferente | Estudiante con nota en "Cálculo" semestre "2025-1" | materia="Cálculo", nota=4.0, semestre="2025-2" | 1. Registrar nota en 2025-1 2. Registrar nota en 2025-2 | Segunda nota registrada exitosamente | Positivo |
| TC-14 | REQ-4 | Permitir materias distintas en el mismo semestre | Estudiante sin notas | materia1="Cálculo", materia2="Física", semestre="2025-1" | 1. Registrar nota en Cálculo 2. Registrar nota en Física | Ambas notas registradas correctamente | Positivo |

---

## Parte 3 — Cobertura de tests

Output final del reporte de cobertura:

```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
src\__init__.py             0      0   100%
src\registro_notas.py      27      2    93%   15, 32
-----------------------------------------------------
TOTAL                      27      2    93%
```

14 tests pasando. Cobertura total: **93%** (supera el mínimo requerido del 85%).
---

## Reflexión final

Diseñar los casos de prueba en la tabla antes de escribir código obligó a pensar en el sistema desde afuera hacia adentro: primero qué debe hacer, luego cómo hacerlo. Eso reveló situaciones que probablemente se habrían ignorado al programar directamente, como el caso del estudiante sin notas o la misma materia en semestres diferentes. Arrancar a codear sin ese análisis hubiera producido una implementación que pasa los casos "obvios" pero falla en los bordes.

Lo más difícil del ciclo TDD fue respetar la fase RED sin escribir nada de implementación antes del commit. La tentación aparece exactamente ahí: cuando escribes el test y ya sabes cómo resolverlo, el impulso natural es implementarlo de una vez. Saltarse el commit RED haría que el historial no evidenciara el proceso, que es precisamente lo que el ciclo busca demostrar — que el test existió antes que el código.
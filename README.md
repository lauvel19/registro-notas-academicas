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

*(se completará en el siguiente commit)*

---

## Parte 3 — Cobertura de tests

*(se completará al finalizar el ciclo TDD)*

---

## Reflexión final

*(se completará al terminar la actividad)*
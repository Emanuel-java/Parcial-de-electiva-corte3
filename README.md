# Sistema de Gestión de Calificaciones

Este repositorio contiene un script de automatización en Python para el cálculo de promedios académicos y asignación de escalas de evaluación, validado mediante un pipeline de CI.

## Estrategia de Integración Continua (CI)

El flujo de trabajo definido en GitHub Actions valida cada cambio bajo los siguientes criterios de calidad:

1.  **Auditoría Estática (Linting):** Se utiliza `Pylint` para evaluar la calidad sintáctica. A diferencia de otros linters, Pylint asigna una puntuación numérica (0-10); el pipeline exige mantener una calidad superior a 8.0.
2.  **Pruebas Unitarias:** Ejecutadas con el framework nativo `unittest`, lo que garantiza compatibilidad sin dependencias externas pesadas.
3.  **Cobertura:** Se utiliza `coverage.py` para asegurar que al menos el 80% de las sentencias lógicas sean verificadas por los tests.

## Ejecución Local

Para correr las pruebas y verificar la cobertura en cualquier máquina:

```bash
coverage run -m unittest test_notas.py
coverage report -m
# Sistema de Gestión de Calificaciones

Script de automatización para el cálculo de promedios académicos y asignación de escalas de evaluación.

## Integración Continua (CI)

Este repositorio cuenta con un pipeline automatizado en GitHub Actions que valida cada cambio bajo los siguientes criterios:

1.  **Auditoría Estática:** Se utiliza `Pylint` para evaluar la calidad sintáctica y detectar "code smells". Se exige una puntuación mínima de 8.0/10.0 en la calidad del código.
2.  **Pruebas Unitarias:** Ejecutadas con el framework nativo `unittest`.
3.  **Cobertura:** Se requiere validar al menos el 80% de las sentencias lógicas mediante la herramienta `coverage.py`.

## Ejecución Local

Para correr las pruebas en su máquina:

```bash
python -m unittest test_notas.py
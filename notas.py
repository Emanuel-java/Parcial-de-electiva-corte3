

def estado_estudiante(promedio):
    """Determina si aprueba o reprueba."""
    if promedio >= 3.0:
        return "APROBADO"
    return "REPROBADO"

def obtener_letra(promedio):
    """Asigna una letra según el sistema americano."""
    if promedio >= 4.5:
        return 'A'
    elif promedio >= 3.5:
        return 'B'
    else:
        return 'C'
def leer_ventas():
    return [120.0, 50.5, 300.0, 89.9, 40.0]

def validar_montos(montos):
    """Valida que los montos sean >= 0"""
    return [m for m in montos if m >= 0]

def generar_reporte(montos):
    if not montos:
        return {"total": 0, "cantidad": 0, "promedio": 0, "max": 0, "min": 0}

    total = sum(montos)
    cantidad = len(montos)
    promedio = total / cantidad

    return {
        "total": round(total, 2),
        "cantidad": cantidad,
        "promedio": round(promedio, 2),
        "max": max(montos),
        "min": min(montos)
    }
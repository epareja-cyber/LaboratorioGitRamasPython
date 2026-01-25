def leer_ventas():
    return [120.0, 50.5, 300.0, 89.9, 40.0]

def validar_montos(montos):
    """TODO: validar montos >= 0"""
    return montos

def generar_reporte(montos):
    """TODO: total, cantidad, promedio, max, min"""
    return {"total": 0, "cantidad": 0, "promedio": 0, "max": 0, "min": 0}

if __name__ == "__main__":
    ventas = leer_ventas()
    ventas = validar_montos(ventas)
    reporte = generar_reporte(ventas)
    print("REPORTE:", reporte)
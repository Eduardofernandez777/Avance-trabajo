class Inventario():
    def __init__(self, item, nombre, cantidad, precio, categoria):
        self.item = item
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria

PELLET_OVEJA = Inventario(10010, "PELLET OVEJA", 150, 12000, "ALIMENTOS")
PESTICIDA_MOSCA = Inventario(10011, "PESTICIDA PARA MOSCAS", 70, 7500, "PESTICIDAS")
ABONO_TIERRA = Inventario(10012, "ABONO PARA LA TIERRA", 100, 8000, "ABONOS")




print(f"Quedan: {PELLET_OVEJA.cantidad} sacos de alimento")
print(f"Quedan: {PESTICIDA_MOSCA.cantidad} botellas de pesticida")
print(f"Quedan: {ABONO_TIERRA.cantidad} sacos de abono")




class Empresa:
    def __init__(self, nombre, rut, telefono, email, direccion, comuna, impuesto, ingreso, egreso, giro):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.comuna = comuna
        self.impuesto = impuesto
        self.ingreso = ingreso
        self.egreso = egreso
        self.giro = giro

obj_Empresa = Empresa( f"DisFer", "77.892.067-7", "9 8760 0671", " lalo17@gmail.com", "Picarte 123", "Valdivia", 0.19, 1000000, 250000, "MANUFACTURA DE ALIMENTOS NATURALES")


print(f"Empresa: {obj_Empresa.nombre} LTDA")
print(f"Rut: {obj_Empresa.rut}")
print(f"Telefono: {obj_Empresa.telefono}")
print(f"Direccion: {obj_Empresa.direccion}")
print(f"Comuna: {obj_Empresa.comuna}")
print(f"Giro: {obj_Empresa.giro}")

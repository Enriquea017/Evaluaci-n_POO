class Alojamiento:

    def __init__(self, nombre, tipo, precio, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.capacidad = capacidad

    def mostrar_info(self):
        return f"Alojamiento: {self.nombre}, Tipo: {self.tipo}, Precio: ${self.precio}, Capacidad: {self.capacidad} personas."


    # Reglas (léelas con atención, no son solo "rellenar")
    # 1. mostrar_info()

    # Debe devolver (no imprimir) una cadena de texto con la información
    # del alojamiento, en un formato legible y consistente.
    # El precio debe verse como moneda y la capacidad como número de personas.

    def precio_por_persona(self):
        # Valida si el precio o la capacidad son 0 o negativos
        if self.precio <= 0 or self.capacidad <= 0:
            return None
        
        # Calcula y redondea el precio por persona a 2 decimales
        precio_individual = self.precio / self.capacidad
        return round(precio_individual, 2)
    # 2. precio_por_persona()

    # Debe devolver el precio que corresponde pagar por persona.
    # Si precio o capacidad no son válidos (capacidad o precio <= 0), 
    # no debe lanzar error: debe devolver None.
    # El resultado debe estar redondeado a 2 decimales.


# Objeto 1
casa = Alojamiento(
    "Casa Centro",
    "Casa",
    1800,
    6
)

# Objeto 2
departamento = Alojamiento(
    "Departamento Reforma",
    "Departamento",
    1200,
    4
)


# Completa las instrucciones necesarias para:
# 1. Mostrar la información de la casa.
print(casa.mostrar_info())
# 2. Mostrar el precio por persona de la casa.
print(f"Precio por persona de la casa: ${casa.precio_por_persona()}")
# 3. Mostrar la información del departamento.
print(departamento.mostrar_info())
# 4. Mostrar el precio por persona del departamento.
print(f"Precio por persona del departamento: ${departamento.precio_por_persona()}")

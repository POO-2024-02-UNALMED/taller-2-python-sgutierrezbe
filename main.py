class Auto:
    cantidadCreados = 0  # Initialize the class variable

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1  # Increment the class variable

    def cantidadAsientos(self):
        count = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                count += 1
        return count

    def verificarIntegridad(self):
        registros_asientos = set(
            asiento.registro for asiento in self.asientos if isinstance(asiento, Asiento)
        )
        if len(registros_asientos) == 1 and self.registro == self.motor.registro == registros_asientos.pop():
            return "Auto original"
        else:
            return "Las piezas no son originales"


class Motor:
    def __init__(self, cilindros, tipo, registro):
        self.cilindros = cilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        tipos_permitidos = ["gasolina", "electrico"]
        if nuevoTipo in tipos_permitidos:
            self.tipo = nuevoTipo


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, nuevo_color):
        colores_permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if nuevo_color in colores_permitidos:
            self.color = nuevo_color

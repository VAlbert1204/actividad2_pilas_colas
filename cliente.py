class Cliente:
    def __init__(self, nombre, documento, telefono, tipo_cita, prioridad, fecha, hora):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.tipo_cita = tipo_cita
        self.prioridad = prioridad
        self.fecha = fecha
        self.hora = hora

    def mostrar(self):
        texto = "Nombre: " + self.nombre
        texto = texto + " | Documento: " + self.documento
        texto = texto + " | Telefono: " + self.telefono
        texto = texto + " | Cita: " + self.tipo_cita
        texto = texto + " | Prioridad: " + self.prioridad
        texto = texto + " | Fecha: " + self.fecha
        texto = texto + " | Hora: " + self.hora
        return texto

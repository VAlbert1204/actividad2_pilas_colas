class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop(0)

    def frente(self):
        if self.esta_vacia():
            return None
        return self.elementos[0]

    def esta_vacia(self):
        if len(self.elementos) == 0:
            return True
        else:
            return False

    def tamano(self):
        return len(self.elementos)

    def listar(self):
        lista = []
        i = 0
        while i < len(self.elementos):
            lista.append(self.elementos[i])
            i = i + 1
        return lista

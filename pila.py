class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.elementos.pop()

    def cima(self):
        if self.esta_vacia():
            return None
        return self.elementos[-1]

    def esta_vacia(self):
        if len(self.elementos) == 0:
            return True
        else:
            return False

    def tamano(self):
        return len(self.elementos)

    def listar_desde_cima(self):
        lista = []
        i = len(self.elementos) - 1
        while i >= 0:
            lista.append(self.elementos[i])
            i = i - 1
        return lista

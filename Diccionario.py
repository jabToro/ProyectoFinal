class Termino:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

    def __str__(self):
        return f"{self.palabra}: {self.definicion}"

# Almacenar datos en arbol binario
class ABB:
    class Nodo:
        def __init__(self, termino):
            self.termino = termino
            self.izquierda = None
            self.derecha = None

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra, definicion):
        nuevo_termino = Termino(palabra, definicion)
        if self.raiz is None:
            self.raiz = self.Nodo(nuevo_termino)
        else:
            self._insertar(nuevo_termino, self.raiz)

    def _insertar(self, termino, nodo_actual):
        if termino.palabra < nodo_actual.termino.palabra:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = self.Nodo(termino)
            else:
                self._insertar(termino, nodo_actual.izquierda)
        elif termino.palabra > nodo_actual.termino.palabra:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = self.Nodo(termino)
            else:
                self._insertar(termino, nodo_actual.derecha)

    def buscar(self, palabra):
        return self._buscar(palabra, self.raiz)

    def _buscar(self, palabra, nodo_actual):
        if nodo_actual is None:
            return None
        if palabra == nodo_actual.termino.palabra:
            return nodo_actual.termino.definicion
        elif palabra < nodo_actual.termino.palabra:
            return self._buscar(palabra, nodo_actual.izquierda)
        else:
            return self._buscar(palabra, nodo_actual.derecha)

    def listar(self):
        terminos = []
        self._listar(self.raiz, terminos)
        return [termino.palabra for termino in terminos]

    def _listar(self, nodo_actual, terminos):
        if nodo_actual is not None:
            self._listar(nodo_actual.izquierda, terminos)
            terminos.append(nodo_actual.termino)
            self._listar(nodo_actual.derecha, terminos)
            
# Terminos frecuentes (Tabla de hash)
class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar(self, palabra, definicion):
        self.tabla[palabra] = definicion

    def buscar(self, palabra):
        return self.tabla.get(palabra, None)

    def listar(self):
        return list(self.tabla.keys())
    
# Diccionario de programación
class DiccionarioProgramacion:
    def __init__(self):
        self.arbol = ABB()
        self.tabla_hash = TablaHash()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        # Datos iniciales (10 términos de programación)
        terminos = [
            ("clase", "Plantilla para crear objetos en POO."),
            ("objeto", "Instancia de una clase."),
            ("loop", "Estructura que repite un bloque de código."),
            ("variable", "Espacio en memoria que almacena un valor."),
            ("función", "Bloque de código reutilizable."),
            ("API", "Interfaz para comunicación entre software."),
            ("herencia", "Mecanismo para reutilizar atributos de una clase."),
            ("polimorfismo", "Capacidad de un objeto de tomar múltiples formas."),
            ("algoritmo", "Conjunto ordenado de pasos para resolver un problema."),
            ("sintaxis", "Reglas para escribir código correctamente.")
        ]
        for palabra, definicion in terminos:
            self.arbol.insertar(palabra, definicion)

        # Términos frecuentes (5 ejemplos)
        frecuentes = ["clase", "loop", "variable", "función", "API"]
        for palabra in frecuentes:
            definicion = self.arbol.buscar(palabra)
            if definicion:
                self.tabla_hash.agregar(palabra, definicion)

    def buscar(self, palabra):
        return self.arbol.buscar(palabra)

    def listar_todos(self):
        return self.arbol.listar()

    def listar_frecuentes(self):
        return self.tabla_hash.listar()

    def obtener_definicion_frecuente(self, palabra):
        return self.tabla_hash.buscar(palabra)



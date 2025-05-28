# Organiza la información básica de cada término
class Termino:
    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

    def __str__(self):
        return f"{self.palabra}: {self.definicion}"

# Organiza los términos como un árbol donde cada palabra se coloca en orden alfabético. Y Las palabras "menores" van a la izquierda, las "mayores" a la derecha
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
        return self._buscar(palabra.lower(), self.raiz)

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

# Es como una agenda de contactos rápida para los 10 términos más usados. Esto es para no tener las palabras más comunes sin necesidad de recorrer nuevamente el arbol.
class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar(self, palabra, definicion):
        self.tabla[palabra] = definicion

    def buscar(self, palabra):
        return self.tabla.get(palabra, None)

    def listar(self):
        return list(self.tabla.keys())

# Es el cerebro del programa. Carga los 30 términos al iniciar y basicamente une todo para que funcione como un diccionario real.
class DiccionarioProgramacion:
    def __init__(self):
        self.arbol = ABB()
        self.tabla_hash = TablaHash()
        self._cargar_datos_iniciales()

    def _cargar_datos_iniciales(self):
        # Términos de programación (30 en total)
        terminos = [
            # Fundamentos
            ("algoritmo", "Conjunto ordenado de pasos para resolver un problema."),
            ("variable", "Espacio en memoria que almacena un valor."),
            ("función", "Bloque de código reutilizable que realiza una tarea."),
            ("sintaxis", "Reglas que definen cómo escribir código correctamente."),
            ("compilador", "Programa que traduce código fuente a lenguaje máquina."),
            
            # POO
            ("clase", "Plantilla para crear objetos en programación orientada a objetos."),
            ("objeto", "Instancia de una clase."),
            ("herencia", "Mecanismo donde una clase adquiere atributos de otra."),
            ("polimorfismo", "Capacidad de un objeto de tomar muchas formas."),
            ("encapsulamiento", "Ocultamiento de los detalles internos de un objeto."),
            
            # Estructuras de datos
            ("array", "Colección ordenada de elementos del mismo tipo."),
            ("lista", "Estructura de datos que almacena elementos de manera secuencial."),
            ("pila", "Estructura LIFO (Last In, First Out)."),
            ("cola", "Estructura FIFO (First In, First Out)."),
            ("grafo", "Conjunto de nodos conectados por aristas."),
            
            # Bases de datos
            ("SQL", "Lenguaje para gestionar bases de datos relacionales."),
            ("tabla", "Estructura que organiza datos en filas y columnas."),
            ("clave primaria", "Identificador único de un registro en una tabla."),
            ("índice", "Estructura que mejora la velocidad de búsqueda en una tabla."),
            ("transacción", "Secuencia de operaciones atómicas en una base de datos."),
            
            # Web
            ("API", "Interfaz para comunicación entre componentes de software."),
            ("HTTP", "Protocolo para transferencia de hipertexto en la web."),
            ("JSON", "Formato ligero para intercambio de datos."),
            ("frontend", "Parte de una aplicación que interactúa con el usuario."),
            ("backend", "Parte de una aplicación que procesa datos en el servidor."),
            
            # Otros
            ("debug", "Proceso de identificar y corregir errores en el código."),
            ("git", "Sistema de control de versiones distribuido."),
            ("loop", "Estructura que repite un bloque de código."),
            ("recursión", "Función que se llama a sí misma."),
            ("framework", "Conjunto de herramientas para desarrollar software.")
        ]

        # Insertar todos los términos en el ABB
        for palabra, definicion in terminos:
            self.arbol.insertar(palabra.lower(), definicion)

        # Términos frecuentes (10 ejemplos)
        frecuentes = ["clase", "objeto", "funcion", "variable", "api", "sql", "loop", "array", "debug", "git"]
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

# Menu que se muestra al ejecutar el programa. Permite al usuario buscar definiciones, listar palabras y mostrar términos frecuentes.
class Consola:
    def __init__(self):
        self.diccionario = DiccionarioProgramacion()

    def mostrar_menu(self):
        print("\n--- Diccionario de Programación ---")
        print("1. Buscar definición")
        print("2. Listar todas las palabras")
        print("3. Mostrar términos frecuentes")
        print("4. Salir")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                palabra = input("Ingrese la palabra: ").strip().lower()
                definicion = self.diccionario.buscar(palabra)
                if definicion:
                    print(f"Definición de '{palabra}': {definicion}")
                else:
                    print(f"La palabra '{palabra}' no existe. Prueba con: {', '.join(self.diccionario.listar_frecuentes()[:3])}...")

            elif opcion == "2":
                palabras = self.diccionario.listar_todos()
                print("Palabras disponibles (orden alfabético):")
                for palabra in palabras:
                    print(f"- {palabra}")

            elif opcion == "3":
                frecuentes = self.diccionario.listar_frecuentes()
                print("Términos frecuentes:")
                for palabra in frecuentes:
                    definicion = self.diccionario.obtener_definicion_frecuente(palabra)
                    print(f"- {palabra}: {definicion}")
 
            elif opcion == "4":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

# Es como el inicio del programa. Crea una instancia de la consola y comienza a interactuar con el usuario.
if __name__ == "__main__":
    consola = Consola()
    consola.iniciar()
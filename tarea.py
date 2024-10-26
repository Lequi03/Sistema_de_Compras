class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")
        
    def quitar_unidad(self):
        if self.cantidad > 0:
            self.cantidad -= 1
        else:
            print(f'No hay más unidades de {self.nombre}')
            
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")
        
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
        
class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def quitar_prenda(self, prenda):
        for p in self.prendas:
            if p.nombre == prenda.nombre:  # Busca la prenda por nombre
                p.quitar_unidad()  # Llama al método para descontar
                return
        print("La prenda no se encuentra en el inventario")

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda

#Creamos instancias para RopaHombre
Camisa = RopaHombre("Camisa para Hombre", 80000, 10, "G")
Pantalon = RopaHombre("Pantalón para Hombre", 120000, 15, "XG")
Remera = RopaHombre("Remera para Hombre", 40000, 20, "G")
Short = RopaHombre("Short para Hombre", 35000, 20, "G")
#Creamos instancias para RopaMujer
Vestido = RopaMujer("Vestido para Mujer", 130000, 10, "M")
Falda = RopaMujer("Falda para Mujer", 70000, 12, "S")
Blusa = RopaMujer("Blusa para Mujer", 40000, 20, "M")
ShortM = RopaMujer("Short para Mujer", 30000, 20, "S")
inventario = Inventario()
inventario.agregar_prenda(Camisa)
inventario.agregar_prenda(Pantalon)
inventario.agregar_prenda(Remera)
inventario.agregar_prenda(Short)
inventario.agregar_prenda(Vestido)
inventario.agregar_prenda(Falda)
inventario.agregar_prenda(Blusa)
inventario.agregar_prenda(ShortM)

def seleccionar_prenda(inventario):
    # Iniciamos un bucle infinito para que el menú se muestre hasta que el usuario decida salir
    while True:
        # Mostramos el menú principal con las opciones disponibles
        print("SISTEMA DE COMPRA DE ROPAS")
        print("1. Ver inventario completo")
        print("2. Seleccionar una prenda")
        print("3. Salir")
        
        # Solicitamos al usuario que elija una opción
        opcion = input("\nSeleccione una opción (1-3): ")
        print("-" * 20)
        
        if opcion == "1":
            # Si elige 1, mostramos todo el inventario usando el método que ya existía
            print("INVENTARIO ACTUAL")
            inventario.mostrar_inventario()
            
        elif opcion == "2":
            # Si elige 2, mostramos la lista de prendas numeradas para facilitar la selección
            print("\nPrendas disponibles:")
            # enumerate(inventario.prendas, 1) numera las prendas empezando desde 1
            for i, prenda in enumerate(inventario.prendas, 1):
                print(f"{i}. {prenda.nombre} (Stock: {prenda.cantidad})")
            
            try:
                # Solicitamos el número de la prenda que desea seleccionar
                seleccion = int(input("\nIngrese el número de la prenda que desea comprar: "))
                print("-" * 20)
                # Verificamos que el número esté dentro del rango válido
                if 1 <= seleccion <= len(inventario.prendas):
                    # Obtenemos la prenda seleccionada (restamos 1 porque las listas empiezan en 0)
                    prenda_seleccionada = inventario.prendas[seleccion - 1]
                    # Verificamos si hay stock disponible
                    if prenda_seleccionada.cantidad > 0:
                        # Descontamos una unidad usando el método existente
                        inventario.quitar_prenda(prenda_seleccionada)
                        print(f"Compra realizada, se ha seleccionado: {prenda_seleccionada.nombre}")
                        print("-" * 20)
                    else:
                        print(f"\nNo hay stock disponible de {prenda_seleccionada.nombre}")
                else:
                    print("\nNúmero de prenda inválido")
                    print("-" * 20)
            # Capturamos el error si el usuario ingresa algo que no es un número
            except ValueError:
                print("\nPor favor, ingrese un número válido")
                print("-" * 20)
                
        elif opcion == "3":
            # Si elige 3, salimos del bucle y terminamos el programa
            print("\nGracias por usar el sistema de selección de prendas")
            print("-" * 20)
            break
            
        else:
            # Si ingresa una opción no válida, mostramos un mensaje de error
            print("\nOpción inválida. Por favor, seleccione una opción válida")
            print("-" * 20)

# Esta línea inicia el sistema llamando a la función
seleccionar_prenda(inventario)
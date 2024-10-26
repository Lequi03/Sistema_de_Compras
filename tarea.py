from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    # Getters y setters para encapsulamiento
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad

    @abstractmethod
    def mostrar_info(self):
        pass

class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, material):
        super().__init__(nombre, precio, cantidad)
        self._material = material

    @property
    def material(self):
        return self._material

    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Precio: ${self._precio}, Stock: {self._cantidad}, Material: {self._material}"

class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, material, talla, tipo_manga):
        super().__init__(nombre, precio, cantidad, material)
        self._talla = talla
        self._tipo_manga = tipo_manga

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}, Tipo de Manga: {self._tipo_manga}"

class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, material, talla, estilo):
        super().__init__(nombre, precio, cantidad, material)
        self._talla = talla
        self._estilo = estilo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}, Estilo: {self._estilo}"

class Zapato(Ropa):
    def __init__(self, nombre, precio, cantidad, material, talla, tipo):
        super().__init__(nombre, precio, cantidad, material)
        self._talla = talla
        self._tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self._talla}, Tipo: {self._tipo}"

class Carrito:
    def __init__(self):
        self._items = []
        self._total = 0

    def agregar_producto(self, producto):
        if producto.cantidad > 0:
            self._items.append(producto)
            self._total += producto.precio
            return True
        return False

    def remover_producto(self, producto):
        if producto in self._items:
            self._items.remove(producto)
            self._total -= producto.precio
            return True
        return False

    def obtener_total(self):
        return self._total

    def obtener_items(self):
        return self._items

    def limpiar_carrito(self):
        self._items.clear()
        self._total = 0

class Tienda:
    def __init__(self):
        self._inventario = []
        self._carrito = Carrito()

    def agregar_producto(self, producto):
        self._inventario.append(producto)

    def mostrar_inventario(self):
        for i, producto in enumerate(self._inventario, 1):
            print(f"{i}. {producto.mostrar_info()}")

    def comprar_producto(self, indice):
        if 0 <= indice < len(self._inventario):
            producto = self._inventario[indice]
            if self._carrito.agregar_producto(producto):
                producto.cantidad -= 1
                return True
        return False

    def mostrar_carrito(self):
        items = self._carrito.obtener_items()
        if not items:
            print("\nEl carrito está vacío")
            print("-" * 20)
            return False

        print("\nCARRITO ACTUAL")
        print("-" * 20)
        for i, item in enumerate(items, 1):
            print(f"{i}. {item.mostrar_info()}")
        print(f"\nTotal actual: ${self._carrito.obtener_total()}")
        return True

    def quitar_del_carrito(self, indice):
        items = self._carrito.obtener_items()
        if 0 <= indice < len(items):
            producto = items[indice]
            if self._carrito.remover_producto(producto):
                # Devolvemos la unidad al inventario
                for prod in self._inventario:
                    if prod.nombre == producto.nombre:
                        prod.cantidad += 1
                        break
                return True
        return False

    def finalizar_compra(self):
        items = self._carrito.obtener_items()
        if not items:
            return False

        print("\nRESUMEN DE COMPRA")
        for item in items:
            print(item.mostrar_info())
        print(f"\nTotal a pagar: ${self._carrito.obtener_total()}")
        self._carrito.limpiar_carrito()
        return True

def inicializar_tienda():
    tienda = Tienda()

    # Agregamos algunos productos de ejemplo
    camisa1 = Camisa("Camisa Casual", 80000, 10, "Algodón", "M", "Manga Corta")
    camisa2 = Camisa("Camisa Formal", 95000, 8, "Lino", "L", "Manga Larga")
    pantalon1 = Pantalon("Jeans Clásico", 120000, 15, "Denim", "32", "Regular")
    zapatos1 = Zapato("Zapatos Casuales", 150000, 5, "Cuero", "42", "Sneakers")

    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(camisa2)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapatos1)

    return tienda

def menu_tienda():
    tienda = inicializar_tienda()

    while True:
        print("\nTIENDA DE ROPA")
        print("1. Ver inventario")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Quitar producto del carrito")
        print("5. Finalizar compra")
        print("6. Salir")

        opcion = input("\nSeleccione una opción (1-6): ")
        print("-" * 20)

        if opcion == "1":
            print("\nINVENTARIO DISPONIBLE")
            tienda.mostrar_inventario()

        elif opcion == "2":
            print("\nPRODUCTOS DISPONIBLES")
            tienda.mostrar_inventario()
            try:
                indice = int(input("\nIngrese el número del producto que desea comprar: ")) - 1
                print("-" * 20)
                if tienda.comprar_producto(indice):
                    print("Producto agregado al carrito exitosamente")
                    print("-" * 20)
                else:
                    print("No se pudo agregar el producto. Verifique el stock disponible.")
                    print("-" * 20)
            except ValueError:
                print("Por favor ingrese un número válido")
                print("-" * 20)

        elif opcion == "3":
            tienda.mostrar_carrito()

        elif opcion == "4":
            if tienda.mostrar_carrito():
                try:
                    indice = int(input("\nIngrese el número del producto que desea quitar del carrito: ")) - 1
                    print("-" * 20)
                    if tienda.quitar_del_carrito(indice):
                        print("Producto removido del carrito exitosamente")
                        print("-" * 20)
                    else:
                        print("No se pudo quitar el producto. Verifique el número ingresado.")
                        print("-" * 20)
                except ValueError:
                    print("Por favor ingrese un número válido")
                    print("-" * 20)

        elif opcion == "5":
            if not tienda.finalizar_compra():
                print("El carrito está vacío")
                print("-" * 20)

        elif opcion == "6":
            if tienda._carrito.obtener_items():
                confirmar = input("\nTienes productos en el carrito. ¿Seguro que deseas salir? (S/N): ")
                print("-" * 20)
                if confirmar.upper() != 'S':
                    continue
            print("\n¡Gracias por su visita!")
            print("-" * 20)
            break

        else:
            print("\nOpción inválida")
            print("-" * 20)

if __name__ == "__main__":
    menu_tienda()

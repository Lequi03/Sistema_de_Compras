# Tienda de Ropa POO Bootcamp

Este proyecto implementa un sistema de tienda de ropa utilizando Programación Orientada a Objetos en Python.

## Estructura del Proyecto

El proyecto implementa los siguientes componentes principales:

### Clases Base
- `Producto`: Clase abstracta base para todos los productos
- `Ropa`: Clase base para productos de vestir
- `Carrito`: Maneja los productos seleccionados
- `Tienda`: Gestiona el inventario y las compras

### Clases de Productos Específicos
- `Camisa`: Productos tipo camisa
- `Pantalon`: Productos tipo pantalón
- `Zapato`: Productos tipo calzado

## Características Principales

1. **Encapsulamiento**
   - Todos los atributos están protegidos (prefix `_`)
   - Implementación de getters y setters
   - Validación de datos en setters

2. **Herencia**
   - Jerarquía de clases: Producto -> Ropa -> [Camisa/Pantalon/Zapato]
   - Reutilización de código a través de `super()`

3. **Polimorfismo**
   - Método `mostrar_info()` implementado de forma específica en cada clase
   - Uso de métodos abstractos

4. **Abstracción**
   - Interface de usuario simplificada
   - Lógica de negocio encapsulada en clases

## Uso del Sistema

1. Ver inventario disponible
2. Agregar productos al carrito
3. Ver productos en el carrito
4. Eliminar productos del carrito
5. Finalizar compra y ver resumen
6. Sistema de gestión de stock automático


## Cómo Ejecutar

```bash
python main.py
```

## Requisitos

- Python 3.x

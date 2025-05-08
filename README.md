
# Sistema de Compras y Sistema de Inventario

Este proyecto está compuesto por dos partes principales:
1. **Sistema de Compras de Snacks**
2. **Sistema de Inventario de Productos**

## 📦 Sistema de Compras de Snacks

Permite al usuario:
- Ver una lista de snacks disponibles.
- Comprar snacks, los cuales se agregan a un ticket de compra.
- Eliminar snacks del ticket.
- Ver el ticket de compra con el total actualizado.

### Variables globales utilizadas:
- `lista_snacks`: Lista con los snacks disponibles.
- `lista_copmra`: Lista que almacena los snacks comprados (¡contiene un typo, debería ser `lista_compra`!).
- `total`: Suma total del ticket.

### Funciones principales:
- `elegir_snack()`: Muestra los snacks disponibles.
- `comprar_snack()`: Permite al usuario comprar un snack por ID.
- `eliminar_snack()`: Elimina un snack comprado según su ID.
- `mostrar_ticket()`: Muestra los productos comprados y el total acumulado.

---

## 🧾 Sistema de Inventario de Productos

Permite:
- Mostrar el inventario.
- Agregar nuevos productos con ID, nombre, precio y cantidad.
- Buscar productos por ID.

### Variables utilizadas:
- `inventario`: Diccionario que contiene productos con su información.

### Funciones principales:
- `mostrar_inventario()`: Muestra todos los productos almacenados.
- `agregar_producto()`: Permite agregar un nuevo producto si el ID no está repetido.
- `buscar_producto()`: Busca un producto por ID.

---

## 💡 Recomendaciones de mejora
- Corregir el nombre `lista_copmra` a `lista_compra`.
- Modularizar el código en funciones separadas y usar clases si se amplía el proyecto.
- Validar mejor las entradas del usuario para evitar errores.

---

## 🚀 Cómo ejecutar

1. Abre el archivo `.py` con Python 3.x instalado.
2. Ejecuta el programa desde la terminal:
```bash
python nombre_del_archivo.py
```
3. Sigue las instrucciones en pantalla.

---

Desarrollado como ejercicio práctico de lógica y estructuras en Python.

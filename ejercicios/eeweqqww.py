import json

# Contenido del notebook
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Ejercicios: comentarios en Python\n",
    "En este notebook practicarás cómo usar comentarios de línea y de bloque en Python para hacer tu código más claro."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Recordatorio rápido\n",
    "- Comentario de línea: empieza con `#` y Python ignora todo lo que hay detrás.\n",
    "- Comentario de bloque: se escribe entre `\"\"\"` o `'''` y suele usarse para explicar un programa, una función o un bloque de código."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ":::{exercise}\n",
    ":label: comentarios-ejercicio-1\n",
    ":class: ejercicio-practico\n",
    "\n",
    "**Objetivo:** Usar comentarios de línea para explicar una instrucción sencilla.\n",
    "\n",
    "**Instrucciones:**\n",
    "1. Escribe una instrucción `print()` que muestre tu nombre y tu curso (por ejemplo, \"2º Bachillerato\").\n",
    "2. Añade un comentario de línea antes o al final explicando claramente qué hace esa instrucción.\n",
    "\n",
    "```\n",
    "# Escribe tu código abajo\n",
    "```\n",
    ":::"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Muestra mi nombre y mi curso por pantalla\n",
    "print(\"Ana, 2º Bachillerato\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ":::{exercise}\n",
    ":label: comentarios-ejercicio-2\n",
    ":class: ejercicio-practico\n",
    "\n",
    "**Objetivo:** Añadir comentarios de línea en varios pasos de un pequeño programa.\n",
    "\n",
    "**Instrucciones:**\n",
    "1. Escribe un programa que:\n",
    "   - Defina dos números enteros.\n",
    "   - Calcule su suma y su producto.\n",
    "   - Muestre ambos resultados por pantalla.\n",
    "2. Añade comentarios de línea que expliquen qué hace cada bloque importante (declaración de variables, operaciones y `print()`).\n",
    "\n",
    "```\n",
    "# Escribe tu código abajo\n",
    "```\n",
    ":::"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definimos dos números enteros\n",
    "a = 10\n",
    "b = 4\n",
    "\n",
    "# Calculamos la suma y el producto\n",
    "suma = a + b\n",
    "producto = a * b\n",
    "\n",
    "# Mostramos los resultados por pantalla\n",
    "print(\"La suma es:\", suma)\n",
    "print(\"El producto es:\", producto)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ":::{exercise}\n",
    ":label: comentarios-ejercicio-3\n",
    ":class: ejercicio-practico\n",
    "\n",
    "**Objetivo:** Usar un comentario de bloque (docstring) para describir un programa.\n",
    "\n",
    "**Instrucciones:**\n",
    "1. Escribe un programa que calcule el área de un triángulo de base 6 y altura 4.\n",
    "2. Antes del código, añade un comentario de bloque (con `\"\"\"`) que explique:\n",
    "   - Qué problema resuelve el programa.\n",
    "   - Qué fórmula utiliza.\n",
    "3. Al final, muestra el área por pantalla con un mensaje claro.\n",
    "\n",
    "```\n",
    "# Escribe tu código abajo\n",
    "```\n",
    ":::"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "Este programa calcula el área de un triángulo.\n",
    "Usa la fórmula: área = (base * altura) / 2.\n",
    "\"\"\"\n",
    "base = 6\n",
    "altura = 4\n",
    "area = (base * altura) / 2\n",
    "print(\"El área del triángulo es:\", area)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ":::{exercise}\n",
    ":label: comentarios-ejercicio-4\n",
    ":class: ejercicio-practico\n",
    "\n",
    "**Objetivo:** Mejorar la claridad de un código usando comentarios adecuados y corrigiendo comentarios confusos.\n",
    "\n",
    "**Instrucciones:**\n",
    "1. Observa el siguiente código mal comentado:\n",
    "   ```\n",
    "   # resta dos números\n",
    "   precio = 15\n",
    "   cantidad = 2\n",
    "   # aquí dividimos\n",
    "   total = precio * cantidad\n",
    "   print(total) # imprime la suma\n",
    "   ```\n",
    "2. Reescribe el programa corrigiendo los comentarios para que describan correctamente lo que hace cada línea o bloque.\n",
    "3. Mantén el mismo código, solo cambia y mejora los comentarios.\n",
    "\n",
    "```\n",
    "# Escribe tu versión corregida abajo\n",
    "```\n",
    ":::"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calcula el precio total de una compra\n",
    "precio = 15  # Precio por unidad\n",
    "cantidad = 2  # Número de unidades compradas\n",
    "\n",
    "# Calculamos el total multiplicando precio por cantidad\n",
    "total = precio * cantidad\n",
    "\n",
    "# Imprime el precio total de la compra\n",
    "print(total)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

# Guardar el archivo
with open('comentarios_ejercicios.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=2)

print("Archivo 'comentarios_ejercicios.ipynb' creado exitosamente")
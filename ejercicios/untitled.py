import json

# Crear la estructura del notebook
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Ejercicios: Operaciones matemáticas\n",
                "En este notebook, practicarás diferentes operaciones matemáticas utilizando Python, la biblioteca `math` y la biblioteca `statistics`. Completa los ejercicios siguientes."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-1\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar la operación de suma en Python.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "a = 5\n",
                "b = 7\n",
                "suma = a + b\n",
                "print(suma)  # Resultado: 12\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea dos variables `x` e `y` con los valores `6` y `3` respectivamente\n",
                "2. Realiza la suma de ambas variables\n",
                "3. Guarda el resultado en una variable llamada `resultado`\n",
                "4. Imprime el resultado usando `print()`\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-2\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar la operación de resta en Python.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "a = 25\n",
                "b = 10\n",
                "resta = a - b\n",
                "print(resta)  # Resultado: 15\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea dos variables `x` e `y` con los valores `8` y `3` respectivamente\n",
                "2. Realiza la resta de ambas variables (x - y)\n",
                "3. Guarda el resultado en una variable llamada `resultado`\n",
                "4. Imprime el resultado usando `print()`\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-3\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar la operación de multiplicación en Python.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "a = 4\n",
                "b = 6\n",
                "multiplicacion = a * b\n",
                "print(multiplicacion)  # Resultado: 24\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea two variables `x` e `y` con los valores `7` y `4` respectivamente\n",
                "2. Realiza la multiplicación de ambas variables\n",
                "3. Guarda el resultado en una variable llamada `resultado`\n",
                "4. Imprime el resultado usando `print()`\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-4\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar las operaciones de división en Python.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "a = 20\n",
                "b = 4\n",
                "division = a / b\n",
                "print(division)  # Resultado: 5.0\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea dos variables `x` e `y` con los valores `15` y `3` respectivamente\n",
                "2. Realiza la división normal (/) de ambas variables\n",
                "3. Realiza también la división entera (//) de las mismas variables\n",
                "4. Guarda ambos resultados en variables `division_normal` y `division_entera`\n",
                "5. Imprime ambos resultados usando `print()`\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-5\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar las operaciones de potencia y módulo en Python.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "base = 2\n",
                "exponente = 3\n",
                "potencia = base ** exponente\n",
                "print(potencia)  # Resultado: 8\n",
                "\n",
                "# También se puede usar pow()\n",
                "potencia_pow = pow(base, exponente)\n",
                "print(potencia_pow)  # Resultado: 8\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea dos variables `base` y `exponente` con los valores `5` y `2` respectivamente\n",
                "2. Calcula la potencia usando el operador `**`\n",
                "3. Calcula la misma potencia usando la función `pow()`\n",
                "4. Calcula también el módulo de 17 dividido entre 5 (17 % 5)\n",
                "5. Imprime todos los resultados con `print()`\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-6\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar el uso de la biblioteca `math` para cálculos geométricos.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "import math\n",
                "\n",
                "# Calcular la hipotenusa de un triángulo rectángulo\n",
                "cateto_a = 3\n",
                "cateto_b = 4\n",
                "hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)\n",
                "print(f\"Hipotenusa: {hipotenusa}\")  # Resultado: 5.0\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Importa la biblioteca `math`\n",
                "2. Define dos variables `cateto_a` y `cateto_b` con los valores `6` y `8` respectivamente\n",
                "3. Calcula la hipotenusa usando el teorema de Pitágoras: √(a² + b²)\n",
                "4. Calcula también el área del triángulo: (base × altura) / 2\n",
                "5. Usa `math.sqrt()` para la raíz cuadrada\n",
                "6. Imprime tanto la hipotenusa como el área con mensajes descriptivos\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-7\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar funciones trigonométricas y constantes matemáticas.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "import math\n",
                "\n",
                "angulo_grados = 45\n",
                "angulo_radianes = math.radians(angulo_grados)\n",
                "seno = math.sin(angulo_radianes)\n",
                "print(f\"Seno de {angulo_grados}°: {seno:.4f}\")\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Asegúrate de tener importada la biblioteca `math`\n",
                "2. Define una variable `radio` con el valor `5`\n",
                "3. Calcula el área de un círculo usando la fórmula: π × r²\n",
                "4. Usa la constante `math.pi` para obtener el valor de π\n",
                "5. Calcula también la circunferencia: 2 × π × r\n",
                "6. Imprime tanto el área como la circunferencia con 2 decimales usando f-strings\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-8\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Crear una calculadora básica que combine múltiples operaciones.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "import math\n",
                "\n",
                "# Calculadora de interés compuesto\n",
                "capital_inicial = 1000\n",
                "tasa_interes = 0.05  # 5%\n",
                "tiempo = 3  # años\n",
                "\n",
                "capital_final = capital_inicial * (1 + tasa_interes) ** tiempo\n",
                "print(f\"Capital final: €{capital_final:.2f}\")\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Crea una calculadora que resuelva este problema:\n",
                "   - Un rectángulo tiene base = 12 y altura = 8\n",
                "   - Calcula el área del rectángulo\n",
                "   - Calcula el perímetro del rectángulo\n",
                "   - Calcula la diagonal del rectángulo (usando teorema de Pitágoras)\n",
                "2. Usa `math.sqrt()` para la diagonal\n",
                "3. Imprime todos los resultados con mensajes descriptivos\n",
                "4. Usa f-strings para formatear las salidas con 2 decimales\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                ":::exercise\n",
                ":label: matematicas-ejercicio-9-statistics\n",
                ":class: ejercicio-practico\n",
                "\n",
                "**Objetivo**: Practicar el uso de la biblioteca `statistics` de Python para análisis estadístico básico.\n",
                "\n",
                "**Ejemplo de referencia**:\n",
                "```\n",
                "import statistics\n",
                "\n",
                "# Calificaciones de estudiantes\n",
                "calificaciones = [85, 92, 78, 90, 88, 76, 95, 89, 82, 79]\n",
                "\n",
                "# Calcular estadísticas básicas\n",
                "promedio = statistics.mean(calificaciones)\n",
                "mediana = statistics.median(calificaciones)\n",
                "desviacion = statistics.stdev(calificaciones)\n",
                "\n",
                "print(f\"Promedio: {promedio:.2f}\")\n",
                "print(f\"Mediana: {mediana}\")\n",
                "print(f\"Desviación estándar: {desviacion:.2f}\")\n",
                "```\n",
                "\n",
                "**Instrucciones del ejercicio**:\n",
                "1. Importa la biblioteca `statistics`\n",
                "2. Crea una lista llamada `temperaturas` con las siguientes temperaturas diarias (en °C):\n",
                "   `[22, 25, 19, 28, 24, 26, 23, 21, 27, 25, 24, 22, 26, 25, 23]`\n",
                "3. Calcula y guarda en variables:\n",
                "   - La **temperatura promedio** usando `statistics.mean()`\n",
                "   - La **temperatura mediana** usando `statistics.median()`\n",
                "   - La **moda** (temperatura más frecuente) usando `statistics.mode()`\n",
                "   - La **desviación estándar** usando `statistics.stdev()`\n",
                "   - La **varianza** usando `statistics.variance()`\n",
                "4. Crea otra lista llamada `lluvia` con milímetros de lluvia:\n",
                "   `[0, 5, 12, 0, 8, 3, 0, 15, 7, 2]`\n",
                "5. Calcula el promedio de lluvia y determina cuántos días llovió (valores > 0)\n",
                "6. Imprime todos los resultados con mensajes descriptivos y 2 decimales\n",
                "\n",
                "**Escribe tu solución en la celda de código siguiente**:\n",
                "```\n",
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓\n",
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
                "# ↓↓↓ ESCRIBE TU CÓDIGO AQUÍ ↓↓↓"
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

# Guardar el notebook en un archivo
with open('operaciones_matematicas.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print("Notebook creado exitosamente: 'operaciones_matematicas.ipynb'")
---
marp: true
paginate: true
html: true

style: |

  /* Fondo general estilo Material Design */
  section {
    background: #0b529508; /* gris claro */
    color: #212121; /* texto oscuro */
    font-size: 28px;
    font-family: 'quicksand', 'Helvetica', sans-serif;
    strong { color: #2980b9; }
    .highlight { color: #c0392b; }
    padding-top: 5%;
    }

  /* Títulos grandes y llamativos */

  h1, h2, h3 {
    font-family: 'Noto sans', 'Helvetica', sans-serif;
    font-weight: 900;
    margin-bottom: 10px;
  }

  h1 {
    color: #1976d2; /* azul vibrante */
    font-size: 50px;
    text-transform: uppercase;
  }

  h2 {
    color: #e67e22;
    font-size: 40px;
    text-transform: uppercase;

  }

  h3 {
    color: #8e44ad;
    font-size: 30px;
  }
  
  /* Caja de información estilo Material */
  .box {
    background: #bbdefba0; /* azul claro */
    color: #0d47a1; /* azul oscuro */
    font-weight: 600;
    strong { color: #e67e22; font-weight: 1000; }
    padding: 16px;
    border-radius: 8px;
    margin: 10px 0;
    border-left: 6px solid #1976d2;
  }


    .question-box {
    font-weight: 600;
    background-color: #f4f3f3ff;
    border-left: 8px solid #e67e22;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border-radius: 4px;
    margin-bottom: 20px;
  }


    /* Clase personalizada para notas/definiciones */
    .note {
    background-color: #eaf2f8;
    border-left: 6px solid #2980b9;
    padding: 20px;
    border-radius: 4px;
    margin: 20px 20px 20px 0;
    font-size: 25px;
    }

    /* Estilo para fórmula matemática grande */
  .formula-box {
    text-align: center;
    font-size: 1.2em;
    padding: 10px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 8px;
    margin: 10px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  }

  table {
      width: 100% !important;  /* El !important fuerza el ancho si el tema lo bloquea */
      table-layout: fixed;     /* CLAVE: Distribuye las columnas equitativamente */
      border-collapse: collapse;
      font-size: 0.9em;        /* Un poco más pequeño para que quepa bien */
      margin-top: 20px;
  }

  th {
      background-color: #2c3e50;
      color: white;
      border: 1px solid #2c3e50;
      padding: 15px;
      text-align: center;      /* Centrar títulos */
  }

  td {
      border: 1px solid #ddd;
      padding: 12px;
      text-align: center;      /* Centrar contenido para que se vea lleno */
      vertical-align: middle;  /* Alinear verticalmente */
      word-wrap: break-word;   /* Evita que textos largos rompan la tabla */
  }

  tr:nth-child(even) {
      background-color: #f2f2f2;
  }

  .examples {
    padding-left: 0;
    margin-top: 25px;
    border-top: 1px solid #ccc;
    padding-top: 15px;
  }
  .examples h3 {
    color: #2c3e50;
    margin-bottom: 10px;
  }
  /* Ajuste de lista para mejor espacio */
  ul {
    padding-left: 20px;
    margin-top: 10px;
  }

  pre {
    background: rgba(255, 255, 255, 0.95); /* Un poco más opaco para leer mejor */
    backdrop-filter: blur(10px);          /* Efecto borroso detrás */
    padding: 15px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 15px;
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
    overflow-x: auto;
    font-size: 1em;
    line-height: 1.4;
    font-family: 'Google Sans Mono', 'Fira Mono', monospace;
    color: #1e5ae6ff;
  }

  /* Aseguramos que el código interior herede el color negro */
  code {
    color: inherit;
    background: transparent;
  }

  .highlight-prop {
    color: #226457cd;
    font-weight: bold;
  }
  .definition-box {
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #eaf2f8;
    color: #2c3e50;
    font-size: 22px;
  }

  .grid2 {
    display: grid;
    grid-template-columns: 1fr 1fr; /* 50% y 50% */
    gap: 30px;
  }

  .grid-container-1 {
    display: grid;
    gap: 20px;
    align-items: center;
    align-content: start;
    grid-template-columns: 1fr 1fr;
  }

  /* Columnas flexibles */
  .cols { display:flex; gap:18px; margin-top:20px; font-size: 0.9em; }
  .col1 { flex:1; }
  .col2 { flex:2; }
  .col15 { flex:1.5; }

  /* Portada centrada */
  .portada {
    text-align:right;
  }

  /* Pie de página más pequeño */
  footer {
    font-size: 0.6em;
    color: #616161;
  }

  /* Columnas flexibles */
  .cols { display:flex; gap:18px; margin-top:20px; font-size: 0.9em; }
  .col1 { flex:1; }
  .col2 { flex:2; }
  .col15 { flex:1.5; }


  /* Pie de página más pequeño */
  footer {
    font-size: 0.6em;
    color: #616161;
  }

---

# Python 🐍

## TIC II 2º Bachillerato

por Alberto Durán Pérez

---

# Introducción

<div class = "grid-container-1">

<div>

* **Características Clave**  
  * 🧘 **Filosofía:** Sencillez (Zen de Python).
  * ▶️ **Ejecución:** Interpretado (línea a línea).
  * 🌍 **Entorno:** Multiplataforma.

* **¿Para qué se usa?**
  * 🤖 Inteligencia Artificial (IA).
  * 📊 Ciencia de Datos.
  * 🌐 Desarrollo Web.

</div>

<div>

* **Fundamentos Técnicos**
  * 📦 **Variables:** Cajas para guardar datos.
  * 📏 **Reglas:** Sintaxis estricta y limpia.

</div>

</div>

---

# Variables en Python

## Reglas, Tipos y Buenas Prácticas

### Fundamentos de Programación

---

# 1. ¿Qué es una variable?

Es un lugar en la memoria para **almacenar un valor**.

* **Etiqueta:** El nombre (`myNum`)
* **Contenido:** El valor (`4`)

![bg fit right:20%](https://cdn-icons-png.flaticon.com/512/679/679720.png)

```python
mynum = 4
cliente = "Mauricio"  # Texto entre comillas
````

> **Nota:** La variable guarda información para consultarla o cambiarla después.

-----

# 2. Valores Cambiantes

Como un marcador de baloncesto 🏀, el contenido puede cambiar, pero el nombre de la variable se mantiene.

```python
puntuacion = 86
print(puntuacion) # Muestra 86

puntuacion = 88   # Cambiamos el valor
print(puntuacion) # Ahora muestra 88
```

**La función `print()`**
Sirve para "enseñar" el valor actual al usuario por pantalla.

-----

# 3\. Reglas de Nombramiento 👮‍♂️

1. **Inicio:** Debe empezar por **Letra** o **guion bajo** (`_`).
      * ✅ `variable`, `_secreta`
      * ❌ `1variable` (Nunca números al principio)
2. **Caracteres:** Solo letras, números y `_`.
      * ❌ Nada de espacios, `@`, `-`, o tildes.
3. **Reservadas:** Prohibido usar palabras propias de Python.
      * ❌ `if`, `for`, `while`, `class`.
4. **Case Sensitive:** Las mayúsculas importan.
      * `nombre` ≠ `Nombre`

-----

# 4\. Convenciones de Estilo 🎨

| Estilo | Formato | Uso Principal |
| :--- | :--- | :--- |
| **snake\_case** 🐍 | `mi_variable_total` | Variables y Funciones |
| **camelCase** 🐪 | `miVariableTotal` | Otros lenguajes / Librerías |
| **PascalCase** 🧑‍🔬 | `MiVariableTotal` | Clases (Avanzado) |
| **UPPERCASE** 📢 | `GRAVEDAD` | **Constantes** (No cambian) |

---

# Tipos de Datos (Data Types)

## ¿Qué guarda la caja?

---

# 1. Números: Enteros y Decimales

En Python, diferenciamos los números "completos" de los que tienen "coma".

| Tipo | Nombre Técnico | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Entero** 🔵 | `int` (Integer) | Sin decimales (+ o -) | `5`, `-3`, `42` |
| **Decimal** 🟣 | `float` (Float) | Con punto decimal | `3.14`, `-0.3` |

### ⚡ El Truco del Incremento

Aumentar un contador es muy común. Python tiene un atajo:

```python
contador = 2
contador += 1  # Es igual a: contador = contador + 1
print(contador) # Resultado: 3
````

---

# 2\. Texto

### 📜 Cadenas (`str`)

Secuencias de caracteres entre comillas (`"` o `'`).

* **Concatenar:** Unir textos con `+`.

<!-- end list -->

```python
nombre = "Elena"
print("Hola " + nombre)
```

---

# 3\. Booleanos (`bool`)

Solo tienen dos valores posibles (Lógica binaria).

* `True` (Verdadero)
* `False` (Falso)

> **¡Ojo\!** La primera letra siempre va en **Mayúscula**.

-----

# 3\. Conversión de Tipos (Casting) 🔄

A veces necesitamos transformar un dato. Python usa funciones con el nombre del tipo destino.

### Las Funciones Mágicas

* `int()`: Convierte a entero (trunca decimales).
* `str()`: Convierte a texto (para imprimir mensajes).
* `float()`: Convierte a decimal.

<!-- end list -->

```python
# Ejemplo: De texto a número para sumar
edad_texto = "17"
edad_numero = int(edad_texto)
print(edad_numero + 1)  # Resultado: 18 (¡Funciona!)
```

-----

# 4\. El Detective `type()` 🕵️‍♂️

¿No sabes qué hay en una variable? Pregúntale a Python.

```python
x = 3.14
print(type(x))  # <class 'float'>
```

### 🤔 Pregunta para pensar

¿Qué pasa si intentas esto?
`print("Tengo " + 15 + " años")`

> **Respuesta:** 💥 **ERROR**.
> Python no suma peras (texto) con manzanas (números).
> **Solución:** `print("Tengo " + str(15) + " años")`

-----

# Resumen Rápido 📝

| Tipo | Función Python | Ejemplo Real |
| :--- | :--- | :--- |
| **Entero** | `int()` | Edad, Cantidad de hijos |
| **Decimal** | `float()` | Precio, Altura, Peso |
| **Texto** | `str()` | Nombre, Dirección |
| **Lógico** | `bool()` | ¿Aprobado?, ¿Usuario activo? |

**Recuerda:** Usa nombres de variables descriptivos (`precio`, no `x`).

---

# Operaciones Matemáticas 📐

## Aritmética, Math y Estadística

**Python para Ciencia de Datos**

---

# 1. Operadores Básicos

Python funciona como una calculadora potente.

| Símbolo | Operación | Ejemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `+` | Suma | `10 + 5` | `15` |
| `-` | Resta | `10 - 5` | `5` |
| `*` | Multiplicación | `10 * 5` | `50` |
| `/` | División | `10 / 3` | `3.333...` |
| `//` | **División Entera** | `10 // 3` | `3` (Trunca) |
| `%` | **Módulo** (Resto) | `10 % 3` | `1` |
| `**` | **Potencia** | `2 ** 3` | `8` |

---

# 2. Presentar Resultados

No basta con calcular, hay que mostrarlo bien. La forma moderna es usar **f-strings**.

```python
a = 10
b = 5
resultado = a + b
```

## Forma antigua (poco clara)

```python
print("La suma de", a, "y", b, "es:", resultado)
```

## Forma PRO (f-strings)

```python
print(f"La suma de {a} y {b} es: {resultado}")
```

---

# 🗣️ La Función `print()`

## La voz de tu programa

---

# Print()

* Es una función **incorporada** (siempre disponible).
* Se utiliza para **mostrar información** al usuario en la consola.

### 📋 Uso Básico

```python
# Imprimir texto fijo
print("¡Hola, Mundo!")

# Imprimir variables y texto combinado (usa comas)
x = 10
print("El valor de x es", x) 
````

> **Recuerda:** La coma (`,`) añade un espacio automáticamente entre los argumentos.

-----

# F-strings: La Forma Moderna ✨

Los `f-strings` (cadenas con formato) son la forma más legible y potente de combinar variables y texto.

* Se nombran por la letra `f` antes de la cadena (`f""`).
* Permiten introducir variables o expresiones usando llaves `{}`.

### 📝 Ejemplo Básico

```python
nombre = "Alberto"
edad = 35

print(f"Hola, me llamo {nombre} y tengo {edad} años.")
# Resultado: Hola, me llamo Alberto y tengo 35 años.

```

-----

# F-strings: Poder Avanzado (I)🚀

Los `f-strings` no solo insertan variables; también pueden ejecutar **código o aplicar formato** dentro de las llaves `{}`.

### 🧮 1. Operaciones Directas

```python
x = 5
y = 3

# Ejecuta x + y DENTRO de la cadena.
print(f"La suma de {x} y {y} es {x + y}")
```

---

# F-strings: Poder Avanzado (II)🚀

### 🔢 2. Formato Decimal

Útil para controlar la precisión de los números flotantes.

```python
div = 124 / 45  # Resultado: 2.7555555...

# Sin formato
print(f"El valor es {div}")

# Con formato: {:.4f} muestra 4 decimales
print(f"El valor es {div:.4f}") 
```

-----

# Controlando la Presentación

### ⬇️ Saltos de Línea

El carácter especial `\n` (newline) fuerza un salto de línea.

```python
# Imprime en tres líneas separadas
print("Línea 1 \nLínea 2 \nLínea 3")
```

### ➡️ Parámetro `sep` (Separador)

Controla el texto que aparece **entre** los argumentos separados por comas.

```python
# Sin sep: 'Alberto Sara Ana'
# Con sep: 'Alberto-Sara-Ana'
print("Alberto", "Sara", "Ana", sep="-")
```

-----

# El Parámetro `end`

Por defecto, `print()` termina la línea con un salto de línea (`\n`). El parámetro `end` te permite cambiar esto:

### 🧵 Unir Líneas

```python
# Muestra "Hola " (nota el espacio al final)
print("Hola", end=" ") 

# Muestra "Mundo" en la MISMA línea
print("Mundo") 

# Salida: Hola Mundo
```

---

### 🍓 Imprimir Colecciones

`print()` funciona directamente con listas, tuplas y diccionarios, mostrándolos en un formato legible.

```python
frutas = ["manzana", "banana", "naranja"]
print("Stock de frutas:", frutas)
```

---

# 👂 La Función `input()`

## Recibiendo datos del usuario

---

# Función `input()`

* **Propósito:** Permite que el programa **reciba datos** (texto) directamente del usuario a través del teclado.
* **Mecanismo:** Muestra un mensaje y **pausa** el programa hasta que el usuario presiona Enter.

### 📝 Sintaxis Clave

La respuesta siempre se asigna a una **variable**.

```python
# Muestra la pregunta y almacena la respuesta en 'name'
name = input("¿Cuál es tu nombre?")

print(name)
````

------

## ¡Cuidado con el Tipo de Dato! ⚠️

La función `input()` **SIEMPRE** devuelve una **cadena de texto (string)**, incluso si el usuario teclea números.

### 🛑 El Error Común

Si pides la edad y no conviertes, ¡no puedes sumar!

### 🔑 La Solución: Conversión

Debes usar las funciones de conversión (`int()`, `float()`) para cambiar el tipo de dato.

-----

# 🛠️ Funciones: `def()`

## Reutiliza tu código

---

# ¿Qué es una Función?

Es una "máquina" con nombre que:

1. **Recibe** datos de entrada (parámetros).
2. **Procesa** (instrucciones).
3. **Devuelve** un resultado (opcional).

> **Objetivo:** Escribir la lógica **una sola vez** y llamarla las veces que quieras.

---

### ⚙️ Sintaxis General

```python
def nombre_funcion(param1, param2=defecto):
    """Docstring: Documentación de la función."""
    # Cuerpo indentado
    resultado = ...
    return resultado
````

-----

## 📝 Parámetros vs. Argumentos

| Concepto | Ubicación | Descripción |
| :---: | :---: | :--- |
| **Parámetro** | En la **Definición** (`def`) | Nombre de la variable de entrada. |
| **Argumento** | En la **Llamada** (`nombre_funcion(...)`) | El valor real que pasas a la función. |

-----

## 🔑 Ejemplo: Devolver un Valor

```python
def suma(a, b=0):
    # a y b son Parámetros
    resultado = a + b
    return resultado # Devuelve el 8 o el 5

# LLAMADA 1: Argumentos 5, 3
total = suma(5, 3) 
print(total) # Imprime 8

# LLAMADA 2: Argumento 5 (b usa 0 por defecto)
total_2 = suma(5)
print(total_2) # Imprime 5
```

---

# 🚦 Estructuras de Control

## Rompiendo la Secuencia Lineal

---

### 📏 1. Ejecución Secuencial (Por Defecto)

Por naturaleza, Python ejecuta las instrucciones **de arriba abajo**, una tras otra.

```python
print("Paso 1: Encender")
print("Paso 2: Calentar")
print("Paso 3: Servir")
````

> **Resultado:** Siempre se ejecuta el `Paso 1`, luego el `Paso 2`, y finalmente el `Paso 3`.

---

### 💡 Estructuras de Control

Permiten **romper esta linealidad** para que el código pueda:

1. **Tomar decisiones** (Condicionales).
2. **Repetir acciones** (Bucles).

-----

## 1. Estructuras Condicionales ⚖️

Permiten al programa **tomar decisiones** y ejecutar un bloque de código *solo si se cumple una condición*.

### 🔑 Componentes Principales

* **`if`**: Ejecuta si la condición es **Verdadera**.
* **`else`**: Ejecuta si la condición es **Falsa** (todo lo demás).
* **`elif`** (Else If): Permite comprobar una condición *adicional* si la anterior fue falsa.

---

### 📝 Ejemplo (Mayoría de Edad)

```python
edad = 17

if edad >= 18:
    print("Eres mayor de edad") # Bloque 1
else:
    print("Eres menor de edad") # Bloque 2
```

> **Analogía:** Piensa en el GPS de un coche: `if` hay atasco, `else` sigue por la ruta principal.

-----

## 2. Bucles: Repetir Acciones 🔄

Permiten ejecutar el mismo bloque de código múltiples veces sin tener que reescribirlo.

<div class="grid2">

<div>

### 🔁 Bucle `for`

* **Uso:** Para repetir un número **determinado** de veces o para iterar sobre una secuencia (listas, rangos).

<!-- end list -->

```python
# Se ejecuta 5 veces (para i = 0, 1, 2, 3, 4)
for i in range(5):
    print(f"Repetición {i + 1}") 
```

</div>

<div>

### 🕰️ Bucle `while`

* **Uso:** Para repetir **mientras** se cumpla una condición; el número de repeticiones es **indefinido**.

<!-- end list -->

```python
contador = 0
while contador < 5:
    print("Contando...") 
    contador += 1 # ¡Clave! Para no caer en un bucle infinito
```

</div>

</div>

-----

## ❓ Actividad de Aprendizaje

1. **¿Qué estructura usarías para determinar si una persona es elegible para la tarifa de descuento (es menor de 12 años o mide menos de 1.20m)?** (Condicional o Bucle)

2. **¿Qué estructura usarías para escanear y registrar las 200 entradas vendidas para el día?** (Condicional o Bucle)


---

## 🚦 Estructuras Condicionales: `if`, `elif` y `else`

Las estructuras **condicionales** en Python son esenciales para la **toma de decisiones**.

Permiten que tu programa elija qué camino seguir en función de si ciertas **condiciones** son `True` (Verdaderas) o `False` (Falsas).

-----

### 1\. El Fundamento: `if`

La estructura `if` es la base. El bloque de código asociado solo se ejecuta si la **condición** es `True`.

  * **Recuerda:** La **indentación** (los espacios al inicio de la línea) es vital. Indica qué código pertenece al bloque `if`.

#### 📋 Ejemplo de `if`

```python
edad = 18

if edad >= 18:
    print("Eres legalmente un adulto.")
print("El programa continúa aquí.") # Esta línea siempre se ejecuta, está fuera del 'if'.
```


-----

### 2\. Manejando Alternativas: `if...else`

Cuando necesitas ejecutar un código si la condición es `True` y **otro código distinto** si es `False`, usas `else`.

  * El bloque `else` **siempre** es la alternativa final y se ejecuta si **ninguna** de las condiciones `if` o `elif` anteriores se cumplió.

#### 📋 Ejemplo de `if...else`

```python
esta_soleado = False

if esta_soleado:
    print("Saldremos a caminar.")
else:
    print("Nos quedaremos dentro a leer.") # Esto se ejecuta
```



-----

### 3\. Múltiples Caminos: `if...elif...else`

La estructura `elif` (abreviatura de *else if*) te permite encadenar múltiples pruebas de condición de forma secuencial.

  * Python evalúa las condiciones **de arriba a abajo**.
    * Tan pronto como encuentra una condición `True`, ejecuta ese bloque de código y **salta** el resto de la estructura, incluyendo los `elif` y el `else`.

```python
nota = 8
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")  # Este bloque se ejecuta porque 85 >= 70
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspendido")
```

-----

## 4\. ⚙️ Operadores de Comparación y Lógicos

Para construir las condiciones, utilizamos operadores que devuelven un valor **Booleano** (`True` o `False`).

#### Operadores de Comparación

| Operador | Significado | Ejemplo | Resultado |
| :---: | :--- | :---: | :---: |
| **`==`** | Igual a | `5 == 5` | `True` |
| **`!=`** | No igual a | `5 != 3` | `True` |
| **`>`** | Mayor que | `10 > 7` | `True` |
| **`<`** | Menor que | `4 < 4` | `False` |
| **`>=`** | Mayor o igual que | `8 >= 8` | `True` |
| **`<=`** | Menor o igual que | `1 <= 0` | `False` |

---

### Operadores Lógicos (Combinando Condiciones)

Estos operadores te permiten evaluar varias condiciones como una sola:

| Operador | Significado | Condiciones Necesarias |
| :---: | :--- | :--- |
| **`and`** | Y lógico | **Todas** las condiciones deben ser `True` para que el resultado sea `True`. |
| **`or`** | O lógico | Solo se necesita que **una** de las condiciones sea `True` para que el resultado sea `True`. |
| **`not`** | Negación | Invierte el valor Booleano (convierte `True` en `False`, y viceversa). |

---

#### 📋 Ejemplo con Operadores Lógicos

```python
temperatura = 28
hay_sol = True

# Usamos AND: ambas deben ser True
if temperatura > 25 and  hay_sol = True:
    print("Día perfecto de playa con viento.")
else:
    print("Mejor planificar otra cosa.")


# Usamos OR: basta con que una sea True
es_sabado = False
es_fin_de_semana = True

if es_sabado or es_fin_de_semana:
    print("¡A disfrutar!") # Este bloque se ejecuta
```

-----


## 🔁 Bucle `for` en Python

---

# 🎯 Bucle `for`: Concepto y Propósito

* Se utiliza para **iterar** (*repetir, recorrer*) sobre una **secuencia**.
* Ejecuta un bloque de código para **cada elemento** en esa secuencia.
* Permite **repetir** un bloque de código un **número determinado** de veces.

### 📝 Sintaxis Básica

```python
for elemento in secuencia:
    # Bloque de código a ejecutar para cada elemento
````

-----

### 🔢 Ejemplo 1: Utilizando la función `range`

```python
for x in range(1, 10):
    print("Hola")
```

  * **Secuencia:** `range(1, 10)` genera números desde **1** hasta **9** (el límite superior es exclusivo).
  * **Repetición:** El bucle se ejecuta **9 veces**, imprimiendo "Hola" en cada iteración.
  * **Variable:** En cada paso, la variable `x` adopta un valor entre 1 y 9.

-----

### 🍎 Ejemplo 2: Iterando (recorriendo) una `lista`

```python
frutas = ["manzana", "banana", "cereza"]

for elemento in frutas:
    print("Me gusta la " + elemento)
```

  * **Recorrido:** El bucle itera sobre cada **elemento** de la lista.
  * **Iteración:** En cada paso, `elemento` toma el valor de la fruta actual (`"manzana"`, `"banana"`, etc.).
  * **Convención:** Es común usar variables cortas como `i` o `j` en lugar de `elemento`.

-----

### 🔠 Ejemplo 3: Iterando sobre una Cadena de Texto

```python
for letra in "Esternocleidomastoideo":
    print(letra)
```

  * **Secuencia:** Una cadena de texto (string) es una secuencia de **caracteres**.
  * **Función:** El bucle itera sobre **cada carácter** del string.
  * **Salida:** Imprimirá cada letra en una línea separada.

---


## 🔄 Bucle `while` en Python

---

# ⏳ Bucle `while`: Concepto y Propósito

* Se utiliza para repetir un bloque de código **mientras una condición sea verdadera**.
* La condición se comprueba **al inicio** de cada ciclo.
* Permite repetir un bloque de código un **número indeterminado** de veces.

### 📝 Sintaxis Básica

```python
while condicion:
    # Bloque de código a ejecutar
    # ¡Importante! Aquí se debe modificar la variable de control
````

-----

### 💡 Ejemplo 1: Contador Ascendente

```python
contador = 1

while contador <= 5:
    print(contador, "paso")
    contador += 1  # Incremento: contador = contador + 1

print("Bucle finalizado")
```

**Explicación**

  * El bucle se ejecuta mientras `contador` sea menor o igual a 5.
  * La línea `contador += 1` es **esencial** para que la condición se cumpla en algún momento y el bucle finalice.

-----

### 🚀 Ejemplo 2: Cuenta Atrás

```python
contadorAtras = 5

print("Comienza la cuenta atrás")

while contadorAtras > 0:
    print(contadorAtras)
    contadorAtras -= 1 # Decremento: contadorAtras = contadorAtras - 1

print("¡Despegue!")
```

  * **Flujo:** El bucle va de 5 a 1. Al llegar a 0, la condición `contadorAtras > 0` se vuelve falsa y el código continúa.

-----

### 🛑 Controlando el Bucle: Sentencia `break`

  * La sentencia `break` **detiene** inmediatamente la ejecución del bucle, incluso si la condición `while` sigue siendo verdadera.

### Simulación de "do-while"

Python no tiene un bucle `do-while`, pero se simula con `while True` para garantizar que el código se ejecuta **al menos una vez**.

```python
suma = 0
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break  # El bucle se detiene aquí
    suma += numero

print(f"La suma total es: {suma}")
```


---


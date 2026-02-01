# Uso de Jupyter Notebook para programar en Python

## ¿Qué es Jupyter Notebook?

Jupyter Notebook es un entorno interactivo que permite combinar **texto explicativo** y **código Python ejecutable** en un mismo documento, llamado *cuaderno* o *notebook*. Esto facilita el aprendizaje porque puedes escribir la teoría, probar código en fragmentos y ver inmediatamente los resultados, todo en un mismo lugar.

***

## Diferencias con la forma tradicional de programar

Normalmente, para ejecutar un programa en Python se crea un archivo con extensión `.py` y luego se ejecuta con el comando:

```bash
python archivo.py
```

Esto ejecuta todo el código junto como un programa completo.

Con Jupyter Notebook, en cambio, el código se organiza en **celdas** que puedes ejecutar una a una para ver su efecto inmediatamente. También puedes combinar celdas de texto para explicar lo que haces, añadir fórmulas, imágenes o enlaces.

***

## Cómo iniciar y usar Jupyter Notebook

1. **Abre la terminal o línea de comandos** de tu sistema operativo.
2. Usa el comando `cd` para ir al directorio donde guardas tus cuadernos. Por ejemplo:
```bash
cd ruta/donde/estan/los/cuadernos
```

3. Escribe el comando para iniciar el servidor de Jupyter:
```bash
jupyter notebook
```

4. Se abrirá tu navegador web automáticamente con la página principal de Jupyter.
5. Ahí puedes:
    - **Abrir un notebook existente** haciendo clic en el archivo
    - **Crear un nuevo notebook** usando el botón *New* → *Python 3*
6. Trabaja con las celdas:
    - **Celdas de código**: escribe o pega código Python y ejecuta con `Ctrl+Enter` o con el botón *Run*.
    - **Celdas de texto**: puedes escribir explicaciones usando lenguaje Markdown (como este texto). No son ejecutables, solo sirven para documentar.
7. Guarda tu progreso en cualquier momento con `Ctrl+S`. Se guardan tanto el código como los resultados visibles.

***

## Ejemplo básico para empezar

### Celda de código (ejecutable):

```python
# Prueba a escribir y ejecutar este código en una celda de código
print("Hola, mundo desde Jupyter Notebook")
```

Ejecuta la celda con `Ctrl+Enter` y verás el resultado justo debajo.

### Celda de texto (explicativa):

```markdown
# Este es un título en una celda de texto escrita con Markdown
Puedes usar listas, negritas, cursivas y mucho más para documentar tus cuadernos.
```


***

## Consejos útiles

- Las celdas se ejecutan individualmente y en orden. Si ejecutas una celda que depende de otra, asegúrate de haber corrido las anteriores para evitar errores.
- Puedes **añadir nuevas celdas** con el botón `+` y elegir si es de código o texto.
- Para mover celdas, usa las flechas arriba y abajo o arrástralas.
- Usa la opción *Restart \& Run All* para reiniciar el kernel y ejecutar todas las celdas desde el principio, asegurándote de que todo funciona correctamente.

***

## ¿Problemas para instalar?

Consulta esta guía para instalar Python y Jupyter en tu ordenador:

[Guía de instalación de Jupyter Notebook](http://facundoq.github.io/courses/images/jupyter.html)

***

Con estas instrucciones, estarás listo para comenzar a programar en Python usando Jupyter Notebook. Cualquier duda, pregúntame y te ayudaré a resolverla.

¡Ánimo y a programar!

***
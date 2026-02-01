
---

## 📘 3. **Ejercicios para alumnos**
```markdown
:::{exercise}
Crea un DataFrame con las temperaturas de la semana y calcula la media, máxima y mínima.
:::

:::{solution} Solución
```python
import pandas as pd

temps = [12, 14, 13, 16, 15, 11, 10]
pd.Series(temps).describe()

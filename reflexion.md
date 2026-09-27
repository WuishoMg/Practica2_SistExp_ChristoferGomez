# Reflexión y análisis de la práctica

## Análisis del Ejercicio 2: Conflicto de reglas

Para analizar el comportamiento del sistema cuando más de una regla puede activarse al mismo tiempo, se utilizó un conjunto de síntomas que cumplía simultáneamente con las condiciones de Gripe y Alergia.

Los síntomas utilizados fueron:

- Fiebre.
- Tos.
- Dolor de garganta.
- Estornudos.
- Congestión nasal.
- Picazón en los ojos.

Con estos síntomas, el motor de inferencia generó dos diagnósticos:

1. Alergia.
2. Gripe.

Esto demuestra que el sistema experto puede activar más de una regla cuando los hechos presentes en la memoria de trabajo cumplen con varias condiciones al mismo tiempo.

En la primera prueba se utilizó el sistema original, donde la regla de Gripe estaba definida antes que la regla de Alergia. A pesar de esto, el sistema ejecutó primero la regla de Alergia y después la de Gripe.

Posteriormente se realizó una segunda prueba en la que se invirtió el orden de definición de estas reglas, colocando primero Alergia y después Gripe. El resultado fue el mismo: se generaron dos diagnósticos y el orden de ejecución volvió a ser Alergia y después Gripe.

Por lo tanto, en las pruebas realizadas se observó que el orden en que las reglas estaban definidas dentro de la clase no modificó el resultado ni el orden de ejecución. Esto también muestra que el motor de inferencia de Experta no simplemente ejecuta las reglas de arriba hacia abajo según aparecen escritas en el código, sino que utiliza su propio mecanismo para resolver qué regla activada se ejecuta primero.

---

## Preguntas de reflexión

### 1. ¿Qué limitaciones observaste en este enfoque durante la práctica?

Una de las principales limitaciones es que el sistema depende completamente de las reglas que fueron programadas previamente. Si el paciente presenta síntomas que no coinciden exactamente con alguna de las combinaciones definidas, el sistema no puede determinar una enfermedad y utiliza la regla de respaldo.

También se observó que pueden existir varios diagnósticos al mismo tiempo. Por ejemplo, cuando se proporcionaron síntomas de Gripe y Alergia, el sistema generó ambos diagnósticos porque las dos reglas cumplían sus condiciones.

Otra limitación es que el sistema no aprende con la experiencia. Las reglas no cambian después de ejecutar nuevos casos y el sistema no puede descubrir nuevas relaciones entre síntomas y enfermedades por sí mismo. Para agregar una nueva enfermedad es necesario escribir manualmente una nueva regla.

Además, en esta práctica los síntomas se manejan de forma booleana, es decir, solamente se considera si están presentes o no. Esto hace que el sistema sea sencillo, pero no permite representar distintos niveles de intensidad.

### 2. ¿Cómo podría manejarse la incertidumbre en los síntomas, por ejemplo, un síntoma presente solo parcialmente?

Una posible mejora sería dejar de representar los síntomas solamente como verdadero o falso y utilizar algún valor que indique su intensidad o nivel de certeza.

Por ejemplo, en lugar de indicar únicamente:

`dolor_cabeza = True`

se podría manejar información como:

- Dolor de cabeza leve.
- Dolor de cabeza moderado.
- Dolor de cabeza intenso.

También podrían utilizarse factores de certeza, probabilidades o lógica difusa para representar situaciones donde no se tiene total seguridad de que un síntoma esté presente.

De esta forma, el sistema podría realizar un razonamiento más flexible y no depender únicamente de coincidencias exactas entre síntomas y reglas.

### 3. En el Ejercicio 2, ¿qué implicaciones tiene para un sistema experto real que se activen varias reglas a la vez?

Que varias reglas se activen al mismo tiempo significa que un mismo conjunto de hechos puede conducir a diferentes conclusiones.

En la práctica, los síntomas utilizados permitieron obtener los diagnósticos de Alergia y Gripe al mismo tiempo. En un sistema experto real esto podría representar un problema, porque no siempre sería adecuado presentar varias conclusiones sin indicar cuál tiene mayor importancia o probabilidad.

Por esta razón, un sistema experto más completo podría necesitar mecanismos adicionales para resolver conflictos entre reglas. Por ejemplo, se podrían utilizar prioridades, niveles de certeza, reglas más específicas o solicitar información adicional al usuario antes de generar una conclusión.

El ejercicio permitió observar que un sistema experto basado en reglas puede ser útil para representar conocimiento de manera sencilla, pero cuando existen varias reglas válidas al mismo tiempo es necesario contar con una estrategia para manejar esos conflictos de forma adecuada.
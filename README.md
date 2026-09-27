# Práctica 2 - Sistema Experto

## Descripción

Proyecto desarrollado para la materia de Inteligencia Artificial con el objetivo de implementar un sistema experto sencillo de diagnóstico médico utilizando Python y la librería Experta.

El sistema recibe síntomas como hechos y utiliza reglas para generar uno o varios diagnósticos mediante un motor de inferencia con encadenamiento hacia adelante (*forward chaining*).

Este proyecto tiene únicamente fines académicos y no sustituye una evaluación médica profesional.

Elaborado por Christofer André Mijares Gómez 23760064 8SS
---

## Tipo de Inteligencia Artificial

El proyecto utiliza **Inteligencia Artificial simbólica**, ya que el conocimiento se representa explícitamente mediante hechos y reglas.

Ejemplo:

```text
SI:
fiebre + tos + dolor de garganta

ENTONCES:
Gripe
```

El sistema no utiliza Machine Learning, redes neuronales ni entrenamiento automático. Las reglas son definidas manualmente y no cambian después de ejecutar los casos.

---

## Funcionamiento general

El proceso del sistema es:

```text
Síntomas
   ↓
Hechos
   ↓
Memoria de trabajo
   ↓
Motor de inferencia
   ↓
Evaluación de reglas
   ↓
Diagnóstico
```

Los síntomas son declarados como hechos mediante la clase `Sintoma`.

Cuando una regla cumple todas sus condiciones, el sistema genera un nuevo hecho mediante la clase `Diagnostico`.

---

## Diagnósticos implementados

### Sistema original

- Gripe.
- Migraña.
- Alergia.
- Gastroenteritis.
- Regla de respaldo para casos sin diagnóstico.

### Sistema ampliado

También se agregaron:

- COVID-19.
- Resfriado común.
- Bronquitis.
- Conjuntivitis.

---

## Estructura del proyecto

```text
Practica2_SistExp_ChristoferGomez/
│
├── sistema_experto.py
├── casos_prueba.py
├── casos_ampliados.py
├── conflicto_reglas.py
├── reflexion.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Archivos del proyecto

### `sistema_experto.py`

Es el archivo principal del proyecto.

Contiene:

- La clase `Sintoma`, utilizada para representar los síntomas del paciente.
- La clase `Diagnostico`, utilizada para representar las conclusiones del sistema.
- La clase `SistemaExpertoMedico`, que funciona como motor de inferencia.
- Las reglas de Gripe, Migraña, Alergia y Gastroenteritis.
- Las reglas agregadas de COVID-19, Resfriado común, Bronquitis y Conjuntivitis.
- La regla de respaldo utilizada cuando ningún diagnóstico coincide.
- El ajuste de compatibilidad necesario para utilizar Experta con Python moderno.

---

### `casos_prueba.py`

Ejecuta automáticamente los **cinco casos principales solicitados en la práctica**.

Cada caso crea una nueva instancia del motor, declara los síntomas correspondientes y ejecuta el proceso de inferencia.

Incluye:

**Caso 1: Gripe**

```text
Fiebre + Tos + Dolor de garganta
```

**Caso 2: Alergia**

```text
Estornudos + Congestión nasal + Picazón en los ojos
```

**Caso 3: Gastroenteritis**

```text
Dolor de estómago + Diarrea + Vómitos
```

**Caso 4: Sin diagnóstico**

```text
Cansancio + Mareo
```

Como estos síntomas no corresponden con ninguna regla, se activa la regla de respaldo.

**Caso 5: Activación de varias reglas**

Se utilizan síntomas suficientes para activar simultáneamente:

```text
Gripe + Alergia
```

Este caso permite observar que un mismo conjunto de hechos puede generar más de un diagnóstico.

---

### `casos_ampliados.py`

Contiene las pruebas correspondientes a las enfermedades agregadas durante el ejercicio de ampliación.

Incluye cuatro casos:

**Caso ampliado 1**

```text
Fiebre + Tos seca + Pérdida de olfato
→ COVID-19
```

**Caso ampliado 2**

```text
Congestión nasal + Estornudos + Tos leve
→ Resfriado común
```

**Caso ampliado 3**

```text
Tos persistente + Producción de flema + Dificultad respiratoria
→ Bronquitis
```

**Caso ampliado 4**

```text
Ojos rojos + Secreción ocular + Ardor en los ojos
→ Conjuntivitis
```

Este archivo permite comprobar individualmente que cada una de las nuevas reglas funciona correctamente.

---

### `conflicto_reglas.py`

Se utiliza para realizar el análisis de conflicto entre las reglas de **Gripe y Alergia**.

En ambas pruebas se utilizan exactamente los mismos síntomas, suficientes para activar las dos reglas simultáneamente.

Se realizan dos experimentos.

**Experimento 1**

Se utiliza el sistema original, donde la regla de Gripe está definida antes que la regla de Alergia.

Resultado observado:

```text
1. Alergia
2. Gripe
```

**Experimento 2**

Se utiliza una versión experimental donde el orden de definición de estas dos reglas se invierte.

Resultado observado:

```text
1. Alergia
2. Gripe
```

En ambos experimentos se generaron dos diagnósticos.

Con estas pruebas se observó que, en este caso, cambiar el orden de definición de las reglas no modificó el resultado ni el orden de ejecución.

---

### `reflexion.md`

Contiene la parte escrita de análisis de la práctica.

Incluye:

- El análisis de los resultados obtenidos en el conflicto entre Gripe y Alergia.
- La cantidad de diagnósticos generados.
- El orden de ejecución observado.
- El análisis sobre el orden de definición de las reglas.
- Las respuestas a las tres preguntas de reflexión solicitadas en la práctica.
- Las principales limitaciones del sistema experto.
- Posibles formas de manejar incertidumbre y conflictos entre reglas.

---

### `requirements.txt`

Contiene las dependencias necesarias para ejecutar el proyecto:

```text
experta==1.9.4
frozendict==1.2
schema==0.6.7
```

---

### `.gitignore`

Evita incluir en el repositorio archivos innecesarios, principalmente:

- El entorno virtual `.venv`.
- Archivos temporales de Python.
- Carpetas `__pycache__`.
- Archivos de configuración del editor.

---

## Requisitos

El proyecto fue desarrollado y probado con:

```text
Python 3.14.2
Experta 1.9.4
```

---

## Instalación

Crear el entorno virtual:

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

---

## Compatibilidad con Python moderno

Experta utiliza una versión antigua de `frozendict` que presenta problemas con versiones modernas de Python.

Durante el desarrollo apareció el error:

```text
AttributeError: module 'collections' has no attribute 'Mapping'
```

Para solucionarlo se agregó un pequeño bloque de compatibilidad en `sistema_experto.py` antes de importar Experta.

Este ajuste únicamente permite utilizar la librería con Python moderno y no modifica el funcionamiento de las reglas ni del motor de inferencia.

---

## Ejecución

Ejecutar los cinco casos principales:

```powershell
python casos_prueba.py
```

Ejecutar los casos de las enfermedades agregadas:

```powershell
python casos_ampliados.py
```

Ejecutar el análisis de conflicto entre reglas:

```powershell
python conflicto_reglas.py
```

---

## Resultados principales

Los casos principales generaron:

```text
Caso 1 → Gripe
Caso 2 → Alergia
Caso 3 → Gastroenteritis
Caso 4 → No determinado
Caso 5 → Alergia y Gripe
```

Las reglas adicionales también fueron comprobadas correctamente:

```text
COVID-19
Resfriado común
Bronquitis
Conjuntivitis
```

En el análisis de conflicto se generaron dos diagnósticos en ambos experimentos:

```text
1. Alergia
2. Gripe
```

---

## Conclusión

La práctica permitió comprender cómo funciona un sistema experto basado en reglas y cómo se representa el conocimiento mediante hechos y condiciones.

Los síntomas funcionan como hechos iniciales y el motor de inferencia utiliza las reglas disponibles para generar diagnósticos mediante encadenamiento hacia adelante.

También se observó que varias reglas pueden activarse al mismo tiempo, lo que demuestra la importancia de contar con mecanismos para resolver conflictos en sistemas expertos más avanzados.

Finalmente, el proyecto permite identificar claramente este enfoque como Inteligencia Artificial simbólica, ya que el conocimiento está definido explícitamente mediante reglas y el sistema no aprende automáticamente de ejecuciones anteriores.
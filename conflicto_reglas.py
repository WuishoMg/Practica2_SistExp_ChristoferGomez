#Este archivo contiene los requisitos de Ejercicio 2: Análisis de conflictos de reglas, separado para poder experimentar con estas instrucciones sin alterar el resto del contenido del proyecto.

from sistema_experto import (
    SistemaExpertoMedico,
    Sintoma,
    Diagnostico
)

from experta import KnowledgeEngine, Rule


# ============================================================
# SISTEMA EXPERIMENTAL
# Las reglas de Alergia y Gripe se definen en orden contrario
# al utilizado en el sistema original.
# ============================================================

class SistemaOrdenInvertido(KnowledgeEngine):

    # En este sistema experimental se define primero Alergia.
    @Rule(
        Sintoma(estornudos=True),
        Sintoma(congestion_nasal=True),
        Sintoma(picazon_ojos=True)
    )
    def diagnosticar_alergia(self):
        self.declare(Diagnostico(nombre="Alergia"))
        print("Diagnóstico: Alergia")

    # Después se define Gripe.
    @Rule(
        Sintoma(fiebre=True),
        Sintoma(tos=True),
        Sintoma(dolor_garganta=True)
    )
    def diagnosticar_gripe(self):
        self.declare(Diagnostico(nombre="Gripe"))
        print("Diagnóstico: Gripe")


def declarar_sintomas(engine):
    """
    Declara el mismo conjunto de síntomas para ambos experimentos.
    Estos síntomas permiten activar simultáneamente las reglas
    de Gripe y Alergia.
    """

    engine.declare(Sintoma(fiebre=True))
    engine.declare(Sintoma(tos=True))
    engine.declare(Sintoma(dolor_garganta=True))

    engine.declare(Sintoma(estornudos=True))
    engine.declare(Sintoma(congestion_nasal=True))
    engine.declare(Sintoma(picazon_ojos=True))


def obtener_diagnosticos(engine):
    """
    Obtiene los diagnósticos generados por el motor
    después de ejecutar las reglas.
    """

    diagnosticos = []

    for hecho in engine.facts.values():
        if isinstance(hecho, Diagnostico):
            diagnosticos.append(hecho["nombre"])

    return diagnosticos


def ejecutar_experimento(titulo, clase_sistema):
    """
    Ejecuta un sistema experto con los mismos síntomas
    y muestra los diagnósticos obtenidos.
    """

    print("\n" + "=" * 65)
    print(titulo)
    print("=" * 65)

    engine = clase_sistema()
    engine.reset()

    declarar_sintomas(engine)

    engine.run()

    diagnosticos = obtener_diagnosticos(engine)

    print("\nCantidad de diagnósticos generados:")
    print(len(diagnosticos))

    print("\nOrden de ejecución observado:")

    for posicion, diagnostico in enumerate(diagnosticos, start=1):
        print(f"{posicion}. {diagnostico}")


def main():

    # --------------------------------------------------------
    # EXPERIMENTO 1
    # Utiliza el sistema completo que ya construimos.
    #
    # En sistema_experto.py:
    # Gripe está definida antes que Alergia.
    # --------------------------------------------------------

    ejecutar_experimento(
        "EXPERIMENTO 1 - SISTEMA ORIGINAL "
        "(Gripe definida antes que Alergia)",
        SistemaExpertoMedico
    )

    # --------------------------------------------------------
    # EXPERIMENTO 2
    # Se utilizan las mismas condiciones, pero las reglas
    # están escritas en el orden contrario.
    # --------------------------------------------------------

    ejecutar_experimento(
        "EXPERIMENTO 2 - ORDEN INVERTIDO "
        "(Alergia definida antes que Gripe)",
        SistemaOrdenInvertido
    )


if __name__ == "__main__":
    main()
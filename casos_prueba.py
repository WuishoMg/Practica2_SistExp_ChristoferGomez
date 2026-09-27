from sistema_experto import (
    SistemaExpertoMedico,
    Sintoma,
    Diagnostico
)

def ejecutar_caso(numero, descripcion, sintomas):
    """
    Ejecuta un caso de prueba utilizando una nueva instancia
    del sistema experto.
    """

    print("\n" + "=" * 60)
    print(f"CASO {numero}")
    print(descripcion)
    print("=" * 60)

    # Se crea una nueva instancia del motor para cada caso.
    engine = SistemaExpertoMedico()

    # Se reinicia la memoria de trabajo.
    engine.reset()

    # Se declaran los síntomas del paciente.
    for sintoma in sintomas:
        engine.declare(Sintoma(**sintoma))

    # Se ejecuta el motor de inferencia.
    engine.run()

    # Se revisan los diagnósticos generados.
    diagnosticos = []

    for hecho in engine.facts.values():
        if isinstance(hecho, Diagnostico):
            diagnosticos.append(hecho["nombre"])

    print("\nResultado registrado:")

    if diagnosticos:
        for diagnostico in diagnosticos:
            print(f"- {diagnostico}")
    else:
        print("- No determinado")


def main():

    # Caso 1: Gripe
    ejecutar_caso(
        1,
        "Paciente con fiebre, tos y dolor de garganta.",
        [
            {"fiebre": True},
            {"tos": True},
            {"dolor_garganta": True}
        ]
    )

    # Caso 2: Alergia
    ejecutar_caso(
        2,
        "Paciente con estornudos, congestión nasal y picazón en los ojos.",
        [
            {"estornudos": True},
            {"congestion_nasal": True},
            {"picazon_ojos": True}
        ]
    )

    # Caso 3: Gastroenteritis
    ejecutar_caso(
        3,
        "Paciente con dolor de estómago, diarrea y vómitos.",
        [
            {"dolor_estomago": True},
            {"diarrea": True},
            {"vomitos": True}
        ]
    )

    # Caso 4: Sin diagnóstico
    ejecutar_caso(
        4,
        "Paciente con cansancio y mareo.",
        [
            {"cansancio": True},
            {"mareo": True}
        ]
    )

    # Caso 5: Conflicto entre Gripe y Alergia
    ejecutar_caso(
        5,
        "Paciente con síntomas que permiten activar Gripe y Alergia.",
        [
            {"fiebre": True},
            {"tos": True},
            {"dolor_garganta": True},
            {"estornudos": True},
            {"congestion_nasal": True},
            {"picazon_ojos": True}
        ]
    )


if __name__ == "__main__":
    main()
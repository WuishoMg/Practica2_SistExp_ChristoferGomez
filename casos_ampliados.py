#Este archivo incluye únicamente las pruebas de la ampliación del sistema de enfermedades del Ejercicio 1, con el objetivo de identificar con mayor facilidad cada apartado.

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
    print(f"CASO AMPLIADO {numero}")
    print(descripcion)
    print("=" * 60)

    # Se crea una nueva instancia del motor.
    engine = SistemaExpertoMedico()

    # Se reinicia la memoria de trabajo.
    engine.reset()

    # Se declaran los síntomas del paciente.
    for sintoma in sintomas:
        engine.declare(Sintoma(**sintoma))

    # Se ejecuta el motor de inferencia.
    engine.run()

    # Se buscan los diagnósticos generados.
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

    ejecutar_caso(
        1,
        "Paciente con fiebre, tos seca y pérdida de olfato.",
        [
            {"fiebre": True},
            {"tos_seca": True},
            {"perdida_olfato": True}
        ]
    )

    ejecutar_caso(
        2,
        "Paciente con congestión nasal, estornudos y tos leve.",
        [
            {"congestion_nasal": True},
            {"estornudos": True},
            {"tos_leve": True}
        ]
    )

    ejecutar_caso(
        3,
        "Paciente con tos persistente, producción de flema y dificultad respiratoria.",
        [
            {"tos_persistente": True},
            {"produccion_flema": True},
            {"dificultad_respiratoria": True}
        ]
    )

    ejecutar_caso(
        4,
        "Paciente con ojos rojos, secreción ocular y ardor en los ojos.",
        [
            {"ojos_rojos": True},
            {"secrecion_ocular": True},
            {"ardor_ojos": True}
        ]
    )


if __name__ == "__main__":
    main()
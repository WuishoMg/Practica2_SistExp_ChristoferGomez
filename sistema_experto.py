# Parche de compatibilidad para Experta en versiones modernas de Python
import collections
import collections.abc

if not hasattr(collections, "Mapping"):
    collections.Mapping = collections.abc.Mapping

if not hasattr(collections, "MutableMapping"):
    collections.MutableMapping = collections.abc.MutableMapping

if not hasattr(collections, "Iterable"):
    collections.Iterable = collections.abc.Iterable

# Aquí comienza la práctica

from experta import Fact, KnowledgeEngine, Rule, NOT


class Sintoma(Fact):
    """
    Representa un síntoma presente en el paciente.
    Cada síntoma se almacena como un atributo con valor booleano.
    """
    pass


class Diagnostico(Fact):
    """
    Representa un diagnóstico generado por el sistema experto.
    Almacena el nombre de la enfermedad identificada.
    """
    pass

class SistemaExpertoMedico(KnowledgeEngine):
    """
    Motor de inferencia que contiene las reglas
    del sistema experto médico.
    """
    #Gripe
    @Rule(
        Sintoma(fiebre=True),
        Sintoma(tos=True),
        Sintoma(dolor_garganta=True)
    )
    def diagnosticar_gripe(self):
        self.declare(Diagnostico(nombre="Gripe"))

        print("Diagnóstico: Gripe")
        print(
            "Recomendación: descansar, mantenerse hidratado "
            "y consultar a un médico si los síntomas empeoran."
        )
        
    #Migraña
    @Rule(
        Sintoma(fiebre=True),
        Sintoma(dolor_cabeza=True),
        Sintoma(nauseas=True)
    )
    def diagnosticar_migrana(self):
        self.declare(Diagnostico(nombre="Migraña"))

        print("Diagnóstico: Migraña")
        print(
            "Recomendación: descansar en un lugar tranquilo, "
            "mantenerse hidratado y consultar a un médico "
            "si los síntomas son intensos o persistentes."
        )
        
    #Alergia
    @Rule(
        Sintoma(estornudos=True),
        Sintoma(congestion_nasal=True),
        Sintoma(picazon_ojos=True)
    )
    def diagnosticar_alergia(self):
        self.declare(Diagnostico(nombre="Alergia"))

        print("Diagnóstico: Alergia")
        print(
            "Recomendación: evitar posibles alérgenos y consultar "
            "a un médico si los síntomas continúan o empeoran."
        )
        
    #Gastroenteritis
    @Rule(
        Sintoma(dolor_estomago=True),
        Sintoma(diarrea=True),
        Sintoma(vomitos=True)
    )
    def diagnosticar_gastroenteritis(self):
        self.declare(Diagnostico(nombre="Gastroenteritis"))

        print("Diagnóstico: Gastroenteritis")
        print(
            "Recomendación: mantenerse hidratado, descansar "
            "y consultar a un médico si los síntomas persisten."
        )
        
    #COVID-19
    @Rule(
        Sintoma(fiebre=True),
        Sintoma(tos_seca=True),
        Sintoma(perdida_olfato=True)
    )
    def diagnosticar_covid(self):
        self.declare(Diagnostico(nombre="COVID-19"))

        print("Diagnóstico: COVID-19")
        print(
            "Recomendación: descansar, mantenerse hidratado y consultar "
            "a un profesional de la salud si los síntomas empeoran."
        )
    
    #Resfriado común  
    @Rule(
        Sintoma(congestion_nasal=True),
        Sintoma(estornudos=True),
        Sintoma(tos_leve=True)
    )
    def diagnosticar_resfriado(self):
        self.declare(Diagnostico(nombre="Resfriado común"))

        print("Diagnóstico: Resfriado común")
        print(
            "Recomendación: descansar, mantenerse hidratado y vigilar "
            "la evolución de los síntomas."
        )
    
    #Bronquitis   
    @Rule(
        Sintoma(tos_persistente=True),
        Sintoma(produccion_flema=True),
        Sintoma(dificultad_respiratoria=True)
    )
    def diagnosticar_bronquitis(self):
        self.declare(Diagnostico(nombre="Bronquitis"))

        print("Diagnóstico: Bronquitis")
        print(
            "Recomendación: consultar a un profesional de la salud, "
            "especialmente si existe dificultad para respirar."
        )
    
    #Conjuntivitis (enfermedad extra)
    @Rule(
        Sintoma(ojos_rojos=True),
        Sintoma(secrecion_ocular=True),
        Sintoma(ardor_ojos=True)
    )
    def diagnosticar_conjuntivitis(self):
        self.declare(Diagnostico(nombre="Conjuntivitis"))

        print("Diagnóstico: Conjuntivitis")
        print(
            "Recomendación: evitar frotarse los ojos, mantener una buena "
            "higiene y consultar a un profesional de la salud."
        )
    
    #Sin diagnóstico
    @Rule(
        NOT(Diagnostico()),
        salience=-100  #representa la prioridad de una regla.
    )
    def sin_diagnostico(self):
        print("Diagnóstico: No determinado")
        print(
            "Recomendación: no fue posible determinar un diagnóstico "
            "con los síntomas proporcionados. Consulte a un médico "
            "para una evaluación adecuada."
        )
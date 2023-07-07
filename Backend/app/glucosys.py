from schemas.HTTPSchemas import InputForRules
import rule_engine
from app.questions_generator import questions_sintomas_generales, questions_sintomas_particulares, questions_glucemia
from app.probability_rules import probability_rules
from app.diabetes_type_rules import diabetes_type_rules
import json

INFO_DIABETES_TIPO_1 = '''
    La causa más probable de diabetes Tipo 1 es un trastorno autoinmune. Esta es una condición que ocurre \
        cuando el sistema inmunitario ataca por error y destruye el tejido corporal sano. Con la diabetes tipo 1, \
        una infección o algún otro desencadenante hace que el cuerpo ataque por error las células beta productoras de \
        insulina en el páncreas. 
    La tendencia de desarrollar enfermedades autoinmunes, incluyendo diabetes tipo 1, puede ser heredada a través de los padres.

    <strong>Si usted cree que puede tener esta enfermadad, debería acudir a un médico para un diagnóstico profesional.</strong>
'''

INFO_DIABETES_TIPO_2 = '''
    La diabetes tipo 2 puede deberse a una combinación de factores: Tener sobrepeso u obesidad; No hacer actividad física; Genética e historia familiar.
        
    En general, la diabetes tipo 2 comienza con resistencia a la insulina. Esta es una afección en la que sus células no responden normalmente \
        a la insulina. \
            Como resultado, su cuerpo necesita más insulina para ayudar a que la glucosa ingrese a las células. 
        
    Al principio, su cuerpo produce más insulina para tratar de que las células respondan. \
        Pero con el tiempo, su cuerpo no puede producir suficiente insulina y sus niveles de glucosa en la sangre aumentan.
'''

def calcular_cant_sintomas_grales(datosUsuario):
    tieneHambre = "Hambre" in datosUsuario and datosUsuario["Hambre"] != None
    tieneOrina = "Orina" in datosUsuario and datosUsuario["Orina"] != None
    tieneSed = "Sed" in datosUsuario and datosUsuario["Sed"] != None
    tienePDP = "PerdidaDePeso" in datosUsuario and datosUsuario["PerdidaDePeso"] != None
    # Para que no valide reglas si no estan los campos...
    if not (tieneHambre or tieneOrina or tieneSed or tienePDP):
        return -1
    return (
        (1 if datosUsuario["Hambre"] != False else 0) + 
        (1 if datosUsuario["Orina"] != False else 0) + 
        (1 if datosUsuario["Sed"] != False else 0) + 
        (1 if datosUsuario["PerdidaDePeso"] != False else 0)
    )


def glucosys(datosUsuario: dict):
    if not datosUsuario.get("Glucemia"):
        return {
            "response_type": "QUESTIONS",
            "questions": questions_glucemia
        }
    cant_sintomas_grales = calcular_cant_sintomas_grales(datosUsuario)
    input_proba_rule = {
        "CantSintomasGrales": cant_sintomas_grales,
        "Glucemia": datosUsuario["Glucemia"]
    }
    probability = None
    for prob_rule, proba in probability_rules.items():
        if prob_rule.matches(input_proba_rule):
            probability = proba
            if probability == 'Nula':
                return {
                    "response_type": "RESULT",
                    "type": "Ninguno",
                    "probability": probability,
                    "info": "Usted no posee probabilidad de tener diabetes con los valores enviados." 
                }
            if ("AnticuerposPancreaticos" in datosUsuario 
                and datosUsuario["AnticuerposPancreaticos"] != None 
                and "AlientoFuerteYDulce" in datosUsuario
                and datosUsuario["AlientoFuerteYDulce"] != None
            ):
                print(datosUsuario)
                for type_rule, type_diabetes in diabetes_type_rules.items():
                    if type_rule.matches({
                        "AnticuerposPancreaticos": datosUsuario["AnticuerposPancreaticos"],
                        "AlientoFuerteYDulce": datosUsuario["AlientoFuerteYDulce"]
                    }):
                        return {
                            "response_type": "RESULT",
                            "type": type_diabetes,
                            "probability": probability,
                            "info": INFO_DIABETES_TIPO_1 if type_diabetes == "Tipo 1" else INFO_DIABETES_TIPO_2 
                        }
            else:
                return {
                    "response_type": "QUESTIONS",
                    "questions": questions_sintomas_particulares
                }
    if probability == None:
        return {
            "response_type": "QUESTIONS",
            "questions": questions_sintomas_generales
        }

from schemas.HTTPSchemas import InputForRules
import rule_engine
from app.rules import rules
import json

def glucosys(datosUsuario: dict):
    for rule, result in rules.items():
        if rule.matches(datosUsuario):
            return result
    return "No se encontró una regla que aplique para los datos ingresados"

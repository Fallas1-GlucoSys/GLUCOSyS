from app.questions_generator import questions_sintomas_generales, questions_sintomas_particulares, questions_glucemia
from frames.frames_proba_glucosys import createFrames as createFramesProbability
from frames.frames_tipo_glucosys import createFrames as createFramesTypeDiabetes

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

    <strong>Si usted cree que puede tener esta enfermadad, debería acudir a un médico para un diagnóstico profesional.</strong>
'''

INFO_DIABETES = {
    "Tipo 1": INFO_DIABETES_TIPO_1,
    "Tipo 2": INFO_DIABETES_TIPO_2,
    "Nulo": "Usted no posee probabilidad de tener diabetes con los valores enviados."
}


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


def calcular_cant_sintomas_particulares(datosUsuario):
    tieneAnticuerpos = "AnticuerposPancreaticos" in datosUsuario and datosUsuario["AnticuerposPancreaticos"] != None and datosUsuario["AnticuerposPancreaticos"] != False
    tieneAlientoFyD = "AlientoFuerteYDulce" in datosUsuario and datosUsuario["AlientoFuerteYDulce"] != None and datosUsuario["AlientoFuerteYDulce"] != False
    return (
        1 if tieneAnticuerpos else 0 +
            1 if tieneAlientoFyD else 0
    )


def getProbability(datosUsuario: dict):
    probabilityFrame = createFramesProbability()
    for key, value in datosUsuario.items():
        probabilityFrame.completeAttribute(key, value)
    cantSintomasGrales = calcular_cant_sintomas_grales(datosUsuario)
    if cantSintomasGrales >= 0:
        probabilityFrame.completeAttribute("CantidadSintomas", cantSintomasGrales)
    probabilityResult = probabilityFrame.continueChaining()
    return probabilityResult


def generateQuestionsProbability(neededFields: dict):
    res = {
        "response_type": "QUESTIONS"
    }
    if ("Glucemia" in neededFields):
        res["questions"] = questions_glucemia
    elif ("Hambre" in neededFields or "Orina" in neededFields or "Sed" in neededFields or "PerdidaDePeso" in neededFields):
        res["questions"] = questions_sintomas_generales
    else:
        res["questions"] = questions_sintomas_particulares
    return res


def getTypeDiabetes(datosUsuario: dict):
    typeFrame = createFramesTypeDiabetes()
    for key, value in datosUsuario.items():
        typeFrame.completeAttribute(key, value)
    cantSintomasParticulares = calcular_cant_sintomas_particulares(datosUsuario)
    if cantSintomasParticulares >= 0:
        typeFrame.completeAttribute("CantidadSintomasParticulares", cantSintomasParticulares)
    typeResult = typeFrame.continueBackwardChaining()
    return typeResult


def generateQuestionsTypeDiabetes():
    return {
        "response_type": "QUESTIONS",
        "questions": questions_sintomas_particulares
    }


def glucosys(datosUsuario: dict):
    resProba = getProbability(datosUsuario)
    if resProba["type"] == "ASK":
        return generateQuestionsProbability(resProba["value"])
    resTypeDiabetes = getTypeDiabetes(datosUsuario)
    if resTypeDiabetes["type"] == "ASK":
        return generateQuestionsTypeDiabetes()
    return {
        "response_type": "RESULT",
        "type": resTypeDiabetes["value"],
        "probability": resProba["value"],
        "info": INFO_DIABETES[resTypeDiabetes["value"]]
    }

    
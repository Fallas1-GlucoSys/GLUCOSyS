from app.questions_generator import questions_sintomas_generales, questions_sintomas_particulares, questions_glucemia, questions_laboratorio
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

RESPUESTA_SIN_LABORATORIO = {
    "response_type": "RESULT",
    "type": "Desconocido",
    "probability": "Desconocida",
    "info": "No puede realizar el presente diagnóstico sin estudios de laboratorio."
}

currentFrames = {}


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
    lastRes = None
    if (not (datosUsuario["ClientId"] in currentFrames)):
        currentFrames[datosUsuario["ClientId"]] = {
            "Probability": createFramesProbability(),
            "Type": None
        }
    elif ((datosUsuario["ClientId"] in currentFrames) and (currentFrames[datosUsuario["ClientId"]]["Probability"] is None)):
        currentFrames[datosUsuario["ClientId"]]["Probability"] = createFramesProbability()
    probabilityFrame = currentFrames[datosUsuario["ClientId"]]["Probability"]
    probabilityFrame.resetValues()
    cantSintomasGrales = calcular_cant_sintomas_grales(datosUsuario)
    if cantSintomasGrales >= 0:
        probabilityFrame.completeAttribute("CantidadSintomas", cantSintomasGrales)
    for key, value in datosUsuario.items():
        if key != "ClientId" and value is not None:
            iterRes = probabilityFrame.completeAttribute(key, value)
            # Puede devolver None si ningun frame tiene el attr a agregar
            if iterRes is not None:
                if iterRes["type"] == "RESULT":
                    return iterRes
                lastRes = iterRes
    return lastRes


def generateQuestionsProbability(neededFields: dict):
    res = {
        "response_type": "QUESTIONS"
    }
    if ("Glucemia" in neededFields):
        res["questions"] = questions_glucemia
    elif ("Hambre" in neededFields or "Orina" in neededFields or "Sed" in neededFields or "PerdidaDePeso" in neededFields):
        res["questions"] = questions_sintomas_generales
    elif ("PoseeLaboratorio" in neededFields):
        res["questions"] = questions_laboratorio
    else:
        res["questions"] = questions_sintomas_particulares
    return res


def getTypeDiabetes(datosUsuario: dict):
    lastRes = None
    if not (datosUsuario["ClientId"] in currentFrames):
        currentFrames[datosUsuario["ClientId"]] = {
            "Probability": None,
            "Type": createFramesTypeDiabetes()
        }
    elif datosUsuario["ClientId"] in currentFrames and currentFrames[datosUsuario["ClientId"]]["Type"] is None:
        currentFrames[datosUsuario["ClientId"]]["Type"] = createFramesTypeDiabetes()
    typeFrame = currentFrames[datosUsuario["ClientId"]]["Type"]
    typeFrame.resetValues()
    cantSintomasParticulares = calcular_cant_sintomas_particulares(datosUsuario)
    if cantSintomasParticulares >= 0:
        typeFrame.completeAttribute("CantidadSintomasParticulares", cantSintomasParticulares)
    for key, value in datosUsuario.items():
        iterRes = typeFrame.completeAttribute(key, value)
        if iterRes is not None:
            lastRes = iterRes
    return lastRes


def generateQuestionsTypeDiabetes():
    return {
        "response_type": "QUESTIONS",
        "questions": questions_sintomas_particulares
    }


def glucosys(datosUsuario: dict):
    resProba = getProbability(datosUsuario)
    if resProba["type"] == "ASK":
        return generateQuestionsProbability(resProba["value"])
    elif resProba["type"] == "RESULT" and resProba["value"] == "Sin Resultado":
        return RESPUESTA_SIN_LABORATORIO
    resTypeDiabetes = getTypeDiabetes(datosUsuario)
    if resTypeDiabetes["type"] == "ASK":
        return generateQuestionsTypeDiabetes()
    return {
        "response_type": "RESULT",
        "type": resTypeDiabetes["value"],
        "probability": resProba["value"],
        "info": INFO_DIABETES[resTypeDiabetes["value"]]
    }

    
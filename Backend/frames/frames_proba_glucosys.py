from inference_engine.Frame import Frame
from inference_engine.Attribute import Attribute


def checkFieldsCompleted(attrs):
    if not attrs["PoseeLaboratorio"].isCompleted():
        return ["PoseeLaboratorio"]
    if not attrs["Glucemia"].isCompleted():
        return ["Glucemia"]
    if (
        attrs["Glucemia"].getValue() < 180 and 
        attrs["Glucemia"].getValue() >= 100 and
            (
                (not attrs["Hambre"].isCompleted()) or 
                (not attrs["Orina"].isCompleted()) or 
                (not attrs["PerdidaDePeso"].isCompleted()) or 
                (not attrs["Sed"].isCompleted())
            )
    ):
        return ["Hambre", "Orina", "PerdidaDePeso", "Sed"]
    return []


def onComplete(attrs):
    # Invalid frame should not be taken in accountance
    for attr in attrs.values():
        if not attr.validate():
            return {
                "type": None,
                "value": None
            }
    neededAttrs = checkFieldsCompleted(attrs)
    if len(neededAttrs) > 0:
        return {
            "type": "ASK",
            "value": neededAttrs
        }
    return {
        "type": "RESULT"
    }


def onCompleteError(attrs):
    if attrs["PoseeLaboratorio"].isCompleted() and attrs["PoseeLaboratorio"].getValue() == False:
        return {
            "type": "RESULT"
        }


def createFrames():
    frames = {
        "Diagnostico": Frame("Diagnóstico Vacío", {
            "PoseeLaboratorio": Attribute(None, None, onComplete),
            "Glucemia": Attribute(None, None, onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, None, onComplete)
        }),

        "ErrorLaboratorio": Frame("Sin Resultado", {
            "PoseeLaboratorio": Attribute(None, lambda posee: (not posee), onCompleteError),
        }),

        "DiabetesProbabilidadAltaGlucemiaAlta": Frame("Probabilidad Alta", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, None, onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, None, onComplete)
        }),

        "DiabetesProbabilidadNula": Frame("Probabilidad Nula", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia < 100), onComplete)
        }),

        "DiabetesProbabilidadBajaGlucemiaBaja": Frame("Probabilidad Baja", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 100 and valGlucemia < 120), onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, lambda cant: cant <= 2, onComplete)
        }),

        "DiabetesProbabilidadMediaGlucemiaBaja": Frame("Probabilidad Media", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 100 and valGlucemia < 120), onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, lambda cant: cant >= 3, onComplete)
        }),

        "DiabetesProbabilidadBajaGlucemiaMedia": Frame("Probabilidad Baja", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180), onComplete),
            "Hambre": Attribute(None, lambda hambre: not hambre, onComplete),
            "Orina": Attribute(None, lambda orina: not orina, onComplete),
            "Sed": Attribute(None, lambda sed: not sed, onComplete),
            "PerdidaDePeso": Attribute(None, lambda pdp: not pdp, onComplete),
            "CantidadSintomas": Attribute(None, lambda cant: cant == 0, onComplete)
        }),

        "DiabetesProbabilidadMediaGlucemiaMedia": Frame("Probabilidad Media", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180), onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, lambda cant: (cant <= 2 and cant > 0), onComplete)
        }),


        "DiabetesProbabilidadAltaGlucemiaMedia": Frame("Probabilidad Alta", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180), onComplete),
            "Hambre": Attribute(None, None, onComplete),
            "Orina": Attribute(None, None, onComplete),
            "Sed": Attribute(None, None, onComplete),
            "PerdidaDePeso": Attribute(None, None, onComplete),
            "CantidadSintomas": Attribute(None, lambda cant: cant > 2, onComplete)
        })
    }
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadBajaGlucemiaMedia"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadMediaGlucemiaMedia"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadAltaGlucemiaMedia"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadBajaGlucemiaBaja"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadMediaGlucemiaBaja"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadAltaGlucemiaAlta"])
    frames["Diagnostico"].addChildren(frames["DiabetesProbabilidadNula"])
    frames["Diagnostico"].addChildren(frames["ErrorLaboratorio"])
    return frames["Diagnostico"]
from inference_engine.Frame import Frame
from inference_engine.Attribute import Attribute

def checkFieldsCompleted(attrs):
    if (not attrs["Glucemia"].isCompleted()):
        return ["Glucemia"]
    if (
        attrs["Glucemia"].getValue() >= 100 and
        (
            (not attrs["AnticuerposPancreaticos"].isCompleted() and (
                (not attrs["AlientoFuerteYDulce"].isCompleted()) or (not attrs["AlientoFuerteYDulce"].getValue())
            )) or 
            (not attrs["AlientoFuerteYDulce"].isCompleted() and (
                (not attrs["AnticuerposPancreaticos"].isCompleted()) or (not attrs["AnticuerposPancreaticos"].getValue())
            ))
        )
    ):
        return ["AnticuerposPancreaticos", "AlientoFuerteYDulce"]
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
    if attrs["PoseeLaboratorio"].isCompleted() and attrs["PoseeLaboratorio"] == False:
        return {
            "type": "RESULT"
        }


def createFrames():
    frames = {
        "TipoDiabetes": Frame("EntradaDiabetes", {
            "PoseeLaboratorio": Attribute(None, None, onComplete),
            "Glucemia": Attribute(None, None, onComplete),
            "AnticuerposPancreaticos": Attribute (None, None, onComplete),
            "AlientoFuerteYDulce": Attribute (None, None, onComplete),
        }),

        "ErrorTipo": Frame("Nulo", {
            "PoseeLaboratorio": Attribute(None, lambda poseeLab: not poseeLab, onCompleteError),
            "Glucemia": Attribute(None, None, onCompleteError),
            "AnticuerposPancreaticos": Attribute (None, None, onCompleteError),
            "AlientoFuerteYDulce": Attribute (None, None, onCompleteError),
            "CantidadSintomasParticulares": Attribute(None, None, onCompleteError),
        }),

        "DiabetesTipoNulo": Frame("Nulo", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc < 100, onComplete),
            "AnticuerposPancreaticos": Attribute (None, None, onComplete),
            "AlientoFuerteYDulce": Attribute (None, None, onComplete),
            "CantidadSintomasParticulares": Attribute(None, None, onComplete),
        }),

        "DiabetesTipo1": Frame("Tipo 1", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc >= 100, onComplete),
            "AnticuerposPancreaticos": Attribute (None, None, onComplete),
            "AlientoFuerteYDulce": Attribute (None, None, onComplete),
            "CantidadSintomasParticulares": Attribute(None, lambda cant: (cant > 0), onComplete),
        }),

        "DiabetesTipo2": Frame("Tipo 2", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee, onComplete),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc >= 100, onComplete),
            "AnticuerposPancreaticos": Attribute (None, None, onComplete),
            "AlientoFuerteYDulce": Attribute (None, None, onComplete),
            "CantidadSintomasParticulares": Attribute(None, lambda cant: cant == 0, onComplete),
        })
    }

    frames["TipoDiabetes"].addChildren(frames["DiabetesTipo2"])
    frames["TipoDiabetes"].addChildren(frames["DiabetesTipo1"])
    frames["TipoDiabetes"].addChildren(frames["DiabetesTipoNulo"])
    frames["TipoDiabetes"].addChildren(frames["ErrorTipo"])

    return frames["TipoDiabetes"]
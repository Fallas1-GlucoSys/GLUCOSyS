from inference_engine.Frame import Frame
from inference_engine.Attribute import Attribute

def createFrames():
    frames = {
        "ValoresDiabetes": Frame("EntradaDiabetes", {
            "PoseeLaboratorio": Attribute(None, None),
            "Glucemia": Attribute(None, None),
        }),

        "ErrorTipo": Frame("Nulo", {
            "PoseeLaboratorio": Attribute(None, lambda poseeLab: not poseeLab)
        }),

        "DiabetesTipoNulo": Frame("Diagnostico Posee Estudios", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc < 100),
        }),

        "PoseeDiabetes": Frame("PoseeDiabetes", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc >= 100),
        }),

        "DiabetesTipo1": Frame("Tipo 1", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc >= 100),
            "AnticuerposPancreaticos": Attribute (None, None),
            "AlientoFuerteYDulce": Attribute (None, None),
            "CantidadSintomasParticulares": Attribute(None, lambda cant: cant > 0),
        }),

        "DiabetesTipo2": Frame("Tipo 2", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valorGluc: valorGluc >= 100),
            "AnticuerposPancreaticos": Attribute (None, None),
            "AlientoFuerteYDulce": Attribute (None, None),
            "CantidadSintomasParticulares": Attribute(None, lambda cant: cant == 0),
        })
    }

    frames["PoseeDiabetes"].addChildren(frames["DiabetesTipo2"])
    frames["PoseeDiabetes"].addChildren(frames["DiabetesTipo1"])
    frames["ValoresDiabetes"].addChildren(frames["PoseeDiabetes"])
    frames["ValoresDiabetes"].addChildren(frames["DiabetesTipoNulo"])
    frames["ValoresDiabetes"].addChildren(frames["ErrorTipo"])

    return frames["ValoresDiabetes"]
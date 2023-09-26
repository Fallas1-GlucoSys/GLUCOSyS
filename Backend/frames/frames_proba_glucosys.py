from inference_engine.Frame import Frame
from inference_engine.Attribute import Attribute

def createFrames():
    frames = {
        "DiagnosticoVacio": Frame("Diagnóstico Vacío", {
            "PoseeLaboratorio": Attribute(None, None),
        }),

        "ErrorLaboratorio": Frame("Sin Resultado", {
            "PoseeLaboratorio": Attribute(None, lambda posee: (not posee)),
        }),

        "DiagnosticoPoseeEstudios": Frame("Diagnostico Posee Estudios", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, None),
        }),

        "DiabetesProbabilidadAltaGlucemiaAlta": Frame("Probabilidad Alta", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, None),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, None)
        }),

        "DiabetesProbabilidadNula": Frame("Probabilidad Nula", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia < 100))
        }),

        "GlucemiaBaja": Frame("Glucemia Baja", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 100 and valGlucemia < 120)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, None)
        }),

        "GlucemiaMedia": Frame("Glucemia Media", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, None)
        }),

        "DiabetesProbabilidadBajaGlucemiaBaja": Frame("Probabilidad Baja", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 100 and valGlucemia < 120)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, lambda cant: cant <= 2)
        }),

        "DiabetesProbabilidadMediaGlucemiaBaja": Frame("Probabilidad Media", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 100 and valGlucemia < 120)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, lambda cant: cant >= 3)
        }),

        "DiabetesProbabilidadBajaGlucemiaMedia": Frame("Probabilidad Baja", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180)),
            "Hambre": Attribute(None, lambda hambre: not hambre),
            "Orina": Attribute(None, lambda orina: not orina),
            "Sed": Attribute(None, lambda sed: not sed),
            "PerdidaDePeso": Attribute(None, lambda pdp: not pdp),
            "CantidadSintomas": Attribute(None, lambda cant: cant == 0)
        }),

        "DiabetesProbabilidadMediaGlucemiaMedia": Frame("Probabilidad Media", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, lambda cant: (cant <= 2 and cant > 0))
        }),


        "DiabetesProbabilidadAltaGlucemiaMedia": Frame("Probabilidad Alta", {
            "PoseeLaboratorio": Attribute(None, lambda posee: posee),
            "Glucemia": Attribute(None, lambda valGlucemia: (valGlucemia >= 120 and valGlucemia < 180)),
            "Hambre": Attribute(None, None),
            "Orina": Attribute(None, None),
            "Sed": Attribute(None, None),
            "PerdidaDePeso": Attribute(None, None),
            "CantidadSintomas": Attribute(None, lambda cant: cant > 2)
        })
    }
    frames["GlucemiaMedia"].addChildren(frames["DiabetesProbabilidadBajaGlucemiaMedia"])
    frames["GlucemiaMedia"].addChildren(frames["DiabetesProbabilidadMediaGlucemiaMedia"])
    frames["GlucemiaMedia"].addChildren(frames["DiabetesProbabilidadAltaGlucemiaMedia"])
    frames["GlucemiaBaja"].addChildren(frames["DiabetesProbabilidadBajaGlucemiaBaja"])
    frames["GlucemiaBaja"].addChildren(frames["DiabetesProbabilidadMediaGlucemiaBaja"])
    frames["DiagnosticoPoseeEstudios"].addChildren(frames["GlucemiaBaja"])
    frames["DiagnosticoPoseeEstudios"].addChildren(frames["GlucemiaMedia"])
    frames["DiagnosticoPoseeEstudios"].addChildren(frames["DiabetesProbabilidadAltaGlucemiaAlta"])
    frames["DiagnosticoPoseeEstudios"].addChildren(frames["DiabetesProbabilidadNula"])
    frames["DiagnosticoVacio"].addChildren(frames["DiagnosticoPoseeEstudios"])
    frames["DiagnosticoVacio"].addChildren(frames["ErrorLaboratorio"])
    return frames["DiagnosticoVacio"]

questions_sintomas_generales = [
    {
        "question": "¿Con qué frecuencia tiene usted hambre?",
        "field": "Hambre",
        "options": [
            {"value": True, "text_to_show": "Frecuente"},
            {"value": False, "text_to_show": "Normal o poca"},
        ]
    },
    {
        "question": "¿Con qué frecuencia orinas?",
        "field": "Orina",
        "options": [
            {"value": True, "text_to_show": "Frecuentemente"},
            {"value": False, "text_to_show": "De forma usual o escasa"},
        ]
    },
    {
        "question": "¿Cómo encuentra usted su pérdida de peso?",
        "field": "PerdidaDePeso",
        "options": [
            {"value": True, "text_to_show": "Sostenida y sin causa"},
            {"value": False, "text_to_show": "Normal"},
        ]
    },
    {
        "question": "¿Cómo se siente usualmente en cuanto a su hidratación?",
        "field": "Sed",
        "options": [
            {"value": True, "text_to_show": "Sed Frecuente"},
            {"value": False, "text_to_show": "Hidratado"},
        ]
    }
]

questions_sintomas_particulares = [
    {
        "question": "Usted describiría a su aliento como...",
        "field": "AlientoFuerteYDulce",
        "options": [
            {"value": True, "text_to_show": "Fuerte y dulce"},
            {"value": False, "text_to_show": "Otra"},
        ]
    },
    {
        "question": "¿Posee usted anticuerpos pancreáticos?",
        "field": "AnticuerposPancreaticos",
        "options": [
            {"value": True, "text_to_show": "Sí"},
            {"value": False, "text_to_show": "No"},
        ]
    }
]

questions_glucemia = [
    {
        "question": "¿Que valores de glucemia presenta en sus análisis de laboratorio?",
        "field": "Glucemia",
        "options": [
            {"value": 10, "text_to_show": "Menor a 100 mg/dL"},
            {"value": 110, "text_to_show": "Entre 100 y 120 mg/dL"},
            {"value": 150, "text_to_show": "Entre 120 y 180 mg/dL"},
            {"value": 190, "text_to_show": "Mas de 180 mg/dL"},
        ]
    },
]
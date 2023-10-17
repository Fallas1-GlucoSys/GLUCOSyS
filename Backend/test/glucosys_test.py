from app.glucosys_with_frames import glucosys

def test_non_has_lab():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": False
    }
    response = glucosys(data_entry)
    assert(response["type"] == "Desconocido")
    assert(response["probability"] == "Desconocida")


def test_has_lab_asks_for_glucemia():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 1)
    assert(response["questions"][0]["question"] == '¿Que valores de glucemia presenta en sus análisis de laboratorio?')
    assert(response["questions"][0]["field"] == "Glucemia")


def test_glucemia_less_than_100_returns_null_result():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 80
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "RESULT")
    assert(response["type"] == "Nulo")


def test_glucemia_over_180_asks_for_specific_symptoms():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 190
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 2)
    assert(response["questions"][0]["question"] == "Usted describiría a su aliento como...")
    assert(response["questions"][0]["field"] == "AlientoFuerteYDulce")
    assert(response["questions"][1]["question"] == "¿Posee usted anticuerpos pancreáticos?")
    assert(response["questions"][1]["field"] == "AnticuerposPancreaticos")


def test_glucemia_between_120_and_180_asks_for_general_symptoms():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 140
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 4)
    assert(response["questions"][0]["field"] == "Hambre")
    assert(response["questions"][1]["field"] == "Orina")
    assert(response["questions"][2]["field"] == "PerdidaDePeso")
    assert(response["questions"][3]["field"] == "Sed")


def test_glucemia_between_100_and_120_asks_for_general_symptoms():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 110
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 4)
    assert(response["questions"][0]["field"] == "Hambre")
    assert(response["questions"][1]["field"] == "Orina")
    assert(response["questions"][2]["field"] == "PerdidaDePeso")
    assert(response["questions"][3]["field"] == "Sed")


def test_glucemia_between_100_and_120_with_general_symptoms_asks_for_specific_symptoms():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 110,
        "Hambre": True,
        "Orina": True,
        "PerdidaDePeso": True,
        "Sed": True
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 2)
    assert(response["questions"][0]["field"] == "AlientoFuerteYDulce")
    assert(response["questions"][1]["field"] == "AnticuerposPancreaticos")


def test_glucemia_between_120_and_180_with_general_symptoms_asks_for_specific_symptoms():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 160,
        "Hambre": True,
        "Orina": True,
        "PerdidaDePeso": True,
        "Sed": True
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "QUESTIONS")
    assert(len(response["questions"]) == 2)
    assert(response["questions"][0]["field"] == "AlientoFuerteYDulce")
    assert(response["questions"][1]["field"] == "AnticuerposPancreaticos")


def test_glucemia_between_120_and_180_with_general_and_specific_symptoms_determines_result():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 160,
        "Hambre": True,
        "Orina": True,
        "PerdidaDePeso": True,
        "Sed": True,
        "AlientoFuerteYDulce": True,
        "AnticuerposPancreaticos": True
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "RESULT")
    assert(response["type"] == "Tipo 1")
    assert(response["probability"] == "Probabilidad Alta")


def test_glucemia_between_100_and_120_with_general_and_specific_symptoms_determines_result():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 110,
        "Hambre": True,
        "Orina": True,
        "PerdidaDePeso": True,
        "Sed": True,
        "AlientoFuerteYDulce": False,
        "AnticuerposPancreaticos": False
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "RESULT")
    assert(response["type"] == "Tipo 2")
    assert(response["probability"] == "Probabilidad Media")


def test_glucemia_over_180_with_specific_symptoms_determines_result():
    data_entry = {
        "ClientId": 0,
        "PoseeLaboratorio": True,
        "Glucemia": 190,
        "AlientoFuerteYDulce": False,
        "AnticuerposPancreaticos": False
    }
    response = glucosys(data_entry)
    assert(response["response_type"] == "RESULT")
    assert(response["type"] == "Tipo 2")
    assert(response["probability"] == "Probabilidad Alta")
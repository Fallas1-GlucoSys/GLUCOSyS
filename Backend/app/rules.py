from rule_engine import Rule, Context, type_resolver_from_dict, DataType

context = Context(type_resolver=type_resolver_from_dict({
    'Hambre': DataType.BOOLEAN,
    'Orina': DataType.BOOLEAN,
    'Sed': DataType.BOOLEAN,
    'PerdidaDePeso': DataType.BOOLEAN,
    'Glucemia': DataType.FLOAT,
    'AnticuerposPancreaticos': DataType.BOOLEAN,
    'AlientoFuerteYDulce': DataType.BOOLEAN
}))

rules = {
    #rule r1
    Rule('''
        Hambre == true 
        and Orina == false 
        and Sed == false 
        and PerdidaDePeso == true 
        and Glucemia >= 100 
        and Glucemia <= 120 
        and AnticuerposPancreaticos == false 
        and AlientoFuerteYDulce == true
    ''', context=context)
    : 
    "Resultado: Tipo Diabetes: 1, Probabilidad: Baja."
    ,
    #rule r2
    Rule(''' 
        Hambre == false 
        and Orina == true 
        and Sed == true 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    "Resultado: Tipo Diabetes: 1, Probabilidad: Baja."
    ,
    #rule r3
    Rule(''' 
        Hambre == false 
        and Orina == true 
        and Sed == false 
        and PerdidaDePeso == true 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r4
    Rule(''' 
        Hambre == true 
        and Orina == false 
        and Sed == true 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r5
    Rule(''' 
        Hambre == false 
        and Orina == false 
        and Sed == true 
        and PerdidaDePeso == true 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r6
    Rule(''' 
        Hambre == true 
        and Orina == true 
        and Sed == false 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r7
    Rule(''' 
        Hambre == true 
        and Orina == false 
        and Sed == false 
        and PerdidaDePeso == false 
        and Glucemia >= 120
        and Glucemia <= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r8
    Rule(''' 
        Hambre == false 
        and Orina == true 
        and Sed == false 
        and PerdidaDePeso == false 
        and Glucemia >= 120
        and Glucemia <= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r9
    Rule(''' 
        Hambre == false 
        and Orina == false 
        and Sed == true 
        and PerdidaDePeso == false 
        and Glucemia >= 120
        and Glucemia <= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r10
    Rule(''' 
        Hambre == false 
        and Orina == false 
        and Sed == false 
        and PerdidaDePeso == true 
        and Glucemia >= 120
        and Glucemia <= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r11
    Rule(''' 
        Hambre == true 
        and Orina == false 
        and Sed == false 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    ,
    #rule r12
    Rule(''' 
        Hambre == false 
        and Orina == false 
        and Sed == true 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia <= 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    'Resultado: Tipo Diabetes: 1. Probabilidad: Baja.'
    

}


     
    

    


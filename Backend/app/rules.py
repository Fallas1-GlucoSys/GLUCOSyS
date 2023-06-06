from rule_engine import Rule, Context, type_resolver_from_dict, DataType

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
'''

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
        and Glucemia < 120 
        and AnticuerposPancreaticos == false 
        and AlientoFuerteYDulce == true
    ''', context=context)
    : 
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r2
    Rule(''' 
        Hambre == false 
        and Orina == true 
        and Sed == true 
        and PerdidaDePeso == false 
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r3
    Rule(''' 
        Hambre == false 
        and Orina == true 
        and Sed == false 
        and PerdidaDePeso == true 
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r4
    Rule(''' 
        Hambre == false 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r5
    Rule(''' 
        Hambre == true
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r6
    Rule(''' 
        Hambre == false
        and Orina == false
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r7
    Rule(''' 
        Hambre == false
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r8
    Rule(''' 
        Hambre == true 
        and Orina == false
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r9
    Rule(''' 
        Hambre == true
        and Orina == true
        and Sed == false
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r10
    Rule(''' 
        Hambre == true
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r11
    Rule(''' 
        Hambre == false
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    }
    ,
    #rule r12
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r13
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r14
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r15
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r16
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == true
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r17
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 180
        and AnticuerposPancreaticos == true
        and AlientoFuerteYDulce == true
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r18
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 180
        and AnticuerposPancreaticos == true
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r19
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == true
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r20
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == true
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 1",
        "info": INFO_DIABETES_TIPO_1
    },
    #rule r21
    Rule(''' 
        Hambre == true 
        and Orina == false
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r22
    Rule(''' 
        Hambre == true 
        and Orina == false
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r23
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r24
    Rule(''' 
        Hambre == false 
        and Orina == false
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r25
    Rule(''' 
        Hambre == false 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r26
    Rule(''' 
        Hambre == false
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Baja",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r27
    Rule(''' 
        Hambre == false
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r28
    Rule(''' 
        Hambre == true 
        and Orina == false
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r29
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r30
    Rule(''' 
        Hambre == false 
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r31
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 100
        and Glucemia < 120
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Media",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r32
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r33
    Rule(''' 
        Hambre == true 
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 120
        and Glucemia < 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r34
    Rule(''' 
        Hambre == false
        and Orina == true
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r35
    Rule(''' 
        Hambre == true
        and Orina == false
        and Sed == true
        and PerdidaDePeso == false
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r36
    Rule(''' 
        Hambre == true
        and Orina == true
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r37
    Rule(''' 
        Hambre == true
        and Orina == true
        and Sed == true
        and PerdidaDePeso == true
        and Glucemia >= 180
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Alta",
        "type": "Tipo 2",
        "info": INFO_DIABETES_TIPO_2
    },
    #rule r38
    Rule(''' 
        Hambre == false
        and Orina == false
        and Sed == false
        and PerdidaDePeso == false
        and Glucemia < 100
        and AnticuerposPancreaticos == false
        and AlientoFuerteYDulce == false
    ''', context=context)
    :
    {
        "probability": "Nula",
        "type": "Ninguno",
        "info": 'Según los datos introducidos, no tiene de que preocuparse ya que su probabilidad de tener actualmente diabetes es nula.'
    },
}


     
    

    


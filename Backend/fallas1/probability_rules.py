from rule_engine import Rule, Context, type_resolver_from_dict, DataType

context = Context(type_resolver=type_resolver_from_dict({
    'CantSintomasGrales': DataType.FLOAT,
    'Glucemia': DataType.FLOAT,
}))

probability_rules = {
    Rule('Glucemia > 180', context):'Alta',
    Rule('Glucemia <= 100', context):'Nula',
    Rule('Glucemia > 100 and Glucemia <= 120 and CantSintomasGrales >= 3', context):'Media',
    Rule('Glucemia > 100 and Glucemia <= 120 and CantSintomasGrales <= 2 and CantSintomasGrales >= 0', context):'Baja',
    Rule('Glucemia > 120 and Glucemia <= 180 and CantSintomasGrales >= 1 and CantSintomasGrales <= 2', context): 'Media',
    Rule('Glucemia > 120 and Glucemia <= 180 and CantSintomasGrales >= 3', context):'Alta',
    Rule('Glucemia > 120 and Glucemia <= 180 and CantSintomasGrales == 0', context):'Baja'
}
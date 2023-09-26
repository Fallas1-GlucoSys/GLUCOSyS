from rule_engine import Rule, Context, type_resolver_from_dict, DataType

context = Context(type_resolver=type_resolver_from_dict({
    'AnticuerposPancreativos': DataType.BOOLEAN,
    'AlientoFuerteYDulce': DataType.BOOLEAN,
}))

diabetes_type_rules = {
    Rule('AnticuerposPancreaticos == true'): 'Tipo 1',
    Rule('AlientoFuerteYDulce == true'): 'Tipo 1',
    Rule('AlientoFuerteYDulce == false and AnticuerposPancreaticos == false'): 'Tipo 2'
}
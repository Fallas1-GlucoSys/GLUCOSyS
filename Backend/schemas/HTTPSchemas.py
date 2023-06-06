from pydantic import BaseModel

class InputForRules(BaseModel):
    Hambre: bool | None
    Orina: bool | None
    Sed: bool | None
    PerdidaDePeso: bool | None
    Glucemia: float | None
    AnticuerposPancreaticos: bool | None
    AlientoFuerteYDulce: bool | None
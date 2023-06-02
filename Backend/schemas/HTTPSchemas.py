from typing import List, Optional, Union
from pydantic import BaseModel

class InputForRules(BaseModel):
    Hambre: bool
    Orina: bool
    Sed: bool
    PerdidaDePeso: bool
    Glucemia: float
    AnticuerposPancreaticos: bool
    AlientoFuerteYDulce: bool

class DiabetesResponse(BaseModel):
    probability: str
    type: str
    info: str


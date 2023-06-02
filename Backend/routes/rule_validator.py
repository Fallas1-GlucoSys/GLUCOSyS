from fastapi import APIRouter, status, Request, HTTPException
from schemas.HTTPSchemas import InputForRules, DiabetesResponse
from app.glucosys import glucosys
import logging

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

@router.post("/diabetes_probability", status_code = status.HTTP_200_OK, response_model=DiabetesResponse)
async def diabetes_probability(datosUsuario: InputForRules):
    try:
        dictDatosUser = datosUsuario.dict()
        print(dictDatosUser)
        response = glucosys(datosUsuario=dictDatosUser)
        logger.info(f"Response: {response}") 
        return response
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {e}") from e

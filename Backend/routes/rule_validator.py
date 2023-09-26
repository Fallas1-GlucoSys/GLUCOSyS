from fastapi import APIRouter, status, HTTPException
from schemas.HTTPSchemas import InputForRules
from app.glucosys_with_frames import glucosys
import logging

router = APIRouter()
logger = logging.getLogger("uvicorn.error")

@router.post("/diabetes_probability", status_code = status.HTTP_200_OK)
async def diabetes_probability(datosUsuario: InputForRules):
    try:
        dictDatosUser = datosUsuario.dict()
        response = glucosys(datosUsuario=dictDatosUser)
        logger.info(f"Response: {response}") 
        return response
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal error: {e}") from e

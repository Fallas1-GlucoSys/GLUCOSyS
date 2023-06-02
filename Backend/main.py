import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.rule_validator import router as rule_validator_routes


origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rule_validator_routes)

if __name__ == '__main__':
    uvicorn.run("main:app", port=3100, log_level="info")

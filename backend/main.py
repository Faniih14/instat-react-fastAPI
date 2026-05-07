from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.database import SessionLocal
from auth.routes import router as auth_router
app = FastAPI()


#appel route authentification
app.include_router(auth_router,prefix="/auth",tags=["auth"]) 


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FastAPI fonctionne !"}


#  fonction qui gere toute la session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

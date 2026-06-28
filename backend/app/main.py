from fastapi import FastAPI #FastAPI -nin kitabxanasini istifade edecem, onu cagir
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import user, product, order
from app.routers import users
#now below I am creating database tables
Base.metadata.create_all(bind=engine)

app=FastAPI(title="StyleShop API", version="1.0")  #I am creating my backend application
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

app.include_router(users.router)

@app.get("/")  #if someone comes to my main backend server with GET request, home() function functions
def home():
    return {"message": "StyleShop API işləyir!"}

@app.get("/health")
def health():
    return {"status": "ok"}



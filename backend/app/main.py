from fastapi import FastAPI #FastAPI -nin kitabxanasini istifade edecem, onu cagir
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title="StyleShop API", version="1.0")  #I am creating my backend application
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

@app.get("/")  #if someone comes to my main backend server with GET request, home() function functions
def home():
    return {"message": "StyleShop API işləyir!"}

@app.get("/health")
def health():
    return {"status": "ok"}

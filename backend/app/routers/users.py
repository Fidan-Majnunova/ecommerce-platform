from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#data format for register schemas
class RegisterSchema(BaseModel):
    name: str
    email: str
    password: str

# data format in login schemas
class LoginSchema(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    # does this email already exist?
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu email artıq qeydiyyatdadır")
    
    hashed_password = pwd_context.hash(data.password) #hashing the password
    
    new_user = User(   #I am creating new user
        name=data.name,
        email=data.email,
        password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Qeydiyyat uğurlu oldu!", "user_id": new_user.id}

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    # does this user already in the system?
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="İstifadəçi tapılmadı")
    
    # is the password correct?
    if not pwd_context.verify(data.password, user.password):
        raise HTTPException(status_code=400, detail="Şifrə yanlışdır")
    
    return {"message": "Giriş uğurlu oldu!", "user_id": user.id, "name": user.name}
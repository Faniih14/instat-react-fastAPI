from fastapi import APIRouter,Depends
from db.database import get_db
from sqlalchemy.orm import Session
from schemas.createUser import CreateUser
from .hashing import hash_password
from models.users import User

router=APIRouter()

#route register
@router.post("/register")
def register(user:CreateUser,db:Session=Depends(get_db)):
    user.password=hash_password(user.password)
    db_user=User(name=user.name,
                 firstname=user.firstname,
                 email=user.email,
                 password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"massage":"utilisateur cree"}



#route login
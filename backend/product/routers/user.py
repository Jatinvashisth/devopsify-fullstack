from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from fastapi import status
from .. import models, schemas
from ..database import get_db


router = APIRouter()



@router.post("/signup",response_model=schemas.DisplayUser, status_code=status.HTTP_201_CREATED)
def add_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
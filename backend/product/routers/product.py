from product.routers.login import get_current_user
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db


router = APIRouter(
    tags=["product"]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
def add_user(request: schemas.UserData, db: Session = Depends(get_db)):
    new_user = models.UserData(
    name=request.name,
    email=request.email,
    phone=request.phone,
    address=request.address,

)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@router.get("/all", response_model=List[schemas.UserData])
def fetchData(db: Session = Depends(get_db), current_user:schemas.User= Depends(get_current_user)):
    UserData = db.query(models.UserData).all()
    return UserData




@router.get("/user/{id}", response_model=schemas.UserData)
def get_product(id: int, db: Session = Depends(get_db)):
    Userdata = db.get(models.UserData, id)
    if not Userdata:
        raise HTTPException(status_code=404, detail="Product not found")
    return Userdata



@router.delete("/delete/{id}")
def delete_User(id: int, db: Session = Depends(get_db)):
    Userdata = db.get(models.UserData, id)
    if not Userdata:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(Userdata)
    db.commit()
    return {"message": "Product deleted successfully"}



@router.put("/update/{id}")
def update_product(id: int, updated_data: schemas.UserData, db: Session = Depends(get_db)):
    Userdata = db.get(models.UserData, id)
    if not Userdata:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated_data.dict().items():
        setattr(Userdata, key, value)

    db.commit()
    db.refresh(Userdata)
    return {"message": "Product updated successfully", "data": Userdata}



@router.get("/user/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = db.query(models.UserData).filter(models.UserData.email == email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="No user found")

    return user



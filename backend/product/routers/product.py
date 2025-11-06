from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas
from ..database import get_db
from product.routers.login import get_current_user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

# ---------------- CREATE USER ----------------
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserData, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(models.UserData).filter(models.UserData.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = models.UserData(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address,
    )
    db.add(new_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to create user due to duplicate entry")
    db.refresh(new_user)
    return new_user

# ---------------- GET ALL USERS ----------------
@router.get("/all", response_model=List[schemas.UserData])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: schemas.UserData = Depends(get_current_user)
):
    users = db.query(models.UserData).all()
    return users

# ---------------- GET USER BY ID ----------------
@router.get("/{id}", response_model=schemas.UserData)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.get(models.UserData, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ---------------- GET USER BY EMAIL ----------------
@router.get("/email/{email}", response_model=schemas.UserData)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = db.query(models.UserData).filter(models.UserData.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ---------------- UPDATE USER ----------------
@router.put("/update/{id}")
def update_user(id: int, updated_data: schemas.UserData, db: Session = Depends(get_db)):
    user = db.get(models.UserData, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in updated_data.model_dump().items():
        setattr(user, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Failed to update user: duplicate email?")
    
    db.refresh(user)
    return {"message": "User updated successfully", "data": user}

# ---------------- DELETE USER ----------------
@router.delete("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.get(models.UserData, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

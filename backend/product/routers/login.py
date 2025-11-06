from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

# ---------------- JWT CONFIG ----------------
SECRET_KEY = "your_secret_key_here"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

router = APIRouter(tags=["Auth"])

# ---------------- Generate Token Helper ----------------
def generate_token(data: dict):
    """JWT token create karega email-based."""
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# ---------------- Login (JSON friendly) ----------------
@router.post("/login", response_model=schemas.Token)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user or user.password != request.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password"
        )

    access_token = generate_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------- Get Current User ----------------
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise credentials_exception
    return user

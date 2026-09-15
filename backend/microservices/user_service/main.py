from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .schemas import UserCreate, UserLogin, UserResponse
from .crud import create_user, authenticate_user
from .auth import create_access_token

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Microservice")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user.email, user.password, user.full_name)
    return new_user


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.email, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": auth_user.email})
    return {"access_token": token, "token_type": "bearer"}

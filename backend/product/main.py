from fastapi import FastAPI
from . import schemas, models
from .database import engine
from .routers import product, login, user
from fastapi.middleware.cors import CORSMiddleware

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Include routers
app.include_router(product.router)
app.include_router(user.router)
app.include_router(login.router)

# Allowed origins
origins = [
    "http://localhost:5173",  # local React
    "https://your-netlify-site.netlify.app",  # deployed frontend
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # Use the origins list
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






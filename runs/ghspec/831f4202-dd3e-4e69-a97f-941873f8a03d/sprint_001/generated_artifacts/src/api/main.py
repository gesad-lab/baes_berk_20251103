```python
import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Validate that required environment variables are set
REQUIRED_ENV_VARS = ["DATABASE_URL", "SECRET_KEY"]

for var in REQUIRED_ENV_VARS:
    if var not in os.environ:
        raise ValueError(f"Environment variable '{var}' is required.")

# Initialize FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# When creating models, make sure to define them using the Base class
# ...

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Student Management API"}

# Additional routes for adding and retrieving students would go here
# ...
```
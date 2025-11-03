```python
from fastapi import FastAPI
from alembic import command
from alembic.config import Config
from database import engine
from models import Base  # Assuming your SQLAlchemy models are in src/models.py

app = FastAPI()

@app.on_event("startup")
async def startup():
    """Apply database migrations on application startup."""
    alembic_cfg = Config("alembic.ini")
    # Upgrade the database schema to the latest version
    command.upgrade(alembic_cfg, "head") 
    # Create any missing tables
    Base.metadata.create_all(bind=engine)
```
```python
# src/main.py

from fastapi import FastAPI
from alembic.config import Config
from alembic import command

app = FastAPI()

# Other existing code...

@app.on_event("startup")
async def startup():
    """Run migrations on application startup."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Run latest migrations to ensure database schema is up to date

# Continue with other existing code...
```
'''
Initializes the FastAPI application and includes the API router.
'''
from fastapi import FastAPI
from api import router
from database import create_database, migrate_database
app = FastAPI()
# Create the database and tables
create_database()
# Migrate the database to add the email field and create the Course table
migrate_database()
# Include the router
app.include_router(router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
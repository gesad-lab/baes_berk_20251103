from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    """Health check endpoint that returns 200 OK."""
    return {"status": "healthy"}
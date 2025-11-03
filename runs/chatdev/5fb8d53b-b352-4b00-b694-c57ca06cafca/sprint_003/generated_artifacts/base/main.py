'''
Runs the FastAPI application using Uvicorn.
'''
if __name__ == "__main__":
    import os
    os.system("uvicorn main:app --reload")
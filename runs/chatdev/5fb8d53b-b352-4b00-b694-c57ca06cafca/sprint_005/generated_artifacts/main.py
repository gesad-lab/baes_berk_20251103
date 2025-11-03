'''
Runs the FastAPI application using Uvicorn.
'''
from fastapi import FastAPI
from routes import student_router, course_router, teacher_router
app = FastAPI()
app.include_router(student_router)
app.include_router(course_router)
app.include_router(teacher_router)
if __name__ == "__main__":
    import os
    os.system("uvicorn main:app --reload")
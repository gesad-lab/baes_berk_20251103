from setuptools import setup, find_packages

setup(
    name='student_api',
    version='1.0.0',
    description='A FastAPI application for managing student records',
    packages=find_packages(),
    install_requires=[
        'fastapi[all]',  # FastAPI framework, includes uvicorn for ASGI server
        'sqlalchemy',    # ORM for handling database interactions
        'pytest',        # Testing framework for unit and integration tests
    ],
    python_requires='>=3.11',  # Specify the required Python version
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Framework :: FastAPI',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
)
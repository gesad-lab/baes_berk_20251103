from setuptools import setup, find_packages

setup(
    name='student_management',
    version='0.1.0',
    description='A simple web application to manage student information using Flask and SQLite',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/student_management',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0,<3.0',
        'SQLAlchemy>=1.4,<2.0',
        'pytest>=6.2,<7.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
        'Framework :: Flask',
    ],
    python_requires='>=3.11',
)
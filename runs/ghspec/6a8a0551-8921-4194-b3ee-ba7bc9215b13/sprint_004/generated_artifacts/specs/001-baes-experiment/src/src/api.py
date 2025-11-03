```python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from api import create_app, db
from api.models import Enrollment  # Assuming Enrollment is defined in models.py

app = create_app()
migrate = Migrate(app, db)

# Initialize the Flask-Script manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
```
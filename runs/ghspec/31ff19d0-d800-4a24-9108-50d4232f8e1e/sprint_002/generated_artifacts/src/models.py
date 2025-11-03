class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required field
    email = db.Column(db.String, nullable=False, unique=True)  # New field added

    def __repr__(self):
        return f'<Student {self.name}, Email: {self.email}>'
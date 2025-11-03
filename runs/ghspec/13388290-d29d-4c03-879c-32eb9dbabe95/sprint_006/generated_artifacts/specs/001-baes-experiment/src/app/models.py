class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=True)  # Added foreign key for teacher

    # Establishing the relationship with Teacher model
    teacher = db.relationship('Teacher', backref='courses')  # Back reference to access all courses of a teacher
from main import db

students = db.Table('sections_students',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('sections.id'), primary_key=True)
)

class Section(db.Model):
    __tablename__="sections"
    id=db.Column(db.Integer,primary_key=True)
    university_id=db.Column(db.Integer,db.ForeignKey("universities.id"))
    period_id=db.Column(db.Integer,db.ForeignKey("periods.id"))
    course_id=db.Column(db.Integer,db.ForeignKey("courses.id"))
    students=db.relationship('Student', secondary=students, lazy='subquery',
        backref=db.backref('sections', lazy=True))
    teacher_id=db.Column(db.Integer,db.ForeignKey("teachers.id"))
    classroom=db.Column(db.String(10))
    def __init__(self, university_id, period_id, course_id, teacher_id, classroom):
        self.university_id=university_id
        self.period_id=period_id
        self.course_id=course_id
        self.teacher_id=teacher_id
        self.classroom=classroom

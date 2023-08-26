
from main import db

class section_students(db.Model):
    __tablename__="section_students"
    id=db.Column(db.Integer,primary_key=True)
    student_id=db.Column(db.Integer,db.ForeignKey("students.id"))
    section_id=db.Column(db.Integer,db.ForeignKey("sections.id"))
    def __init__(self, student_id, section_id):
        self.student_id=student_id
        self.section_id=section_id
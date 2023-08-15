from main import db

class Student(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True)
    university_id=db.Column(db.Integer,db.ForeignKey("universities.id"))
    name=db.Column(db.String(50))

    def __init__(self,name,university_id):
        self.name=name
        self.university_id=university_id

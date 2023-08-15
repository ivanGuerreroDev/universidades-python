from main import db

class Teacher(db.Model):
    __tablename__="teachers"
    id=db.Column(db.Integer,primary_key=True)
    university_id=db.Column(db.Integer,db.ForeignKey("universities.id"))
    name=db.Column(db.String(50))

    def __init__(self,name,university_id):
        self.name=name
        self.university_id=university_id

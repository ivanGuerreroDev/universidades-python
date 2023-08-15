from main import db

class Course(db.Model):
  __tablename__="courses"
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100),nullable=False)
  university_id=db.Column(db.Integer,db.ForeignKey("universities.id"))
  department_id=db.Column(db.Integer,db.ForeignKey("departments.id"))
  def __init__(self,name,university_id,department_id):
    self.name=name
    self.university_id=university_id
    self.department_id=department_id

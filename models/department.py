from main import db

class Department(db.Model):
  __tablename__="departments"
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(100),nullable=False)
  def __init__(self,name):
    self.name=name

from main import db

class University(db.Model):
    __tablename__="universities"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

    def __init__(self,name):
        self.name=name
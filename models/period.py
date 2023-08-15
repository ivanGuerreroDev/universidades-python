from main import db

class Period(db.Model):
    __tablename__="periods"
    id=db.Column(db.Integer,primary_key=True)
    year=db.Column(db.Integer)
    semester=db.Column(db.Integer)

    def __init__(self,year,semester):
        self.year=year
        self.semester=semester

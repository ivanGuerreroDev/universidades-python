from flask import Blueprint, render_template,request,redirect,flash
from models.student import Student,db
from models.university import University,db
students=Blueprint("students",__name__,url_prefix="/student",template_folder="../templates/student")

@students.route("/create",methods=['POST','GET'])
def create():
  try:
      if request.method=="GET":
          universities=University.query.all()
          return render_template('create.html', universities=universities)
      if request.method=="POST":
          name=request.form["name"]
          university_id=request.form["university"]
          student=Student(name,university_id)
          db.session.add(student)
          db.session.commit()
          return redirect("/student")
  except:
      flash("error occured")
      universities=University.query.all()
      return render_template('create.html', universities=universities)

@students.route("/update/<id>",methods=['POST','GET'])
def update(id):
  try:
      if request.method=="GET":
          student=Student.query.filter_by(id=id).first()
          universities=University.query.all()
          return render_template('update.html',student=student, universities=universities)
      if request.method=="POST":
          name=request.form["name"]
          university_id=request.form["university_id"]
          student=Student.query.filter_by(id=id).first()
          student.name=name
          student.university_id=university_id
          db.session.commit()
          return redirect("/student")
  except Exception as error:
      print(str(error))
      flash("error occured")
      return render_template('update.html')
  return render_template('update.html')

@students.route("/delete/<id>")
def delete(id):
  print("student delete route ", id)
  try:
      student=Student.query.filter_by(id=id).first()
      db.session.delete(student)
      db.session.commit()
      print("student deleted successfully")
      return redirect("/student")
  except Exception as error:
      print(str(error))
      flash("error occured")
      return redirect("/student")
  
@students.route("/",methods=['GET'])
def index():
  students=Student.query.join(University).all()
  return render_template("student/index.html",students=students)


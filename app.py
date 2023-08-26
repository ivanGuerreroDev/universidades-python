from config import app
from controllers.home import home
from controllers.user import users
from controllers.student import students

#register blueprints
app.register_blueprint(home)
app.register_blueprint(users)
app.register_blueprint(students)

# uncomment this to run 

if __name__=="__main__":
    app.run(debug=True,port=5000)
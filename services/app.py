from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import User
from dbConnection.connection import DbConnect
from daoServices.crud import CRUDOperations

app = Flask(__name__)

# Configure SQLAlchemy
db = DbConnect()
engine = create_engine(db.establish_connection())
Session = sessionmaker(bind=engine)
session = Session()

# Initialize CRUD operations
crud = CRUDOperations(session)

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        nationalId = request.form['nationalId']
        email = request.form['email']
        cellphone = request.form['cellphone']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        # Create a new user
        user = User(first_name=firstName, last_name=lastName,national_id=nationalId, 
                    email_id=email,teleph_number=cellphone, password=password,
                    confirm_password=confirmPassword)
        # Add user to database
        crud.create_user(user)
        return 'User registered successfully!'

if __name__ == '__main__':
    app.run(debug=True)

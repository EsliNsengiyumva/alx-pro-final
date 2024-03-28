from flask import Flask, render_template, request,redirect, url_for,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import User
from dbConnection.connection import DbConnect
from daoServices.crudUser import CrudUserOperation
from daoServices.crudApplication import *
from daoServices.crudLogin import CrudLoginOperation 


app = Flask(__name__)

mysql_config = {
    'host': 'localhost',
    'user': 'sqluser',
    'password': 'password',
    'database': 'smartpermit'
}

# Initialize CRUD operations
crud = CrudUserOperation()
crud_login=CrudLoginOperation()
db = DbConnect(mysql_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
       return render_template('login.html')
   
@app.route('/welcome')
def welcome():
    # Render the welcome page
    return render_template('welcome.html')
   
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check user credentials (replace with your own logic)
        # email = request.form.get('email')
        # password = request.form.get('password')
        
        # if email == 'eslinsengiyumva@gmail' and password == 'password':
            # Redirect to the next page after successful login
        return redirect(url_for('welcome'))
        # else:
        #     return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')


    

  
@app.route('/application')
def application():
    
    return render_template('application.html')  


# # Route for handling form submission
# @app.route('/create_application', methods=['POST'])
# def create_application():
#     # Get form data
#     full_name = request.form['fullName']
#     applicant_category = request.form['category']
#     applicant_type = request.form['applicantType']
#     national_id = request.form['identity']
#     teleph_number = request.form['telephoneContact']
#     email_id = request.form['emailAddress']
#     date_app = request.form['applicationDate']
#     # Additional form fields...

#     # Create a new user (if not already exists) or retrieve existing user
#     #session = Session()
#     user = session.query(User).filter_by(email_id=email_id).first()
#     if not user:
#         user = User(first_name='', last_name='', national_id=national_id, teleph_number=teleph_number,
#                     email_id=email_id, password='', confirm_password='')
#         session.add(user)
#         session.commit()

#     # Create a new water permit application
#     application = WaterPermitApplication(full_Name=full_name, applicant_category=applicant_category,
#                                          applicant_type=applicant_type, national_id=national_id,
#                                          teleph_number=teleph_number, email_id=email_id, date_app=date_app,
#                                          user_id=user.user_id)
#     session.add(application)
#     session.commit()
#     session.close()

#     return 'Application created successfully'

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

    return render_template('forgot_password.html')



if __name__ == '__main__':
    app.run(debug=True)




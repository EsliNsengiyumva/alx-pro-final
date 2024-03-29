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

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

    return render_template('forgot_password.html')


@app.route('/application', methods=['POST'])
def submit():
    # Process form data here if needed
    # Redirect to success page
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)




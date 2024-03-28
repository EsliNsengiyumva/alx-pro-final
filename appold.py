from flask import Flask, render_template,url_for,redirect,request,Flask,flas
import mysql.connector
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'  # Set a secret key for flashing messages
# MySQL connection configuration
mysql_config = {
    'host': 'localhost',
    'user': 'sqluser',
    'password': 'password',
    'database': 'smartpermit'
}

conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

print('connection is done!')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/application')
def application():
    return render_template('index.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get data from the form
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        national_id = request.form['nationalId']
        cellphone = request.form['cellphone']
        email = request.form['email']        
        password_hash = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Insert data into the users table
        query = (
            "INSERT INTO water_permit_user (first_name, last_name, national_id,teleph_number, email_id,password, confirm_password) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        data = (first_name, last_name, national_id, email, cellphone, password_hash, confirm_password)

        try:
            cursor.execute(query, data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            return f"Error: {str(e)}"

        return redirect(url_for('index'))  # Redirect to the homepage or another page after successful registration

    return render_template('register.html')  # Render the registration form



cursor = conn.cursor(dictionary=True)

# Endpoint to handle login requests
@app.route('/login', methods=['POST'])
def login():
    # Get email and password from request data
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        # Check credentials using the provided method
        is_valid = crud_login.check_credentials(email, password)
        
        if is_valid:
            # Redirect to a welcome or home page upon successful login
            return redirect(url_for('welcome'))
        else:
            # Render the login page with an error message
            return render_template('login.html', error='Invalid email or password')

    else:
        # Render the login page
        return render_template('login.html')
    
@app.route('/welcome')
def welcome():
    # Render the welcome page
    return render_template('welcome.html')







app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with your email server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'nssli2@yahoo.fr'
app.config['MAIL_PASSWORD'] = '#Muhigi83#'
app.config['MAIL_DEFAULT_SENDER'] = 'nssli2@yahoo.fr'

mail = Mail(app)

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        # Check if the email exists in the database
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            # Generate a temporary password
            temporary_password = 'new_temporary_password'

            # Update the user's password in the database
            hashed_temp_password = generate_password_hash(temporary_password)
            update_query = "UPDATE users SET password_hash = %s WHERE email = %s"
            cursor.execute(update_query, (hashed_temp_password, email))
            conn.commit()

            # Send the temporary password to the user's email
            send_password_reset_email(email, temporary_password)

            flash('Password reset successful. Check your email for the temporary password.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Email not found. Please enter a valid email address.', 'error')

    return render_template('forgot_password.html')

def send_password_reset_email(email, temporary_password):
    subject = 'Password Reset'
    body = f'Your temporary password is: {temporary_password}'
    message = Message(subject, recipients=[email], body=body)
    mail.send(message)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    
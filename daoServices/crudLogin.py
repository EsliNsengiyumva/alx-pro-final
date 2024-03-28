from dbConnection.connection import DbConnect
from sqlalchemy.exc import SQLAlchemyError
from model.user import User

class CrudLoginOperation:
    def check_credentials(self, email, password):
        try:
            # MySQL configuration
            mysql_config = {
                'host': 'localhost',
                'user': 'sqluser',
                'password': 'password',
                'database': 'smartpermit'
            }
            
            # Establish database connection
            db = DbConnect(mysql_config)
            session = db.establish_connection()
 
            # Query the database for the user with the provided email and password
            user = session.query(User).filter(User.email_id == email, User.password == password).first()
 
            # Close the session
            session.close()
 
            # Return True if user exists, False otherwise
            return user is not None
        except Exception as e:
            print(f"Error: {e}")
            return False

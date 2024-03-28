from dbConnection.connection import DbConnect
from model.user import *
from sqlalchemy.exc import SQLAlchemyError
from model.user import User

class CrudUserOperation:
                

    def create_user(self, first_name, last_name, national_id, teleph_number, 
                        email_id, password, confirm_password):
            try:
                session = self.db.get_session()
                new_user = User(first_name=first_name, last_name=last_name, national_id=national_id,
                                teleph_number=teleph_number, email_id=email_id, password=password,
                                confirm_password=confirm_password)
                session.add(new_user)
                session.commit()
                session.close()
                print("User created successfully!")
            except Exception as e:
                print(f"Error creating user: {e}")


    def read_all_users(self):
        try:
            session = self.db.get_session()
            users = session.query(User).all()
            session.close()
            return users
        except Exception as e:
            print(f"Error reading all users: {e}")
            return None


    def update_user(self, user_id, updated_data):
        try:
            session = self.db.get_session()
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                for key, value in updated_data.items():
                    setattr(user, key, value)
                session.commit()
                print(f"User with ID {user_id} updated successfully.")
            else:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error updating user: {e}")
        finally:
            session.close()


    def delete_user(self, user_id):
        try:
            session = self.db.get_session()
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                print(f"User with ID {user_id} deleted successfully.")
            else:
                print(f"User with ID {user_id} not found.")
        except Exception as e:
            print(f"Error deleting user: {e}")
        finally:
            session.close()


    def check_credentials(self, email, password):
        session = self.db.get_session()
        

        try:
            # Query the database for the user with the provided email
            user = session.query(User).filter(User.email_id == email).first()
            
            # Check if a user with the provided email exists
            if user:
                # Compare the provided password with the password stored in the database
                if user.password == password:
                    return True  # Credentials are valid
                else:
                    return False  # Incorrect password
            else:
                return False  # User with the provided email does not exist
        except SQLAlchemyError as e:
            print(f"Error checking credentials: {e}")
            return False  # Error occurred during database query
        finally:
            session.close()

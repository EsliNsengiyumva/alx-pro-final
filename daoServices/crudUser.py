from dbConnection.connection import DbConnect
from model.user import *


class CrudUserOperation:
    def __init__(self, db_url):
        self.db = DbConnect(db_url)

    def create_user(self, first_name, last_name, national_id, teleph_number, email_id, password, confirm_password):
        session = self.db.get_session()
        new_user = User(first_name=first_name, last_name=last_name, national_id=national_id,
                        teleph_number=teleph_number, email_id=email_id, password=password,
                        confirm_password=confirm_password)
        session.add(new_user)
        session.commit()
        session.close()

    def read_all_users(self):
        session = self.db.get_session()
        users = session.query(User).all()
        session.close()
        return users

    # Implement update and delete operations similarly
    def update_user(self, user_id, updated_data):
        session = self.db.get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)
            session.commit()
        else:
            print(f"User with ID {user_id} not found.")
        session.close()

    def delete_user(self, user_id):
        session = self.db.get_session()
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
        else:
            print(f"User with ID {user_id} not found.")
        session.close()

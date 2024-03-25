from dbConnection.connection import DbConnect
from model.application import *
from model.entity import *


class CrudApplicationOperation:
    def __init__(self, db_url):
        try:
            self.db = DbConnect(db_url)
        except Exception as e:
            print(f"Error initializing database connection: {e}")


    def create_water_permit_application(self, id_of_app, permit_representative, permit_ownership, intended_activities, state_app, date_app, user_id):
        try:
            session = self.db.get_session()
            new_application = WaterPermitApplication(id_of_app=id_of_app, permit_representative=permit_representative, permit_ownership=permit_ownership, 
                                                    intended_activities=intended_activities, 
                                                    state_app=state_app, date_app=date_app, user_id=user_id)
            session.add(new_application)
            session.commit()
            return new_application
        except Exception as e:
            print(f"Error creating water permit application: {e}")
            return None
        finally:
            session.close()

    
    # Read
    def read_water_permit_application(self, application_id):
        try:
            session = self.db.get_session()
            application = session.query(WaterPermitApplication).filter_by(id=application_id).first()
            return application
        except Exception as e:
            print(f"Error reading water permit application: {e}")
            return None
        finally:
            session.close()


    # Update
    def update_water_permit_application(self, application_id, new_state):
        try:
            session = self.db.get_session()
            application = session.query(WaterPermitApplication).filter_by(id=application_id).first()
            if application:
                application.state_app = new_state
                session.commit()
        except Exception as e:
            print(f"Error updating water permit application: {e}")
        finally:
            session.close()

    # Delete
    def delete_water_permit_application(self, application_id):
        try:
            session = self.db.get_session()
            application = session.query(WaterPermitApplication).filter_by(id=application_id).first()
            if application:
                session.delete(application)
                session.commit()
        except Exception as e:
            print(f"Error deleting water permit application: {e}")
        finally:
            session.close()

            
            
    def create_file_storage(session, id_file, file_type, file_name, file_upload, water_permit_application_id):
        try:
            new_file_storage = FileStorage(id_file=id_file, file_type=file_type, file_name=file_name, file_upload=file_upload, water_permit_application_id=water_permit_application_id)
            session.add(new_file_storage)
            session.commit()
        except Exception as e:
            print(f"Error creating file storage: {e}")
        finally:
            session.close()

        
    def get_all_file_storages(session):
        try:
            return session.query(FileStorage).all()
        except Exception as e:
            print(f"Error fetching all file storages: {e}")
        finally:
            session.close()

    
    def update_file_storage(session, file_storage_id, new_id_file, new_file_type, new_file_name, new_file_upload, new_water_permit_application_id):
        try:
            file_storage = session.query(FileStorage).filter_by(id=file_storage_id).first()
            if file_storage:
                file_storage.id_file = new_id_file
                file_storage.file_type = new_file_type
                file_storage.file_name = new_file_name
                file_storage.file_upload = new_file_upload
                file_storage.water_permit_application_id = new_water_permit_application_id
                session.commit()
        except Exception as e:
            print(f"Error updating file storage: {e}")
        finally:
            session.close()

    def delete_file_storage(session, file_storage_id):
        try:
            file_storage = session.query(FileStorage).filter_by(id=file_storage_id).first()
            if file_storage:
                session.delete(file_storage)
                session.commit()
        except Exception as e:
            print(f"Error deleting file storage: {e}")
        finally:
            session.close()


    def create_water_permit_payment(session, payment_id, payment_amount, payment_paid, payment_detail, payment_date, water_permit_application_id):
        try:
            new_payment = WaterPermitPayment(payment_id=payment_id, payment_amount=payment_amount, payment_paid=payment_paid,
                                            payment_detail=payment_detail, payment_date=payment_date, water_permit_application_id=water_permit_application_id)
            session.add(new_payment)
            session.commit()
        except Exception as e:
            print(f"Error creating water permit payment: {e}")
        finally:
            session.close()


    def get_all_water_permit_payments(session):
        try:
            return session.query(WaterPermitPayment).all()
        except Exception as e:
            print(f"Error retrieving water permit payments: {e}")
            return None
        finally:
            session.close()


    def update_water_permit_payment(session, payment_id, new_payment_amount, new_payment_paid, new_payment_detail, new_payment_date, new_water_permit_application_id):
        try:
            payment = session.query(WaterPermitPayment).filter_by(payment_id=payment_id).first()
            if payment:
                payment.payment_amount = new_payment_amount
                payment.payment_paid = new_payment_paid
                payment.payment_detail = new_payment_detail
                payment.payment_date = new_payment_date
                payment.water_permit_application_id = new_water_permit_application_id
                session.commit()
        except Exception as e:
            print(f"Error updating water permit payment: {e}")
            session.rollback()
        finally:
            session.close()

            
    def delete_water_permit_payment(session, payment_id):
        try:
            payment = session.query(WaterPermitPayment).filter_by(payment_id=payment_id).first()
            if payment:
                session.delete(payment)
                session.commit()
        except Exception as e:
            print(f"Error deleting water permit payment: {e}")
            session.rollback()
        finally:
            session.close()

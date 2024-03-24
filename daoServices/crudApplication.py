from dbConnection.connection import DbConnect
from model.application import *
from model.entity import *


class CrudApplicationOperation:
    def __init__(self, db_url):
        self.db = DbConnect(db_url)

    # Create
    def create_water_permit_application(self,id_of_app, permit_representative, permit_ownership, intended_activities, state_app, date_app, user_id):
        session = self.db.get_session()
        new_application = WaterPermitApplication(id_of_app=id_of_app, permit_representative=permit_representative, permit_ownership=permit_ownership, intended_activities=intended_activities, 
                                                state_app=state_app, date_app=date_app, user_id=user_id)
        session.add(new_application)
        session.commit()
        return new_application
    
    # Read
        def read_water_permit_application(self, application_id):
            session = self.db.get_session()
            return session.query(WaterPermitApplication).filter_by(id=application_id).first()

        # Update
        def update_water_permit_application(self, application_id, new_state):
            session = self.db.get_session()
            application = session.query(WaterPermitApplication).filter_by(id=application_id).first()
            if application:
                application.state_app = new_state
                session.commit()

        # Delete
        def delete_water_permit_application(self,application_id):
            session=self.db.get_session()
            application = session.query(WaterPermitApplication).filter_by(id=application_id).first()
            if application:
                session.delete(application)
                session.commit()

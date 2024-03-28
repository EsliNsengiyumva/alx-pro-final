from flask import Flask, request, render_template
from model.application import *
from model.entity import *
from dbConnection.connection import DbConnect
from daoServices.crudUser import CrudUserOperation
from daoServices.crudApplication import *

#from your_module import WaterPermitApplication, WaterSourceCategory, WaterPermitLocation, WaterPermitPayment, FileStorage, StateAppEnum

app = Flask(__name__)
db = DbConnect()
engine = create_engine(db.establish_connection())
Session = sessionmaker(bind=engine)
session = Session()
crud = CrudUserOperation(session)

@app.route('/')
def index():
    return render_template('application.html')



@app.route('/application', methods=['POST'])
def create_water_permit_application():
    id_of_app = request.form['id_of_app']
    full_Name = request.form['fullName']
    applicant_category = request.form['category']
    applicant_type = request.form['applicantType']
    national_id = request.form['identity']
    teleph_number = request.form['telephoneContact']
    email_id = request.form['emailAddress']
    date_app = request.form['applicationDate']
    user_id = request.form['user_id']
    water_source_type = request.form['sourceType']
    water_source_name = request.form['sourceofwater']
    water_land_use_owner = request.form.get('landOwnership') == 'Yes'  # Assuming landOwnership is a checkbox
    water_intended_activities = request.form.getlist('intendedActivity')  # Assuming intendedActivity is a multi-select
    province = request.form['province']
    district = request.form['district']
    sector = request.form['sector']
    cell = request.form['cell']
    village = request.form['village']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    payment_amount = request.form['paymentAmount']
    payment_type = request.form['paymentType']
    file_name = request.form['documentName']
    file_upload = request.files['documentUpload']  # Assuming it's a file upload field

    # Now, call the method to save the data to the database
    # Make sure you have imported the necessary modules and defined the methods correctly
    # For brevity, I'm assuming you have a `db` object that handles the database connection
    # and `create_water_permit_application` method in the `db` object

    result = crud.create_water_permit_application(id_of_app, full_Name, applicant_category, applicant_type, national_id,
                                                teleph_number, email_id, date_app, user_id, water_source_type,
                                                water_source_name, water_land_use_owner, water_intended_activities,
                                                province, district, sector, cell, village, latitude, longitude,
                                                payment_amount, payment_type, file_name, file_upload)
    
    if result:
        return "Water Permit Created Successfully"
    else:
        return "Failed to create Water Permit"

if __name__ == '__main__':
    app.run(debug=True)

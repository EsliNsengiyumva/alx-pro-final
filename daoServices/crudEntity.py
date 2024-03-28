from dbConnection.connection import DbConnect
from model.entity import *


class CrudEntityOperation:
    
    def __init__(self, db_url):
        try:
            self.db = DbConnect(db_url)
            print("Database connection established successfully.")
        except Exception as e:
            print(f"Error establishing database connection: {str(e)}")

    
    def create_entity(session, entity_name, tin_number):
        try:
            new_entity = Entity(entity_name=entity_name, tin_number=tin_number)
            session.add(new_entity)
            session.commit()
            print("Entity has been Save successfully !")
        except Exception as e:
             print(f"Error entity not saved: {str(e)}")

    def get_all_entities(session):
        try:
            return session.query(Entity).all()
        except Exception as e:
            print(f"Error: Unable to retrieve entities - {str(e)}")
            return []

     
    def update_entity(session, entity_id, new_entity_name, new_tin_number):
        try:
            entity = session.query(Entity).filter_by(id_entity=entity_id).first()
            if entity:
                entity.entity_name = new_entity_name
                entity.tin_number = new_tin_number
                session.commit()
                print("Entity updated successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error updating entity: {str(e)}")

        
    def delete_entity(session, entity_id):
        try:
            entity = session.query(Entity).filter_by(id_entity=entity_id).first()
            if entity:
                session.delete(entity)
                session.commit()
                print("Entity deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error deleting entity: {str(e)}")

    
    def create_category(session, category_name, entity_id):
        try:
            new_category = Category(category_name=category_name, entity_id=entity_id)
            session.add(new_category)
            session.commit()
            print("Category created successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error creating category: {str(e)}")

    def get_all_categories(session):
        try:
            return session.query(Category).all()
        except Exception as e:
            print(f"Error retrieving categories: {str(e)}")
            return []

    
    def update_category(session, category_id, new_category_name, new_entity_id):
        try:
            category = session.query(Category).filter_by(id_category=category_id).first()
            if category:
                category.category_name = new_category_name
                category.entity_id = new_entity_id
                session.commit()
                print("Category updated successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error updating category: {str(e)}")


    def delete_category(session, category_id):
        try:
            category = session.query(Category).filter_by(id_category=category_id).first()
            if category:
                session.delete(category)
                session.commit()
                print("Category deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error deleting category: {str(e)}")

            
    def create_water_category(session, category_name, entity_id, type_of_water, use_of_water, source_of_water):
        try:
            new_water_category = WaterSourceCategory(category_name=category_name, entity_id=entity_id, type_of_water=type_of_water, use_of_water=use_of_water, source_of_water=source_of_water)
            session.add(new_water_category)
            session.commit()
            print("Water category created successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error creating water category: {str(e)}")


    def get_all_water_categories(session):
        try:
            return session.query(WaterSourceCategory).all()
        except Exception as e:
            print(f"Error retrieving water categories: {str(e)}")
            return []

    
    def update_water_category(session, water_category_id, new_category_name, new_entity_id, new_type_of_water, new_use_of_water, new_source_of_water):
        try:
            water_category = session.query(WaterSourceCategory).filter_by(id_water_category=water_category_id).first()
            if water_category:
                water_category.category_name = new_category_name
                water_category.entity_id = new_entity_id
                water_category.type_of_water = new_type_of_water
                water_category.use_of_water = new_use_of_water
                water_category.source_of_water = new_source_of_water
                session.commit()
                print("Water category updated successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error updating water category: {str(e)}")

            
    def delete_water_category(session, water_category_id):
        try:
            water_category = session.query(WaterSourceCategory).filter_by(id_water_category=water_category_id).first()
            if water_category:
                session.delete(water_category)
                session.commit()
                print("Water category deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"Error deleting water category: {str(e)}")


    def create_water_location(session, province, district, sector, cell, village, street, latitude, longitude, water_category_id):
        try:
            new_water_location = WaterPermitLocation(province=province, district=district, sector=sector, cell=cell,
                                            village=village, street=street, latitude=latitude, longitude=longitude,
                                            water_category_id=water_category_id)
            session.add(new_water_location)
            session.commit()
            print("Water location created successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error creating water location: {str(e)}")
            
    def get_all_water_locations(session):
        try:
            return session.query(WaterPermitLocation).all()
        except Exception as e:
            print(f"Error retrieving water locations: {str(e)}")
            return []
    
    def update_water_location(session, location_id, new_province, new_district, new_sector, new_cell, new_village, new_street, new_latitude, new_longitude, new_water_category_id):
        try:
            water_location = session.query(WaterPermitLocation).filter_by(id_location=location_id).first()
            if water_location:
                water_location.province = new_province
                water_location.district = new_district
                water_location.sector = new_sector
                water_location.cell = new_cell
                water_location.village = new_village
                water_location.street = new_street
                water_location.latitude = new_latitude
                water_location.longitude = new_longitude
                water_location.water_category_id = new_water_category_id
                session.commit()
                print("Water location updated successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error updating water location: {str(e)}")













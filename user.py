class User:
    def __init__(self, firstname, lastname, nationalId, teleph,emailid, password, confirmpsw):
        self.firstname = firstname
        self.lastname = lastname
        self.nationalId = nationalId
        self.teleph = teleph
        self.emailid=emailid
        self.password = password
        self.confirmpsw = confirmpsw

class Password:
    def __init__(self):
        self.users = []
    
    def add_user(self, firstname, lastname, nationalId, teleph, emailid, password, confirmpsw):
        user = User(firstname, lastname, nationalId, teleph,emailid, password, confirmpsw)
        self.users.append(user)
    
    def display_user(self):
        for user in self.users:
            print(f"First Name: {user.firstname}")
            print(f"Last Name: {user.lastname}")
            print(f"National Id: {user.nationalId}")
            print(f"Telephone: {user.teleph}")
            print(f"Email id:{user.emailid}")
            print(f"Password: {user.password}")
            print(f"Confirm Password: {user.confirmpsw}")
            print("......................................")

Pass = Password()

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
nationalId = input("Enter id: ")
teleph = input("Enter telephone: ")
emailid=input("emailid:")
password = input("Enter password: ")
confirmpsw = input("Confirm password: ")

Pass.add_user(firstname, lastname, nationalId, teleph, emailid,password, confirmpsw)
Pass.display_user()
Pass.add_user(firstname, lastname, nationalId, teleph,emailid, password, confirmpsw)
Pass.display_user()
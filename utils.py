import json_utils

# App administration
def create_user(name, phone_number, email):
    # New user in the app
    # Users are ID'd by phone number

    user_data = json_utils.load_data()

    for user, data in user_data.items():
        if user == phone_number:
            error = 'User (%s) already exists' % user
            return error
    

    user_data[phone_number] = {
        'name': name,
        'email': email
    }

    json_utils.save_data(user_data)
    return user_data

def create_customer(name, phone_number, email):
    # Square customer creation
    customer_data = {}
    return customer_data

def list_customers():
    # List square customers
    return


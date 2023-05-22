import json_utils

# App administration
def create_user(name, phone_number, email):
    # New user in the app
    # Users are ID'd by phone number

    existing_user_data = json_utils.load_data()

    for user, data in existing_user_data.items():
        if user == phone_number:
            error = 'User (%s) already exists' % user
            return error
    
    new_user_record = {}
    new_user_record[phone_number] = {
        'name': name,
        'email': email
    }

    new_user_data = existing_user_data.append(new_user_record)

    json_utils.save_data(new_user_data)
    return new_user_data

def create_customer(name, phone_number, email):
    # Square customer creation
    customer_data = {}
    return customer_data

def list_customers():
    # List square customers
    return


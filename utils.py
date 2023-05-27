import utils_json

# App administration
def create_user(name, phone_number, email):
    # New user in the app
    # Users are ID'd by phone number

    user_data = get_users()

    for user, data in user_data.items():
        if user == phone_number:
            error = 'User (%s) already exists' % user
            return error
    

    user_data[phone_number] = {
        'name': name,
        'email': email
    }

    utils_json.save_data(user_data)
    return user_data

def get_users():
    try:
        user_data = utils_json.load_data()
        return user_data
    except:
        return "Error in fetching user data"


def create_customer(name, phone_number, email):
    # Square customer creation
    customer_data = {}
    return customer_data

def list_customers():
    # List square customers
    return

def incoming_processor(data):
    incoming_body = data['Body']
    incoming_from = data['From']

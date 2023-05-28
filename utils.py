import utils_json
import utils_twilio
import re

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
        'email': email,
        'incoming_history': {}
    }

    utils_json.save_data(user_data)
    return user_data

def get_users():
    try:
        user_data = utils_json.load_data()
        return user_data
    except:
        return "Error in fetching user data"

def phone_num_formatter(phone_num):
    phone_num = re.sub("[^0-9]", "", phone_num)
    phone_num = '+' + str(phone_num)
    return phone_num

def incoming_processor(data):
    incoming_text = data['Body'].lower()
    user = phone_num_formatter(data['From'])
    utils_json.add_user_incoming_history(data)
    
    # Structure for the incoming command:
    # <command> <square_object> <arguments>
    # <command> = add, list, show, etc
    # <square_object> = customer, subscription, etc
    
    commands = ['add', 'list', 'show', 'assist', 'hello']
    square_objects = ['customer', 'subscription']

    # Break out incoming text into the supposed parts
    incoming_text_list = incoming_text.split(' ')
    command = incoming_text_list[0].lower()

    if command in commands:
        available_commands = ', '.join(commands)
        available_objs = ', '.join(square_objects)
        # Logic to parse the first part of the incoming text (ie the command)
        if 'hello' in command:
            response = 'Hello! This is your Square SMS Assistant.\n\nReply "assist" at any time to see how I can help you today.'
        elif 'assist' in command:
            response = 'Available commands:\n- %s\n\nYou may use the above commands paired with the below Square merchant information:\n%s\nExample:\n List customers' % (available_commands, available_objs)
        else:
            response = "Sorry, I don't understand what you mean."
    else:
        response = 'Sorry, I do not know the command "%s"' % command

    # Based on the command, determine what kind of API call will be made

    # Send response
    utils_twilio.send_sms(user, response)
    return response
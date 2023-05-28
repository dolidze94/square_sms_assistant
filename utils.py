import utils_json
import utils_twilio
import re
import command_matrix
import sys

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
    # <action> <square_object> <arguments>
    # <action> = add, list, show, etc
    # <square_object> = customer, subscription, etc
    
    actions = command_matrix.actions
    square_objects_dict = command_matrix.square_objects_dict

    # Break out incoming text into the supposed parts
    incoming_text_list = incoming_text.split(' ')
    incoming_action = incoming_text_list[0].lower()
    incoming_obj = incoming_text_list[1].lower()


    if incoming_action in actions:
        print('>>> Incoming action:\n%s' % incoming_action, file=sys.stderr)
        available_actions = ', '.join(actions)
        available_objs = ', '.join(square_objects_dict.keys())
        # Logic to parse the first part of the incoming text (ie the command)
        if 'hello' in incoming_action:
            response = 'Hello! This is your Square SMS Assistant.\n\nReply "assist" at any time to see how I can help you today.'
        elif 'assist' in incoming_action:
            response = "Available functions:\n- %s\n\nSpecify which information you'd like to see:\n- %s\n\nExample: 'List customers'" % (available_actions, available_objs)
        elif incoming_obj in square_objects_dict.keys():
            try:
                square_command = square_objects_dict[incoming_obj]['actions'][incoming_action]
                result = eval(square_command)
            except Exception as e:
                response = "That action is unavailable. Error:\n", e
        else:
            response = "Sorry, I don't understand what you mean."
    else:
        response = 'Sorry, I do not know the command "%s"' % incoming_action

    # Based on the command, determine what kind of API call will be made

    # Send response
    utils_twilio.send_sms(user, response)
    return response
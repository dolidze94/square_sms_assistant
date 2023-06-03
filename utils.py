import utils_json
import utils_twilio
import re
import command_matrix
import sys
import utils_square

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
    for i in range(len(incoming_text_list)):
        if i == 0:
            incoming_action = incoming_text_list[i].lower()
        if i==1:
            incoming_obj = incoming_text_list[i].lower()


    if incoming_action in actions:
        print('>>> Incoming action:\n%s' % incoming_action, file=sys.stderr)
        available_actions = ', '.join(actions)
        available_objs = ', '.join(square_objects_dict.keys())
        # Logic to parse the first part of the incoming text (ie the command)
        if 'hello' in incoming_action:
            response = 'Hello! This is your Square SMS Assistant.\n\nReply "assist" at any time to see how I can help you today.'
        elif 'assist' in incoming_action:
            response = 'Available functions (Prototype Mode):\n> List and add customers/employees\nFor example, "list employees"\nTo add a record, type add <employee/customer> <first name> <last name> <phone number> <email>\nie.: Add employee James Jameston +14155552671 james@ceo.com'
        elif 'add' in incoming_action:
            if 'customer' in incoming_obj or 'employee' in incoming_obj:
                # add customer Luke Sky +15555555555 luke@sky.com'
                first_name = incoming_text_list[2]
                last_name = incoming_text_list[3]
                full_name = first_name+' '+last_name
                phone_number = incoming_text_list[4]
                email = incoming_text_list[5]
                type = incoming_obj
                new_person = utils_square.create_person(type, full_name, phone_number, email)
                print('new_person:\n'+str(new_person), file=sys.stderr)
                if new_person:
                    new_record_name = ''
                    for record_type, record in new_person.body.items():
                        if 'customer' in type:
                            new_record_name = record['given_name']
                        if 'employee' in type:
                            new_record_name = record['given_name']
                        type = record_type
                    response = 'Record for %s (%s) has been created' % (new_record_name.replace('_', ' '), type)
                else:
                    response = 'Record creation did not succeed'
        elif 'list' in incoming_action:
            if 'customer' in incoming_obj:
                response = utils_square.list_customers()
            elif 'employee' in incoming_obj:
                response = utils_square.list_employees()
            else:
                response = 'Unable to find object "%s"' % incoming_obj
        #elif incoming_obj in square_objects_dict.keys():
            #try:
                #square_command = exec(square_objects_dict[incoming_obj]['actions'][incoming_action])
                #response = square_command
                #print('>>> Response:\n%s' % response, file=sys.stderr)
            #except Exception as e:
                #response = "That action is unavailable. Error:\n", str(e)
        else:
            response = "Sorry, I don't understand what you mean."
    else:
        response = 'Sorry, I do not know the command "%s"' % incoming_action

    # Based on the command, determine what kind of API call will be made

    # Send response
    utils_twilio.send_sms(user, response)
    return response
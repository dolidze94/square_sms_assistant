import json
import sys

database_file = 'database.json'

def load_data(file_path = database_file):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(data, file_path = database_file):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def user_exists(incoming):
    database = load_data()
    print('database after retrieving: %s' % database, file=sys.stderr)
    for cust_id, cust_data in database.items():
        if incoming['From'] == cust_id:
            return True
    return False

def add_user_incoming_history(incoming):
    print('add_user_incoming_history executed', file=sys.stderr)
    if user_exists(incoming):
        indexed_history_dict = {}
        incoming_user = incoming['From']
        database = load_data()
        if not cust_data["incoming_history"]:
            cust_data["incoming_history"] = []
        for cust_id, cust_data in database.items():
            if incoming_user == cust_id:
                entry_tuple = (len(cust_data["incoming_history"]), str(incoming)) # Indexed tuple
                cust_data["incoming_history"].append(entry_tuple)
        save_data(database)
        return True
    else:
        return "This user does not exist in the records"

import json

database_file = 'database.json'

def load_data(file_path = database_file):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(data, file_path = database_file):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def get_all_records(data):
    return data

def get_record_by_id(data, record_id):
    for record in data:
        if record['id'] == record_id:
            return record
    return None

def add_record(data, new_record):
    data.append(new_record)

def update_record(data, record_id, updated_record):
    for i, record in enumerate(data):
        if record['id'] == record_id:
            data[i] = updated_record
            break

def delete_record(data, record_id):
    for i, record in enumerate(data):
        if record['id'] == record_id:
            del data[i]
            break

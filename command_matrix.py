import utils_square

actions = ['add', 'show', 'list', 'assist', 'hello']

square_objects = ['customer', 'subscription']

# Helper variables
customer_list = utils_square.list_customers()
customer_add = ''
emp_list = ''
subs_add = ''

# Example: result = client.customers.list_customers()
square_objects_dict = {
    "customer": {
        "actions": {
            "add": "",
            "assist": "",
            "list": customer_list,
            "show": "",
        },
        "subclass": "customers",
    },
    "employees": {
        "actions": {"add": "", "assist": "", "show": "", "list": emp_list},
        "subclass": "subscriptions",
    },
}




# For personal utility - regenerates square_objects_dict if I ever enter new actions/objects

def object_normalizer(square_objects, square_objects_dict):
    for obj in square_objects:
        square_objects_dict.setdefault(obj, {})
        for action in actions:
            if action != 'hello':
                square_objects_dict[obj].setdefault('actions', {})
                square_objects_dict[obj].setdefault('subclass', '')
                square_objects_dict[obj]['actions'].setdefault(action, '')
    return square_objects_dict

#square_objects_dict = object_normalizer(square_objects, square_objects_dict)
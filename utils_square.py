from square.client import Client
import configs

client = Client(access_token=configs.square_access_token, environment='sandbox')

def list_customers():
    try:
        result = client.customers.list_customers(limit = 10, sort_field = "CREATED_AT", sort_order = "DESC")
        cust_list = 'Customers not found'
        if result.body['customers']:
            cust_list = 'Your customers:\n\n'
            for cust in result.body['customers']:
                cust_list += 'Name: %s\nPhone number: %s\n\n' % (cust['given_name'], cust['phone_number'])
        return cust_list
    except Exception as e:
        return "Error while trying to retrieve customer data: " + str(e)

def list_employees():
    try:
        result = client.team.search_team_members()
        return result
    except Exception as e:
        return "Error while trying to retrieve employee data: " + str(e)

def create_person(type, name, phone_number, email):
    # Square customer creation
    body = {
        "given_name": name,
        "phone_number": phone_number,
        "email": email
    }
    if 'customer' in type:
        result = client.customers.create_customer(body=body)
    if 'employee' in type:
        result = client.team.create_team_member(body={"team_member": body})
    return result


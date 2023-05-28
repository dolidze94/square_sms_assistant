from square.client import Client
import configs

client = Client(access_token=configs.square_access_token, environment='sandbox')

def list_customers():
    try:
        result = client.customers.list_customers(limit = 2, sort_field = "CREATED_AT", sort_order = "DESC")
        cust_list = 'Customers not found'
        if result.body['customers']:
            #cust_list = 'Your customers:\n\n'
            cust_list = 'hello:\n\n'
            for cust in result.body['customers']:
                #cust_list += 'Name: %s\nPhone number: %s\n\n' % (cust['given_name'], cust['phone_number'])
                cust_list += 'Name: Jane Doe'
        return cust_list
    except Exception as e:
        return "Error while trying to retrieve customer data: " + str(e)

def list_employees():
    try:
        result = client.team.search_team_members()
        return result
    except Exception as e:
        return "Error while trying to retrieve employee data: " + str(e)

def create_customer(name, phone_number, email):
    # Square customer creation
    result = client.customers.create_customer(
    body = {
        "given_name": name,
        "phone_number": phone_number,
        "email": email
    }
)


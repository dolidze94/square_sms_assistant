import configs
import sys
from square.client import Client

client = Client(access_token=configs.square_access_token, environment='sandbox')

#client = Client(access_token=configs.square_access_token, environment='sandbox')

def list_customers():
    try:
        result = client.customers.list_customers(limit = 10, sort_field = "CREATED_AT", sort_order = "DESC")
        cust_list = 'Customers not found'
        if result.body['customers']:
            cust_list = 'Here are your most recent customers:\n\n'
            for cust in result.body['customers']:
                cust_list += 'Name: %s\nPhone number: %s\n\n' % (cust['given_name'], cust['phone_number'])
        return cust_list
    except Exception as e:
        return "Error while trying to retrieve customer data: " + str(e)

def list_employees():
    body = {}
    try:
        result = client.team.search_team_members(body=body)
        emp_list = 'Customers not found'
        if result.body['team_members']:
            emp_list = 'Here are your employees:\n\n'
            for emp in result.body['team_members']:
                if not emp['is_owner']:
                    emp_list += 'Name: %s\nPhone number: %s\n\n' % (emp['given_name'], emp['phone_number'])
        return emp_list
    except Exception as e:
        print("Error while trying to retrieve employee data: " + str(e), file=sys.stderr)
        return False

def create_person(type, name, phone_number, email):
    # Square customer creation
    try:
        body = {
            "given_name": name,
            "phone_number": phone_number,
            "email_address": email
        }
        if 'customer' in type:
            result = client.customers.create_customer(body=body)
        if 'employee' in type:
            body['family_name'] = name
            result = client.team.create_team_member(body={"team_member": body})
        print('>>> Result from create_person:\n'+str(result.body), file=sys.stderr)
        return result
    except Exception as e:
        print("Error when trying to create person:\n", str(e))
        return False


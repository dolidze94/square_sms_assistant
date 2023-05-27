from square.client import Client
import configs

client = Client(access_token=configs.square_access_token, environment='sandbox')

def list_customers():
    try:
        result = client.customers.list_customers()
        return result
    except Exception as e:
        return "Error while trying to retrieve customer data: " + e
    
def add_customer():
    customer = []
    return customer
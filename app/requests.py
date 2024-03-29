import urllib.request,json
from .models import Quote

base_url = None
api_key =None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_BASE_URL']
    

def get_random_quote():
    '''
    Function that gets the response to our url request
    '''
    
    with urllib.request.urlopen(base_url) as url:
        
        quote_data = url.read()
        quote_response = json.loads(quote_data)
        print(quote_data)
        
    return quote_response
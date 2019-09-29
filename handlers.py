import api_urls
import requests as request
'''
# api-endpoint 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json()
'''

#Search query and returns list of json strings
#search_api_link="https://www.jiosaavn.com/api.php?_format=json&__call=autocomplete.get&query=coldplay"
def search_query(query):
    PARAMS = {
        '_format': 'json',
        '__call': 'autocomplete.get',
        'query' : query
        }

    response = request.get(url = api_urls.search_link, params = PARAMS, headers = {
        "content-type" : "text", 
        "User-Agent" :"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0" 
    })
    response.encoding = 'utf-8'
    data = response.text
    index = data.find('{')
    return data[index - 1 : len(data)]
    

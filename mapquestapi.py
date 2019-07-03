#Kan Dang 54515091 Lab Section 4. Safir

import json
import urllib.parse
import urllib.request

MAPQUEST_API = 'NHJ7XEUY2oRGI9boTGmjo7vsVIhDTMDx'
MAPQUEST_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'
BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2/'

def build_url(locations: list) -> str:
    '''This function builds the url by taking the search query as an input'''

    query = [ ('key', MAPQUEST_API), ('from', locations[0])]
    for i in range(len(locations)-1):
        query.append(('to', locations[i+1]))
        

    return BASE_MAPQUEST_URL + 'route?' + urllib.parse.urlencode(query)

def build_elevation_url(elevations: list) -> str:
    '''Builds the API url for Elevations using the search query '''
    elevation = ''
    for item in elevations:
        elevation = elevation + str(item) + ','
    elevation = elevation[0:-1]
        
    query = [ ('key', MAPQUEST_API) ]
    
    return MAPQUEST_ELEVATION_URL + urllib.parse.urlencode(query) + '&latLngCollection=' + elevation

def get_elevations(json_result: 'json') -> None:
    '''Uses the JSON response from Mapquest API and prints directions'''

    for item in json_result['elevationProfile']:
        print(item['height'])


def get_directions(url: str) -> 'json':
    '''Takes a URL and returns Python object representing the JSON response'''

    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)

    finally:
        if response != None:
            response.close()

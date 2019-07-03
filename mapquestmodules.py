#Kan Dang 54515091 Lab Section 4. Safir

from math import ceil
import mapquestapi as mpa

class LatLongMQ:
    '''Class for the Latitude and Longitude'''
    def __init__(self):
        pass
    
    def printMQ(self, j) -> None:
        '''Prints the output of latitude and longitude'''
        result = []
        result2 = []
        print('LATLONGS')
        for item in j['route']['locations']:
            lat = item['displayLatLng']['lat']
            lng = item['displayLatLng']['lng']
            if lat > 0:
                latdir = 'N '
            else:
                latdir = 'S '
            if lng > 0:
                lngdir = 'E '
            else:
                lngdir = 'W '
            result2.append(lat)
            result2.append(lng)
                
            print(("{:.2f}" + latdir + "{:.2f}" + lngdir).format(abs(lat), abs(lng)))       

class StepsMQ:
    '''Class for the steps from location to location'''
    def __init__(self):
        pass
    
    def printMQ(self, j) -> None:
        '''Prints the output of the steps, one per line'''
        print('DIRECTIONS')
        for item in j['route']['legs']:
            for item in item['maneuvers']:
                print(item['narrative'])
 

class TotalTimeMQ:
    '''Class for the total time of the trip'''
    def __init__(self):
        pass
    
    def printMQ(self, j) -> None:
        'Prints the output of the total time'''
        a = j
        b = a['route']['time']
        print('TOTAL TIME:', round(int(b)/60), 'minutes')

class TotalDistanceMQ:
    '''Class for the total distance of the trip'''
    def __init__(self):
        pass
    
    def printMQ(self, j) -> None:
        '''Prints the output of the total distance of the trip'''
        print('TOTAL DISTANCE:', round(j['route']['distance']), 'miles')

class ElevationMQ:
    '''Class for the Elevations'''
    def __init__(self):
        pass
            
    def printMQ(self, j) -> None:
        '''Prints the output of the elevations, one per line
        Uses the list from getlatlong and builds url with list'''
        result = []
        a = self.getlatlong(j)
        for i in range(0, len(a), 2):
            result.append([str(a[i]), str(a[i+1])])

        result2 = []
        for item in result:
            thing = mpa.get_directions(mpa.build_elevation_url((item)))
            for element in thing['elevationProfile']:
                result2.append(element['height'])
        print('ELEVATIONS')
        for item in result2:
            print(round(int(item) * 3.28084))

    def getlatlong(self, j) -> list:
        '''Gets the longitudes and latitudes to get the elevations'''
        result2 = []
        for item in j['route']['locations']:
            lat = item['displayLatLng']['lat']
            lng = item['displayLatLng']['lng']
            result2.append(lat)
            result2.append(lng)
        return result2
        

def run_mapquest(mqs: ['MQs'], starting_value) -> None:
    '''Runs each function to print the output using json'''
    result = []
    print()
    for item in mqs:
        result.append(item.printMQ(starting_value))
        print()


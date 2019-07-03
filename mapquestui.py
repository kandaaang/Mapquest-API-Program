#Kan Dang 54515091 Lab Section 4. Safir

import mapquestapi as mpa
import mapquestmodules as mpm

def add_functions(a: list) -> list:
    '''Based on user input, adds which functions to perform and returns as list'''
    result = []
    for item in a:
        if item == 'STEPS':
            result.append(mpm.StepsMQ())
        elif item == 'TOTALTIME':
            result.append(mpm.TotalTimeMQ())
        elif item == 'TOTALDISTANCE':
            result.append(mpm.TotalDistanceMQ())
        elif item == 'LATLONG':
            result.append(mpm.LatLongMQ() )
        elif item == 'ELEVATION':
            result.append(mpm.ElevationMQ())
    return result
            

def run_program() -> None:
    '''Runs the program and follows procedure for user input'''
    lineone = int(input(''))
    result = []
    for i in range(lineone):
        result.append(input(''))
    linetwo = int(input(''))
    result2 = []
    for j in range(linetwo):
        result2.append(input(''))

    total = add_functions(result2)
    try:
        checkerror = mpa.get_directions(mpa.build_url(result))
    except:
        print()
        print('MAPQUEST ERROR')
    else:
        if checkerror['info']['statuscode'] == 0:
            mpm.run_mapquest(total, mpa.get_directions(mpa.build_url(result)))
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        elif checkerror['info']['statuscode'] == 400:
            print()
            print('ROUTE ERROR')
        else:
            try:
                mpm.run_mapquest(total, mpa.get_directions(mpa.build_url(result)))
                print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
            except:
                pass
        

if __name__ == '__main__':
    run_program()

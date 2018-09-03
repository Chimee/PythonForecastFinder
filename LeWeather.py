import sys
import requests
import json
import falcon
import flask
import logging
import re
from datetime import datetime

from apixu.client import ApixuClient

from apixu.client import ApixuException

logging.basicConfig(filename='/Weather API Conflict/logs/applog.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)



#Example Call to OpenWeather API For Current Weather by City ID 
#https://api.openweathermap.org/data/2.5/weather?id=4671654&appid=0c9597524a3f445d77b02ccda4e6b577
#Example Call to OpenWeather API For Current Weather by Zip Code
#https://api.openweathermap.org/data/2.5/weather?zip=78708,us&appid=0c9597524a3f445d77b02ccda4e6b577
#https://api.openweathermap.org/data/2.5/forecast?zip=78708&appid=0c9597524a3f445d77b02ccda4e6b577

#Need to return
#    Location
#    Current Temp For Today
#    Forecasted Temp for tomorrow
#    Current Condition (Cloudy, Windy, Sunny, Rainy...)
#    Forecasted Condition for Tomorrow
#   Sunrise & Sunset




def my_serializer(req, resp, exception): #Send response body as JSON to client when HTTPError Raised
    representation = None

    preferred = req.client_prefers(('application/x-yaml',
                                    'application/json'))

    if preferred is not None:
        if preferred == 'application/json':
            representation = exception.to_json()
        else:
            representation = yaml.dump(exception.to_dict(),
                                       encoding=None)
        resp.body = representation
        resp.content_type = preferred

    resp.append_header('Vary', 'Accept')



class ForecastInput(object):
    def on_get(self, req, resp):
        clientlog = open('/Weather API Conflict/logs/accesslog.txt', "a")
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        
        with open('chisweather.html', 'r') as f:
            resp.body = f.read()


        clientlog.write(str(datetime.now()) + ': Forecast input page accessed by client ' + str(req.access_route) + '\n' + '    USER-AGENT: '
                        + str(req.get_header('USER-AGENT')) + '\n') 
        clientlog.close()
    
        
        
        
		


class GetTheWeather(object):

    
    def on_get(self, req, resp):
        
 

        #Alphabet list to check against client's state entry for proper weather API routing
        clientlog = open('/Weather API Conflict/logs/accesslog.txt', "a")
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
        alphabetlow = [letter.lower() for letter in alphabet] #using .lower method in case client enter state with lowercase letter 
        print(alphabet)
        print(alphabetlow)
        
        
        city = req.get_param('city')
        zipcode = req.get_param('zip')
        state = req.get_param('state')
        print('Client requesting weather information for ' + city + ', ' + state + ' with zipcode of ' + zipcode)
        statebegins = state[0:1]

        
        if (
                re.match("^[A-Za-z ]+$", state) and
                re.match("^[A-Za-z ]+$", city) and
                re.match("^[0-9]+$", zipcode)

            ):

            print('All characters are letters')
            try:

                if (statebegins in alphabet[0:13]): #send client request to openweather API if state begins with A - M
                    clientlog.write(str(datetime.now()) + ': Client requesting weather information for ' + city + ', ' + state + ' with zipcode of ' + zipcode)   
                    print(state + ' weather information must be requested from Open Weather Api')
                    logger.info('Starting Weather forecast request to OpenWeather API')
                    resp.status = falcon.HTTP_200
                    
                    owapikey = "0c9597524a3f445d77b02ccda4e6b577"
                    

                    request_url = "https://api.openweathermap.org/data/2.5/weather"
                    request_param = {'zip': zipcode, 'appid': owapikey}
                    request_header = {}
                  


                    
                    
                    request_response = requests.get(
                        url=request_url,
                        params=request_param, 
                        headers=request_header
                     
                    )
                    request_url2 = "https://api.openweathermap.org/data/2.5/forecast"
                    request_param2 = {'zip': zipcode, 'appid': owapikey}
                    request_header2 = {}
                  


                    
                    
                    request_response2 = requests.get(
                        url=request_url2,
                        params=request_param2, 
                        headers=request_header2
                     
                    )        

                    weatherinfo = request_response.json()
                    wi = weatherinfo
                    weatherinfo2 = request_response2.json()
                    wi2 = weatherinfo2
                    print(request_url)
                    
                    #construct weather information response from OpenWeather API
                    tobody = ('Location: ' + wi['name'] + '\n' + 'Current Temperature: ' + str(wi['main']['temp'])
                    + '\n' + 'Tom. High: ' + str(wi2['list'][0]['main']['temp_max'])
                    + '\n' + 'Tom. Low: ' + str(wi2['list'][0]['main']['temp_min'])
                    + '\n' + 'Current Weather Conditions: ' + wi['weather'][0]['description']
                    + '\n' + 'Tom. Weather Conditions: ' + wi2['list'][0]['weather'][0]['description']
                    + '\n' + 'Sunrise: ' + str(wi['sys']['sunrise'])
                    + '\n' + 'Sunset: ' + str(wi['sys']['sunset'])           )

                    jsonbodyow = {'Location': wi['name'],
                     'Current Temperature': str(wi['main']['temp']),
                     'Tom. High':  str(wi2['list'][0]['main']['temp_max']),
                     'Tom. Low':  str(wi2['list'][0]['main']['temp_min']),
                     'Current Weather Conditions':  wi['weather'][0]['description'],
                     'Tom. Weather Conditions':  wi2['list'][0]['weather'][0]['description'],
                     'Sunrise': str(wi['sys']['sunrise']),
                     'Sunset':  str(wi['sys']['sunset'])}
                    #Print nonjsonformatted weather info to terminal
                    #print(tobody)
                    owjsonbody = json.dumps(jsonbodyow)
                    jsonbodyload = json.loads(owjsonbody)
                    print(owjsonbody)

                    #display weather information in client body nonjsonformatted
                    #resp.body = (tobody)

                    #JSON Formatted body response
                    resp.append_header('API', 'Open Weather API')
                    resp.body = owjsonbody
                    
                    
                elif(statebegins in alphabet[13:25]): #send client request to apixu API if state begins with N - Z
                    print(state + ' weather information must be requested from APIXU Api')
                    logger.info('Starting Weather forecast request to APIXU API')
                    resp.status = falcon.HTTP_200
                    xuapikey = "b8f9f07b62c7415fa8862117183108"
                    client = ApixuClient(xuapikey) 
                    current = client.getCurrentWeather(q=zipcode)
                    forecast = client.getForecastWeather(q=zipcode, days=2)
                    
                    #construct weather information response from APIXU
                    tobodyxu = ('Location: ' + current['location']['name']
                    + '\n' + 'Current Temperature: ' + str(current['current']['temp_c'])
                    + '\n' + 'Tom. High: ' + str(forecast['forecast']['forecastday'][1]['day']['maxtemp_c'])
                    + '\n' + 'Tom. Low: ' + str(forecast['forecast']['forecastday'][1]['day']['mintemp_c'])
                    + '\n' + 'Current Weather Conditions: ' + current['current']['condition']['text']
                    + '\n' + 'Tom. Weather Conditions: ' + str(forecast['forecast']['forecastday'][1]['day']['condition']['text'])
                    + '\n' + 'Sunrise: ' + forecast['forecast']['forecastday'][0]['astro']['sunrise']
                    + '\n' + 'Sunset: ' + forecast['forecast']['forecastday'][0]['astro']['sunset'])

                    #Weather information formatted for JSON conversion
                    jsonbodyxu = {' Location':  current['location']['name'],
                    'Current Temperature':  str(current['current']['temp_c']),
                    'Tom. High':  str(forecast['forecast']['forecastday'][1]['day']['maxtemp_c']),
                    'Tom. Low':  str(forecast['forecast']['forecastday'][1]['day']['mintemp_c']),
                    'Current Weather Conditions':  current['current']['condition']['text'],
                    'Tom. Weather Conditions':  str(forecast['forecast']['forecastday'][1]['day']['condition']['text']),
                    'Sunrise':  forecast['forecast']['forecastday'][0]['astro']['sunrise'],
                    'Sunset':  forecast['forecast']['forecastday'][0]['astro']['sunset']}

                    #Print nonjsonformatted weather info to terminal
                    #print(tobodyxu)
                    jsonbody = json.dumps(jsonbodyxu)
                    jsonbodyload = json.loads(jsonbody)
                    print(jsonbody)
                    
                    #display weather information in client body nonjsonformatted
                    #resp.body = (tobodyxu)
                    #Json Formatted Body Response 
                    resp.body = (jsonbody)
                else: #respond with error if client enters invalid state i.e. first character is not a letter
                    print('Error in parameters issued by client')
                    resp.status = falcon.HTTP_406
                    resp.body = 'You have entered an invalid State parameter.'
            except Exception:
                logger.error('Something major has gone wrong', exc_info=True)
        else:
            resp.status = falcon.HTTP_406
            logger.error('Client entered invalid parameters', exc_info=True)
            #resp.body = 'Your input contains invalid characters.'
            raise falcon.HTTPError('Bad request', 'Your input contains invalid characters.')

app = falcon.API()
app.set_error_serializer(my_serializer)
app.add_route('/GetTheWeather', GetTheWeather())
app.add_route('/', ForecastInput() )

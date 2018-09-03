


PythonForecastFinder
=======================
Example Forecast Retriever Using Falcon Framework

The purpose of this project is to solve the issue stated in the fictional prompt below using the Python Falcon Framework. 

Prompt
------------

We have determined that weather APIs are returning incorrect results depending on which state you are in. One API works correctly for only  26 states (A-M), and the other API works for the remaining 24 states (N-W).

Create a RESTful API that takes a request looking for 1 specific state and then connects to the appropriate API and consumes them in their respective formats (JSON). Once the data has been collected from the proper API, return the results to the user via JSON.

Response from the API to the user should return the following in JSON format:
    1. Location
    2. Current Temperature for today
    3. Forecasted Temperature for tomorrow
    4. Current Condition (Cloudy, Windy, Sunny, Rainy…)
    5. Forecasted Condition for tomorrow
    6. Sunrise & Sunset


Application Features
-------
API built on Falcon Framework
Waitress used as WSGI Servr
Client weather query routed to APIs at:

https://openweathermap.org/api JSON (A-M)

https://github.com/apixu/apixu-python JSON (N-W)

Logging using Python Logging module as well as custom logging utilizing Python file write method




Selenium Used For Testing
-------------

Api test script: WeatherApiTest.py




Usage
-------------

Falcon App may be served by waitress using a terminal



    python -m waitress FalconWeather:app
    
Navigate to url App is being served on to test API. 


Alternatively, request to FalconWeather may be accomplished using curl in the terminal in the following manner:

    curl -v "http://localhost:8080/GetTheWeather?city=Austin&state=TX&zip=78708"

In the example above, note that the app is being served on port 8080 with city, state, and zip parameters equal to Austin, TX, and 78707 respectively. 

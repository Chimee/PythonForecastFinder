from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import requests
from datetime import datetime

base_url = "http://localhost:8080"



def test_one(): #Open main input page

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    driver = webdriver.Chrome(executable_path='C:/Weather API Conflict/chromedriver_win32/chromedriver.exe')
    try:
        driver.get(base_url)
        assert "Chi's Forecast Finder" in driver.title
        testlog.write(str(datetime.now()) + ': Forecast Input Page Test Passed Page Title Assertion' + '\n') 
        testlog.close()
        time.sleep(5)
        driver.quit()
        
    except Exception:
        testlog.write(str(datetime.now()) + ': Forecast Input Page Test Failed Page Title Assertion' + '\n') 
        testlog.close()
        driver.quit()



def test_two(): #Test API Response after proper input

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    city = "Austin"
    state = "Texas"
    zipcode = "78708"
    driver = webdriver.Chrome(executable_path='C:/Weather API Conflict/chromedriver_win32/chromedriver.exe')
    try:
        driver.get(base_url)
        assert "Chi's Forecast Finder" in driver.title
        #Find Input Fields and enter test parameters
        elem = driver.find_element_by_name("city")
        elem.send_keys(city)
        elem = driver.find_element_by_name("state")
        elem.send_keys(state)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zipcode)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        #get response body element by name of pre
        elem=driver.find_element_by_tag_name("pre")
        datatest = elem.text
        print(datatest)
        assert("Austin" in datatest)
        testlog.write(str(datetime.now()) + ': Test_Two (Proper Input) Passed' + '\n') 

        testlog.close()
        driver.quit()
        #time.sleep(5)
        #driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Two (Proper Input) Failed' + '\n') 
        testlog.close()
        driver.quit()
    
def test_three(): #Test API Response after invalid input

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    city = "Austin"
    state = "Texas"
    zipcode = "X78708"
    driver = webdriver.Chrome(executable_path='C:/Weather API Conflict/chromedriver_win32/chromedriver.exe')
    try:
        driver.get(base_url)
        assert "Chi's Forecast Finder" in driver.title
        #Find Input Fields and enter test parameters
        elem = driver.find_element_by_name("city")
        elem.send_keys(city)
        elem = driver.find_element_by_name("state")
        elem.send_keys(state)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zipcode)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        #get response body element by name of pre
        elem=driver.find_element_by_tag_name("pre")
        datatest = elem.text
        print(datatest)
        #check for invalid characters message in response body
        assert("Your input contains invalid characters." in datatest)        
        testlog.write(str(datetime.now()) + ': Test_Three (Invalid Characters in input message) Passed' + '\n') 

        testlog.close()
        driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Three Failed' + '\n') 
        testlog.close()
        driver.quit()


def test_four(): #Test API Response For Proper Routing To OpenWeather API

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    city = "Birgmingham"
    state = "Alabama"
    zipcode = "35208"
    driver = webdriver.Chrome(executable_path='C:/Weather API Conflict/chromedriver_win32/chromedriver.exe')
    try:
        driver.get(base_url)
        assert "Chi's Forecast Finder" in driver.title
        elem = driver.find_element_by_name("city")
        elem.send_keys(city)
        elem = driver.find_element_by_name("state")
        elem.send_keys(state)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zipcode)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        #get response body element by name of pre
        elem=driver.find_element_by_tag_name("pre")
        datatest = elem.text
        print(datatest)
        assert("Birmingham" in datatest)        
        testlog.write(str(datetime.now()) + ': Test_Four (Proper Routing To OpenWeather API) Passed' + '\n')
        
        testlog.close()
        #time.sleep(5)
        driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Four Failed' + '\n')
        testlog.close()
        driver.quit()

#Testing API Response For Proper Routing To APIXU API satisfied in Test_two


test_one()
test_two()
test_three()
test_four()        

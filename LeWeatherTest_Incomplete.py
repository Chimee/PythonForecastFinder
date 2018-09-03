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
    #assert "Property Search" in driver.title
    #elem = driver.find_element_by_id("fldInput")
    #elem.send_keys(name)
    #elem = driver.find_element_by_id("login_pwd")
    #elem.send_keys(Keys.RETURN)


def test_two(): #Test API Response after proper input

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    city = "Austin"
    state = "Texas"
    zipcode = "78708"
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
        testlog.write(str(datetime.now()) + ': Test_Two Passed' + '\n') 

        testlog.close()
        #time.sleep(5)
        #driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Two Failed' + '\n') 
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
        elem = driver.find_element_by_name("city")
        elem.send_keys(city)
        elem = driver.find_element_by_name("state")
        elem.send_keys(state)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zipcode)
        elem.send_keys(Keys.RETURN)
        testlog.write(str(datetime.now()) + ': Test_Three Passed' + '\n') 

        testlog.close()
        #time.sleep(5)
        #driver.quit()
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
        testlog.write(str(datetime.now()) + ': Test_Four Passed' + '\n')
        
        testlog.close()
        #time.sleep(5)
        #driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Four Failed' + '\n')
        testlog.close()
        driver.quit()

def test_five(): #Test API Response For Proper Routing To APIXU API

    testlog = open('/Weather API Conflict/logs/testresults.txt', "a")
    city = "Austin"
    state = "Texas"
    zipcode = "78708"
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
        testlog.write(str(datetime.now()) + ': Test_Five Passed' + '\n')
        testlog.close()
        #time.sleep(5)
        #driver.quit()
    except Exception:
        testlog.write(str(datetime.now()) + ': Test_Five Failed' + '\n')
        testlog.close()
        driver.quit()         



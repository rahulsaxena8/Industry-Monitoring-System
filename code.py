
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import time

import pyttsx3

#initialize the text to speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def tts(text):
    engine.say(text)
    engine.runAndWait()


#define the scope of the credential file
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('industry-monitoring-system-69f53b557610.json', scope)
client = gspread.authorize(creds)

#get the instance of the SpreadSheet and open the sheet
sheet = client.open('Sensor Readings')
sheet_instance = sheet.get_worksheet(0)

#check if temperature is within the threshold of 20-30 degree celsius
def check_temperature(temperature):
    if temperature < 20:
        tts("temperature has dropped below the threshold, please maintain the temperature between 20 to 30 degree celsius!")
    elif temperature >= 20 and temperature <=30:
        tts("temperature is fine!")
    elif temperature > 30:
        tts("temperature has gone above the threshold, please maintain the temperature between 20 to 30 degree celsius!")

#check if humidity is within the threshold of 45-55 %
def check_humidity(humidity):
    if humidity < 45:
        tts("humidity has dropped below the threshold, please maintain the humidity between 45 to 55 percent!")
    elif humidity >= 45 and humidity <= 55:
        tts("humidity is fine!")
    elif humidity > 55:
        tts("humidity has gone above the threshold, please maintain the humidity between 45 to 55 percent!")
        
#check if pressure is within the threshold of 12-18 pascals
def check_pressure(pressure):
    if pressure < 12:
        tts("pressure has dropped below the threshold, please maintain the pressure between 12 to 18 pascals!")
    elif pressure >= 12 and pressure <=18:
        tts("pressure is fine!")
    elif pressure > 18:
        tts("pressure has gone above the threshold, please maintain the pressure between 12 to 18 pascals!")


#get the value at a specific cell
while True:
    temperature = int(sheet_instance.cell(col=2,row=2).value)
    check_temperature(temperature)

    humidity = int(sheet_instance.cell(col=2,row=3).value)
    check_humidity(humidity)

    pressure = int(sheet_instance.cell(col=2,row=4).value)
    check_pressure(pressure)

    time.sleep(300)

#note - install dotenv package
import os
import requests
from dotenv import load_dotenv
load_dotenv

#list of nightscout url extensions to fetch specific data
bolus_period = 2
ns_commands = {
     '100s': "/api/v1/entries.json?find[sgv]=100",
     'Boluses': "/api/v1/treatments.json?find[insulin][$gte]=" + str(bolus_period)
}
#temp storage for data
ns_data = {
     '100s': '',
     'Boluses': ''
}
num_of_commands = len(ns_commands)
command_list = ns_commands.keys()

def fetch_ns(url_extension):
    url = os.getenv('NS_URL')
    print(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
            return(response.text)
        else:
            print("Error: File does not exist")
            return(None)
    except requests.exceptions.RequestException:
        print("Error: Could not connect to server")
        return(None)

#just goes through all the different fetch url extensions
for key in command_list:
     url_extension = ns_commands[key]
     fetched_data = fetch_ns(url_extension)
     ns_commands[key] = fetched_data
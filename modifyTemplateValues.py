#!/usr/bin/env python3
################################################################################
# Filename: modifyTemplateValues.py
# Date Created: 20190623
# Author: Marco Tijbout
#
# Version 1.0
#
# Description: 
#   Script to modify specific value of specific template.
#
# Requirements:
#   Install any missing modules. 
#
# Usage: Provide authentication details in the script below.
#
# Version history:
# 1.0 - Marco Tijbout: Original script.
################################################################################

## This is my trial and error script experient to see how it works.
## This script is documenten per command. Not very pretty. I believe most is readible though.

# Import stuff that we apparently need...
import requests
import json
import time
import urllib.request ## Not sure if needed.
from requests.auth import HTTPBasicAuth
from datetime import datetime

# URL of the API server instance.
url = 'https://iotc008.vmware.com/api/tokens'

# Configure the headers to work with the API server.
headers = {'Accept': 'application/json;api-version=1.0', 'Content-Type': 'application/json'}

# resp_auth gives the HTTP answer 200 or other.
resp_auth = requests.get(url, headers=headers, auth=HTTPBasicAuth('marco@pulse.local', 'VMware1!'))

## Print message if command is other than OK.
if resp_auth.status_code != 200:
    print(resp_auth.text)
    raise Exception('Recieved non 200 response.')

# Convert the output to readible text.
resp_str = resp_auth.text

# Convert the output to a json dictionary
resp_dict = json.loads(resp_str)

# Filter from the dictionary
resp_dict['accessToken']

# Only thet the token
token = resp_dict['accessToken']

# Get the expiry value for the Token
expires = resp_dict['accessTokenExpiresAt']

# Display when the token expires.
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print('Access Token expires:')
print(datetime.utcfromtimestamp(expires).strftime('%Y-%m-%d %H:%M:%S'))

# Change the headers to use the Bearer token instead of username and password
headers = {'Accept': 'application/json;api-version=1.0', 'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % token}

# Change the URL to the item where we want to collect information from.
# url = 'https://iotc008.vmware.com/api/device-templates'
# URL for specific template. Get the Template ID from the other script.
url = 'https://iotc008.vmware.com/api/device-templates/e556178e-fe5e-4a8d-9bb3-d73a4e8291a2'

# Get the information and store it directly as a json dictionary.
resp_dev_templates = requests.get(url, headers=headers).json()

# print()
# print(resp_dev_templates)
# print()

# print('Print dictionary:')
# print(json.dumps(resp_dev_templates, indent=4, sort_keys=True))


#------------------------------------------------------------------------------#
# Sub Values
#

# cfisValue = resp_dev_templates['templates'][0]['settings'][0]['settings']['commandFetchIntervalSeconds']
# print ("commandFetchIntervalSeconds = " + str(cfisValue))

#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Change a value of a sub key.
#
print()
print('#------------------------------------------------------------------------------#')
print('Before: ')
print(resp_dev_templates)
print()

print()
print('#------------------------------------------------------------------------------#')
print('Value manipulation: ')

print('Old value: ')
print( resp_dev_templates['settings'][0]['settings']['commandFetchIntervalSeconds'])
resp_dev_templates['settings'][0]['settings']['commandFetchIntervalSeconds'] = 5
print('New value: ')
print( resp_dev_templates['settings'][0]['settings']['commandFetchIntervalSeconds'])

# url = 'https://iotc008.vmware.com/api/device-templates/e556178e-fe5e-4a8d-9bb3-d73a4e8291a2'
put_dev_templates = requests.put(url, headers=headers, data=json.dumps(resp_dev_templates))

# #req = requests.put(event['ResponseURL'], data=json.dumps(resp_dev_templates))

if put_dev_templates.status_code == 200:
    print(put_dev_templates.text)
    raise Exception('Recieved 200 response while sending response to API.')

if put_dev_templates.status_code != 200:
    print(put_dev_templates.text)
    raise Exception('Recieved non 200 response while sending response to API.')

# def change_key(d, required_key, new_value):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             change_key(v, required_key, new_value)
#         if k == required_key:
#             d[k] = new_value

# stocks = {
#     'name': 'stocks',
#     'IBM': 146.48,
#     'MSFT': 44.11,
#     'CSCO': 25.54,
#     'micro': {'name': 'micro', 'age': 1}
# }

#  change_key(resp_dev_templates, 'commandFetchIntervalSeconds', 'int(5)')

print()
print('#------------------------------------------------------------------------------#')
print('After: ')
print(resp_dev_templates)

#------------------------------------------------------------------------------#


# template_name = resp_dev_templates['templates'][0]['name']
# template_id = resp_dev_templates['templates'][0]['id']
# print()
# print('Name: ' + template_name)
# print('ID  : ' + template_id)

# For each item show name and ID.
# for each in resp_dev_templates['templates']:
#     print()
#     print('Name                 : ' + each['name'])
#     print('ID                   : ' + each['id'])
#     #print('commandFetchInterval : ' + each['commandFetchIntervalSeconds'])


##
## Below is garbage and test stuff. No guarantee stuff works you find here.
##

# resp_str = resp_devices.text
# json_object = json.loads(resp_str)


# def func1(damn):
#     for key,value in damn.items():
#         print ('\n'+str(key)+' -> '+str(value))
#         if type(value) == type(dict()):
#             func1(value)
#         elif type(value) == type(list()):
#             for val in value:
#                 if type(val) == type(str()):
#                     pass
#                 elif type(val) == type(list()):
#                     pass
#                 else:
#                     func1(val)
# func1(json_object)

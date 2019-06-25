#!/usr/bin/env python3
################################################################################
# Filename: APIconnectionTest.py
# Date Created: 20190623
# Author: Marco Tijbout
#
# Version 1.0
#
# Description: 
#   Script to access the API server with authentication and Bearer token.
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

# External function from getUserCreds.py:
from getUserCreds import user_creds

# Ask for credentials
uname, pwd = user_creds()
# print("Username = ", uname)
# print("Password = ", pwd)

# Ask for instance
instance = input("Pulse instance <instance_name>.vmware.com : ")
# print(instance)

# URL of the API server instance.
url = 'https://'+instance +'.vmware.com/api/tokens'
# print(url)

# Configure the headers to work with the API server.
headers = {
    'Accept': 'application/json;api-version=1.0',
    'Content-Type': 'application/json'
    }

# resp_auth gives the HTTP answer 200 or other.
resp_auth = requests.get(url, headers=headers, auth=HTTPBasicAuth(uname, pwd)).json()

# Convert the output to readible text.
# resp_str = resp_auth.text

# Convert the output to a json dictionary
# resp_dict = json.loads(resp_str)

# Filter from the dictionary
# resp_dict['accessToken']
# resp_auth['accessToken']

# Only the the token
token = resp_auth['accessToken']
print(token)

# Get the expiry value for the Token
#expires = resp_dict['accessTokenExpiresAt']

# Display when the token expires.
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print('Access Token expires:')
#print(datetime.utcfromtimestamp(expires).strftime('%Y-%m-%d %H:%M:%S'))

# print(r)
# print(token)

# Change the headers to use the Bearer token instead of username and password
headers = {
    'Accept': 'application/json;api-version=1.0',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' % token
    }

# Change the URL to the item where we want to collect information from.
url = 'https://iotc008.vmware.com/api/device-templates'

# Get the information and store it directly as a json dictionary.
resp_dev_templates = requests.get(url, headers=headers).json()

# template_name = resp_dev_templates['templates'][0]['name']
# template_id = resp_dev_templates['templates'][0]['id']
# print()
# print('Name: ' + template_name)
# print('ID  : ' + template_id)

# For each item show name and ID.
for each in resp_dev_templates['templates']:
    print()
    print('Name: ' + each['name'])
    print('ID  : ' + each['id'])


#------------------------------------------------------------------------------#
# Sub Values
#

cfisValue = resp_dev_templates['templates'][0]['settings'][0]['settings']['commandFetchIntervalSeconds']
print ("commandFetchIntervalSeconds = " + str(cfisValue))

#------------------------------------------------------------------------------#

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

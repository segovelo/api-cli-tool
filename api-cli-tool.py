# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:36:46 2022

@author: sebas
"""
from argparse import ArgumentParser
import csv
import json
from pprint import pprint
import requests


def read():
   fake_data_list_url = 'https://61004cc6bca46600171cf84a.mockapi.io/api-crud/v1/fakeData'
   response = requests.get(fake_data_list_url)

   return response.json()

def preview(data):
   pprint(data)
   
def save(data):
   with open('fake_data.csv', 'w') as f:
       field_names = ['id', 'firstName', 'lastName', 'checkbox']
       writer = csv.DictWriter(f, fieldnames=field_names)

       writer.writeheader()
       for row in data.json():
           writer.writerow(row)
           
           
if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for interacting with our API')
   parser.add_argument('-r', '--read', action='store_true', help='Sends a GET request to the product API.')
   parser.add_argument('-p', '--preview', action='store_true', help='Shows us a preview of the data.')
   parser.add_argument('-s', '--save', action='store_true', help='Saves the response to a CSV file.')


   args = parser.parse_args()

   if args.read:
       read()
   if args.preview:
       preview(read())
   else:
       print('Use the -h or --help flags for help')
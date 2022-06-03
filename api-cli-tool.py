# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:36:46 2022

@author: sebas
"""
from argparse import ArgumentParser
#import argparse
import csv
import json
from pprint import pprint
import requests

def read(url):
   #fake_data_list_url = 'https://61004cc6bca46600171cf84a.mockapi.io/api-crud/v1/fakeData'
   #fake_data_list_url = 'https://qxo3mb6xaa.execute-api.us-east-2.amazonaws.com/latest/posts'
   #%fake_data_list_url = 'https://qxo3mb6xaa.execute-api.us-east-2.amazonaws.com/latest/users'
   response = requests.get(url)
   return response.json()

def preview(data):
   pprint(data)
   
def save(data, file_name):
   with open(file_name, 'w') as f:       
       writer = csv.DictWriter(f, list(data[0].keys()))

       writer.writeheader()
       for row in data:
           writer.writerow(row)
           
           
if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for interacting with our API')
   parser.add_argument('-r', '--read', action='store_true', help='Sends a GET request to the product API.')
   parser.add_argument('-p', '--preview', action='store_true', help='Shows us a preview of the data.')
   parser.add_argument('-s', '--save', action='store', help='Saves the response to a CSV file.')
   parser.add_argument('-u', '--url', action='store', help='URL passed as argument')

   args = parser.parse_args()
   
   if args.url:
       print("\nUrl passed as command line argument: % s" % args.url)
   if args.read:
       read(args.url)
   if args.preview:
       preview(read(args.url))
   if args.save:
       save(read(args.url), args.save)
   else:
       print('Use the -h or --help flags for help')



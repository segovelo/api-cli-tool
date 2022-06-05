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
import re

def read(url):
   response = requests.get(url)
   pprint(response.status_code)
   pprint(response.text)
   return response.json()

def preview(data):
   pprint(data)
   
def save(data, file_name):
    file_name_1 = file_name.translate({ord(i): None for i in '!#@{}[]<>=+£%^&*()?|,;:/\\\'\"'})
    file_name_2 = re.sub(r"\s+", "", file_name_1)
    file_extension = file_name_2[-4:].rstrip()
    if file_extension == '.csv':
        save_csv(data, file_name)
    elif file_extension == '.txt':
        save_txt(data, file_name)

            
def save_csv(data, file_name):
    with open(file_name, 'w') as f:  
        writer = csv.DictWriter(f, list(data[0].keys()))    
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def save_txt(data, file_name):
    with open(file_name, 'w') as f:
        f.write('[')
        for row in data:
            f.write('\n\t{\n')
            for key, value in row.items():
                f.write('\t%s: %s,\n' % (key, value))
            f.write('\t},')
        f.write('\n]')
    
    
            
if __name__ == '__main__':
   parser = ArgumentParser(description='A command line tool for interacting with our API')
   parser.add_argument('-r', '--read', action='store_true', help='Sends a GET request to the product API.')
   parser.add_argument('-p', '--preview', action='store_true', help='Shows us a preview of the data.')
   parser.add_argument('-s', '--save', action='store', help='Saves the response to a CSV file.')
   parser.add_argument('-u', '--url', action='store', help='URL passed as argument')

   args = parser.parse_args()
   data = []
   if args.url:
       print("\nUrl passed as command line argument: % s" % args.url)
   if args.read:
       data = read(args.url)
   if args.preview:
       if len(data) == 0:
           data = read(args.url)           
       preview(data)
   if args.save:
       if len(data) == 0:
           data = read(args.url)           
       save(data, args.save)
   else:
       print('Use the -h or --help flags for help')



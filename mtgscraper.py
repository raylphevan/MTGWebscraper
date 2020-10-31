import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://ebay.to/35L6afm')

soup = BeautifulSoup(response.text, 'html.parser')
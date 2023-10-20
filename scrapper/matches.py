from bs4 import BeautifulSoup
import requests
import psycopg2
from constant.urls import base_url

def get_response(url):
    matches=[]
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    return soup.prettify

print(get_response(base_url))
import requests
from bs4 import BeautifulSoup
import pickle
import re
import sys

#--------------------------------------------------
#https://towardsdatascience.com/intro-to-yelp-web-scraping-using-python-78252318d832
#--------------------------------------------------

def yelp_url_to_data(url):
    """Returns HTML Data from specified URL"""
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = soup.find_all('p')
    print(text)

    


if __name__ == '__main__':
    url_to_data(sys.argv[1])

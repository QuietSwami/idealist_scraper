#!/bin/usr/env python3

#
# Scraper for the Idealista Scraper.
#



import requests
import datetime
import sys
from dbutils import *
import json
import time
import logging
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options




def searchByQuery(query):
    """Returns all the house references in the first page of a query.

    Arguments:
        houseRef {string/integer} -- Idealista reference for the house.

    TODO:
        - Check if link is valid (check if house still exists).
        - Return:
            - REF
    """
    pass

def scrapeHouse(houseRef):
    """Returns all the valuable information from the house.

    Arguments:
        houseRef {string/integer} -- Idealista reference for the house.

    TODO:
        - Check if link is valid (check if house still exists).
        - Check if is RENT or BUY
        - Return:
            - Price
            - M^2
            - IF LOCAL:
                - Address
            - Structure - T0/T1/...
    """
    pass

def scrapePrice(houseRef):
    """Only scrapes the price of the house.

    Arguments:
        houseRef {string/integer} -- Idealista reference for the house.

    TODO:
        - Check if link is valid (check if house still exists).
        - Return:
            - Price
    """
    pass

if __name__ == "__main__":
    pass
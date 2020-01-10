#!/bin/usr/env python3

#
# DB Utilities for the Idealista Scraper.
#


import sqlite3
import datetime


def getConnection(dbname):
    return sqlite3.connect(dbname)


def createHouseTable(conn):
    pass

def insertHouse(House, conn):
    pass


if __name__ == "__main__":
    pass
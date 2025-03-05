from sqlite3 import *
import sqlite3

db = sqlite3.connect('databasa/database.sqlite3')
sql = db.cursor()

###    bu baza bilan bog'lanish uchun ochilgan fayll

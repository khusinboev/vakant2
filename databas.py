from sqlite3 import *
import sqlite3
from pathlib import Path


db = sqlite3.connect(str(Path(__file__).resolve().parent)+'databasa/database.sqlite3')
sql = db.cursor()

###    bu baza bilan bog'lanish uchun ochilgan fayll

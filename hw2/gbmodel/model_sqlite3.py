"""
A simple guestbook flask app.
ata is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+
| Name       | Email            | signed_on  | message        |
+============+==================+============+----------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world    |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date, message);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from bubbletea")
        except sqlite3.OperationalError:
            cursor.execute("create table bubbletea (name text, address text, special)")
            cursor.execute("insert into bubbletea(name, address, special) VALUES ('dingtea', 'PDX', 'taro'") 
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, address, special
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM bubbletea")
        return cursor.fetchall()

    def insert(self, name, address, special):
        """
        Inserts entry into database
        :param name: String
        :param address: String
        :param special: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name, 'address':address, 'special':special}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into bubbletea (name, address, special) VALUES (:name, :address, :special)", params)

        connection.commit()
        cursor.close()
        return True

"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.guestentries = []

    def select(self):
        """
        Returns guestentries list of lists
        Each list in guestentries contains: name, address, special
        :return: List of lists
        """
        return self.guestentries

    def insert(self, name, address, special):
        """
        Appends a new list of values representing new message into guestentries
        :param name: String
        :param address: String
        :param special: String
        :return: True
        """
        params = [name, address, special]
        self.guestentries.append(params)
        return True

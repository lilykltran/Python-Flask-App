"""Base class for model.  Derived models must implement abstract methods"""
class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, name, streetAddress, city, state, zipCode, hours, phone, rating, review, drink):
        """
        Inserts entry into database
        :param name: String
        :param streetAddress: String
        :param city: String
        :param state: String
        :param zipCode: String
        :param hours: String
        :param phone: String
        :param rating: String
        :param reviews: String
        :param drink: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

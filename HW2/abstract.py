from abc import ABC, abstractmethod

class BaseModel(ABC):
  
  """
  Fetch all of the entries in the database
  """
  @abstractmethod
  def fetchall(self):
    pass


  """
  Fetch all stores matching a requested term
  """
  @abstractmethod
  def fetch_by_name(self, name):
    pass


  """
  Add a new bubbletea store to the database
  """
  @abstractmethod
  def add_bubbletea(self, id):
    pass


  """
  Update a store w/ a matching an id
  """
  @abstractmethod
  def update_bubbletea(self, id):
    pass


  """
  Delete a store w/ a matching an id
  """
  @abstractmethod
  def delete_bubbletea(self, id):
    pass



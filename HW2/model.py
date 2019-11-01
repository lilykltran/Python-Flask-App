from abstract import BaseModel

bubbletea_list = [["Dingtea", "PDX", "9am-9pm", "Taro"],["Tea Bar", "PDX", "9 am-9pm", "Matcha"],["Bambu", "PDX", "10am-7pm", "Mango"]]

class DModel(BaseModel):
  
  def __init__(self, app):
    self.app = app

  def fetchall(self):
    return bubbletea_list

  def fetch_by_name(self, name):
    return True

  def fetch_by_id(self, id):
    return True

  def add_bubbletea(self, id):
    return True

  def update_bubbletea(self, id):
    return True

  def delete_bubbletea(self, id):
    return True

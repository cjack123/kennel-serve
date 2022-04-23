from concurrent.futures.process import _python_exit
from unicodedata import name


class Customer():
    def __init__(self, id, first_name, last_name, address, phone, email):
        self.id = id
        self.first_name =first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email

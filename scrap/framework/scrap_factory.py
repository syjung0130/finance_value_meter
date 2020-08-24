
from value import Value

class ScrapFactory:
    def __init__(self, scrap_type):
        print("__init__")
        self.scrap_type = scrap_type
    
    def create_scrap(self):
        print("create_scrap")

    def scrap_value(self):
        print("scrap_value")

if __name__ == "__main__":
    scrap_type = 1
    scrap = ScrapFactory(scrap_type)
    scrap.create_scrap()

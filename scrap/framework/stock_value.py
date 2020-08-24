from value import Value

class StockValue(Value):
    def __init__(self, value_type):
        print("__init__")
        super().__init__(value_type)
        print("value type : {}".format(self.value_type))
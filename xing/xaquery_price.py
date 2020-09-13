import sys
import win32com.client
from xasession import XASession, XASessionEventHandler
import json
import pythoncom

class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1        

class XAQueryPrice:
    def __init__(self):
        print('__init__')
        self.session = XASession()
        self.session.login()
        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        self.query.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"
    
    def RequestData(self, code):
        self.query.SetFieldData("t1102InBlock", "shcode", 0, code)
        self.query.Request(0)
        while XAQueryEventHandler.query_state == 0:
            pythoncom.PumpWaitingMessages()
        return
    
    def GetPrice(self):
        return self.query.GetFieldData("t1102OutBlock", "price", 0)
    
    def GetName(self):
        return self.query.GetFieldData("t1102OutBlock", "hname", 0)

if __name__ == "__main__":
    str_code = "078020"
    query_price = XAQueryPrice()
    query_price.RequestData(str_code)
    print("name: ", query_price.GetName())
    print("price: ", query_price.GetPrice())
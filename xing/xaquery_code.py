import sys
import win32com.client
from xasession import XASession, XASessionEventHandler
import json
import pythoncom

class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1

class XAQueryCode:
    def __init__(self):
        print("__init__")
        self.session = XASession()
        self.session.login()

        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        self.query.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8430.res"

    def RequestData(self):
        self.query.SetFieldData("t8430InBlock", "gubun", 0, 1)
        self.query.Request(0)
        while XAQueryEventHandler.query_state == 0:
            pythoncom.PumpWaitingMessages()
        return
    
    def PrintData(self):
        count = self.query.GetBlockCount("t8430OutBlock")
        for i in range(5):
            name = self.query.GetFieldData("t8430OutBlock", "hname", i)
            shcode = self.query.GetFieldData("t8430OutBlock", "shcode", i)
            expcode = self.query.GetFieldData("t8430OutBlock", "expcode", i)
            etfgubun = self.query.GetFieldData("t8430OutBlock", "etfgubun", i)
            print(i, name, shcode, expcode, etfgubun)        

if __name__ == "__main__":
    query_code = XAQueryCode()
    query_code.RequestData()
    query_code.PrintData()

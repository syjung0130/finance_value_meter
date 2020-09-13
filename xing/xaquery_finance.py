import sys
import win32com.client
from xasession import XASession, XASessionEventHandler
import json
import pythoncom

class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1

class XAQueryFinance:
    def __init__(self):
        print("__init__")
        self.session = XASession()
        self.session.login()

        self.query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
        self.query.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t3320.res"

    def RequestData(self):
        self.query.SetFieldData("t3320InBlock", "gicode", "005930", 0)
        self.query.Request(0)
        while XAQueryEventHandler.query_state == 0:
            pythoncom.PumpWaitingMessages()
        return
    
    def PrintData(self):
        count = self.query.GetBlockCount("t3320OutBlock1")
        gsym = 0.0
        per = 0.0
        pbr = 0.0
        roe = 0.0
        print("count : {}".format(count))
        for i in range(count):
            gsym = self.query.GetFieldData("t3320OutBlock1", "gsym", 0)
            per = self.query.GetFieldData("t3320OutBlock1", "per", 0)
            pbr = self.query.GetFieldData("t3320OutBlock1", "pbr", 0)
            roe = self.query.GetFieldData("t3320OutBlock1", "roe", 0)
            print("[{0}] per: {1}, pbr:{2}, roe:{3}".format(i, per, pbr, roe))

        count = self.query.GetBlockCount("t3320OutBlock")
        company = ""
        print("count : {}".format(count))
        for i in range(count):
            company = self.query.GetFieldData("t3320OutBlock", "company", 0)
            print("[{0}] company: {1}".format(i, company))

if __name__ == "__main__":
    query_code = XAQueryFinance()
    query_code.RequestData()
    query_code.PrintData()

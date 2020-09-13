import sys
import win32com.client
from xasession import XASession, XASessionEventHandler
import json
import pythoncom

class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1        

if __name__ == "__main__":
    session = XASession()
    session.login()

    query = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandler)
    query.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"

    query.SetFieldData("t1102InBlock", "shcode", 0, "078020")
    query.Request(0)

    while XAQueryEventHandler.query_state == 0:
        pythoncom.PumpWaitingMessages()

    name = query.GetFieldData("t1102OutBlock", "hname", 0)
    price = query.GetFieldData("t1102OutBlock", "price", 0)
    print(name)
    print(price)
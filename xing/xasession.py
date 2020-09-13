import sys
import win32com.client
import json
import pythoncom


g_login_done = False
# 이벤트 처리용 클래스
class XASessionEventHandler:
    def __init__(self):
        self.user_obj = None
        self.com_obj = None

    def connect(self, user_obj, com_obj):
        self.user_obj = user_obj
        self.com_obj = com_obj

    def OnLogin(self, code, msg):
        # self.user_obj.status = True
        global g_login_done
        g_login_done = True
        print(code, msg)


# XASession 클래스
class XASession:
    def __init__(self):
        print("__init__")
        # self.status = False
        global g_login_done
        g_login_done = False
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
        self.event_handler = win32com.client.WithEvents(self.session, XASessionEventHandler)
        self.event_handler.connect(self, self.session)
        self.session.ConnectServer("hts.ebestsec.co.kr", 20001)


    def login(self):
        print("login")
        with open('info.json') as json_file:
            self.json_data = json.load(json_file)

        ID = self.json_data["ID"]
        PASSWD = self.json_data["PASSWD"]
        CERT = self.json_data["CERT"]
        self.session.Login(ID, PASSWD, CERT, 0, False)

        # while not self.status:
        global g_login_done
        while not g_login_done:
            pythoncom.PumpWaitingMessages()

    def get_account_list(self):
        account_list = []
        count = self.session.GetAccountListCount()
        for i in range(count):
            account = self.session.GetAccountList(i)
            account_list.append((account))
        return account_list


if __name__ == "__main__":
    session = XASession()
    session.login()
    accounts = session.get_account_list()
    print(accounts)
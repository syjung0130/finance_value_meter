from PyQt5.QtWidgets import *
import sys
import win32com.client
import json

ID = "아이디"
PASSWD = "비밀번호"
CERT = "공인인증서비밀번호"


# 이벤트 처리용 클래스
class XASessionEvents:
    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
        else:
            print("로그인 실패 ", msg)


# XASession 클래스
class XASession:
    def __init__(self):
        self.session = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents)
        self.session.ConnectServer("hts.ebestsec.co.kr", 20001)

    def login(self):
        print("login")
        with open('info.json') as json_file:
            self.json_data = json.load(json_file)

        ID = self.json_data["ID"]
        PASSWD = self.json_data["PASSWD"]
        CERT = self.json_data["CERT"]
        self.session.Login(ID, PASSWD, CERT, 0, False)
    def get_account_list(self):
        account_list = []
        count = self.session.GetAccountListCount()
        for i in range(count):
            account = self.session.GetAccountList(i)
            account_list.append((account))
        return account_list


class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("계좌 가져오기", self)        
        self.t_edit = QTextEdit("")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.t_edit)

        self.setLayout(self.layout)

        self.btn.clicked.connect(self.get_account)

        self.session = XASession()
        self.session.login()

    def get_account(self):
        accounts = self.session.get_account_list()
        print("계좌: {}".format(accounts))
        self.t_edit.append("계좌: {}".format(accounts))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
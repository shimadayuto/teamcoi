import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# wks.update_acell("A1","")
# wks.update_acell("B1","")
class Sheet:
    def __init__(self):
        self.name_list = ["yuto", "kato", "wang", "shigeaki", "yuka"]
        self.id_list = ["01010a10e41a9f23","01010910a417c81b","01010A10E41A9F25","010106010407e602","01010312841a360d"]
        self.scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/teamcoi/gspread-sample-44bb354dbe62.json', self.scope)

    def read(self,cell):
        return wks.acell(cell).value

    def clear(self,cell,moji):
        wks = self.open
        wks.update_acell(cell, moji)

    def open(self):
        print("open spread sheet")
        gc = gspread.authorize(self.credentials)
        wks = gc.open('senzokuike').sheet1
        return wks

    def write(self,IDs):
        wks = self.open()
        print("updating google spread sheet now...")
        print("")
        names = ""
        num = []

        for i in range(len(IDs)):
            num.append(self.id_list.index(IDs[i]))
            names = names + self.name_list[num[i]] + ', '
    
        cell = "B1"
        if wks.acell(cell).value is "":
            names = names[:-2]
            wks.update_acell("A1","=CHAR(HEX2DEC(\"1f37b\"))")
            wks.update_acell(cell, names)
        elif names is "":
            wks.update_acell("A1","")
            wks.update_acell(cell, names)
        else:
            names = names[:-2]
            wks.update_acell(cell, names)

        print(wks.acell(cell))
        print("succeeded to update")
        print("")

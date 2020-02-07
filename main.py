import time
from sheet import Sheet
import pressure_sensor
import threading
import datetime
#from readNFC import scanning
import led
import requests

class mat:
    
    def __init__(self):
        self.idm = "01010312841a360d"
        self.isScaned = True #for demonstration
        self.isStepped = False
        self.IDs = ["01010a10e41a9f23","01010A10E41A9F25"]
        self.sheet = Sheet()
        self.num = 0
        self.sheet.write(self.IDs)
    
    def maintanance(self):
        while True:
            #sheet.open()

            # now  = datetime.datetime.now()
            # current_hour = int(now.strftime("%H"))
            # if 5 < current_hour < 15:
            #     self.__init__()
            #     sheet.clear('B1',"=CHAR(HEX2DEC(\"1f917\"))")
            #     sheet.clear('A1',"")

            time.sleep(60)

    # def ScanID(self):
    #     reader = scanning()
    #     while True:
    #             reader.exe_scan()
    #             led.led_on("blue")
    #             self.isScaned = True
    #             self.idm = reader.idm 
    #             print("detected card")
    #             print("user id : " +  self.idm)
    #             #elf.show()
    #             print("")

    def WaitStep(self):
        while True:
            time.sleep(0.3)
            if pressure_sensor.sensing() is True:
                self.isStepped = True
            # if self.isScaned is True:
            #     time.sleep(10)
    
    def UpdateSheet(self):

        if not self.idm in self.IDs:
            self.IDs.append(self.idm)
            self.SendToLINE()
            self.sheet.write(self.IDs)
            time.sleep(10)
            self.IDs.remove(self.idm)
            self.sheet.write(self.IDs)
        else:
            print("cancel action")
            self.IDs.remove(self.idm)
        



    def SendToLINE(self):
        url = "https://notify-api.line.me/api/notify"
        token = "8KUextLc2r7ARf9uyoVeioxkrE18NU7FOTkmhxlb7uT"
        headers = {"Authorization" : "Bearer " + token}
        payload = {"message" : "yuto, wang, yuka" }
        #files = {"imageFile": open("test.jpg", "rb")} #バイナリで画像ファイルを開きます。対応している形式はPNG/JPEGです。
        r = requests.post(url ,headers = headers ,params=payload) #, files=files)

    def processing(self):
        while True:
            if self.isStepped is True:
                #print("waiting for being stepped")
                #スキャンされてからマットを踏むまでの待機時間
                name = "yuka"
                if self.isStepped is True:
                    print( name + " stepped on the mat")
                    self.UpdateSheet()
                else:
                    print( name + " didn't stepped ")
                    
                self.isScaned = True #for demonstration
                self.isStepped = False
                print("restart processing")
                print("")
                led.led_off("blue")
                led.led_off("red")
            
            else:
                pass

            # elif self.isStepped is True:
            #     #print("waiting for detecting card")
            #     #マットを踏んでからスキャンするまでの待機時間
            #     time.sleep(10)
            #     if self.isScaned is True:
            #         name = self.sheet.name_list[self.sheet.name_list.index(self.idm)]
            #         print( name + " scanned caed")
            #         self.UpdateSheet()
            #     else:
            #         print("mat was stepped but NOT detected card")

            #     self.isScaned = False
            #     self.isStepped = False
            #     print("restart processing")
            #     led.led_off("blue")
            #     led.led_off("red")
                        
            # else:
            #     time.sleep(5)

coimat = mat()

print("setting up now...")
time.sleep(3)
print("set up finished")
print("main loop start")
print("")
led.led_on("green")

#LED光らせる

#thread_scan = threading.Thread(target = coimat.ScanID)
thread_step = threading.Thread(target = coimat.WaitStep)
thread_processing = threading.Thread(target = coimat.processing)
thread_maintainance = threading.Thread(target = coimat.maintanance)

#thread_scan.start()
thread_step.start()
thread_processing.start()
thread_maintainance.start()
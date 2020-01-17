from sheet import Sheet
import pressure_sensor
import time
import threading
import datetime
from readNFC import scanning
import led

class mat:
    
    def __init__(self):
        self.idm = ""
        self.isScaned = False
        self.isStepped = False
        self.IDs = []
        self.IDs.clear()
        self.sheet = Sheet()
    
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


    # def show(self):
    #     name = self.sheet.name_list[self.sheet.id_list.index(self.idm)]
    #     print("person : " + name)


    def ScanID(self):
        reader = scanning()
        while True:
                reader.exe_scan()
                led.led_on("blue")
                self.isScaned = True
                self.idm = reader.idm 
                print("detected card")
                print("user id : " +  self.idm)
                #elf.show()
                print("")

    def WaitStep(self):
        while True:
            time.sleep(0.3)
            if pressure_sensor.sensing() is True:
                self.isStepped = True
            # if self.isScaned is True:
            #     time.sleep(10)
    
    def UpdateSheet(self):
        self.sheet.open()
        if not self.idm in self.IDs:
            self.IDs.append(self.idm)
        else:
            print("cancel action")
            self.IDs.remove(self.idm)
        
        self.sheet.write(self.IDs)
    
    def processing(self):
        while True:
            if self.isScaned is True:
                #print("waiting for being stepped")
                #スキャンされてからマットを踏むまでの待機時間
                time.sleep(10)
                name = self.sheet.name_list[self.sheet.id_list.index(self.idm)]
                if self.isStepped is True:
                    print( name + " stepped on the mat")
                    self.UpdateSheet()
                else:
                    print( name + " didn't stepped ")
                    
                self.isScaned = False
                self.isStepped = False
                print("restart processing")
                print("")
                led.led_off("blue")
                led.led_off("red")

            elif self.isStepped is True:
                #print("waiting for detecting card")
                #マットを踏んでからスキャンするまでの待機時間
                time.sleep(10)
                if self.isScaned is True:
                    name = self.sheet.name_list[self.sheet.id_list.index(self.idm)]
                    print( name + " scanned caed")
                    self.UpdateSheet()
                else:
                    print("mat was stepped but NOT detected card")

                self.isScaned = False
                self.isStepped = False
                print("restart processing")
                led.led_off("blue")
                led.led_off("red")
                        
            else:
                time.sleep(5)

coimat = mat()

print("setting up now...")
time.sleep(3)
print("set up finished")
print("main loop start")
print("")
led.led_on("green")

#LED光らせる

thread_scan = threading.Thread(target = coimat.ScanID)
thread_step = threading.Thread(target = coimat.WaitStep)
thread_processing = threading.Thread(target = coimat.processing)
thread_maintainance = threading.Thread(target = coimat.maintanance)

thread_scan.start()
thread_step.start()
thread_processing.start()
thread_maintainance.start()

    


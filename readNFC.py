import nfc

class scanning():

        def __init__(self):
                self.idm = ""
        
        def on_startup(self,targets):
                #print("on_startup()")
                return targets
                
        def on_connect(self,tag):
                #print("Tag: {}".format(tag))
                #print("Tag type: {}".format(tag.type))
                #print '\n'.join(tag.dump())
                self.idm = tag.idm.hex()
                
                if tag.ndef:
                        print (tag.ndef.message.pretty())

        def on_release(self,tag):
                #print("on_release()")
                if tag.ndef:
                        print(tag.ndef.message.pretty())
        
        def exe_scan(self):
                try:
                        clf = nfc.ContactlessFrontend('usb')
                        if clf:
                                #print("Clf: {}".format(clf))

                                clf.connect(rdwr={
                                        'on-startup': self.on_startup,
                                        'on-connect': self.on_connect,
                                        'on-release': self.on_release
                                })
                        clf.close()
                
                except:
                        clf.close()


from machine import Timer
from time import sleep_ms
import ubluetooth

class Beacon1():
    def __init__(self, name):
        
        
        self.timer1 = Timer(0)
        self.name = name
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self.ble_irq)
        self.advertiser()
     
    def connected(self):
        self.timer1.deinit()
    

    def ble_irq(self, event, data):
        global ble_msg
        
        if event == 1:
            
            self.connected()
            print("connected")
            
    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)
        print(adv_data)
        print("\r\n")


ble = Beacon1("Beacon1_ESP32")
     

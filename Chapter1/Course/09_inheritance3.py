class Phone:
    serial_number = None
    producer = None

    def call_by_5g(self):
        print("5g calls.")

class NFCReader:
    nfc_type = "Fifth Generation"
    producer = "HM"

    def read_cardd(self):
        print("Read NFC cards.")

    def write_cards(self):
        print("Write NFC cards.")

class RemoteControl:
    rc_type = "IR remote control"

    def control(self):
        print("Infrared remote control opening.")

class MyPhone(Phone, NFCReader, RemoteControl):
    pass


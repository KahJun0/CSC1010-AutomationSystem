import time

import SimpleMFRC522
import MQTT_Publisher


class RFIDReader:

    def __init__(self):
        self.reader = SimpleMFRC522.SimpleMFRC522()
        self.publisher = MQTT_Publisher.MQTTPublisher('192.168.86.234', 'has/door', 'RFID_Reader_Ent_1')

    def read_data(self):
        id, text = self.reader.read()
        print(id, text)
        if "Test" in text:
            self.publisher.publish('open')
        return id, text

    def run(self):
        while True:
            self.read_data()
            time.sleep(1)

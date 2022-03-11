import sys

import servo_control
import rfid_controls
import MQTT_Subscriber
import threading

if __name__ == '__main__':
    MQTTSub = MQTT_Subscriber.MQTTSubscriber('has/system-controller')
    RFIDRead = rfid_controls.RFIDReader()
    servo_control = servo_control.GroveServo(int(sys.argv[1]))
    MQTT_Thread = threading.Thread(target=MQTTSub.run, args=(servo_control,), daemon=True)
    RFID_Thread = threading.Thread(target=RFIDRead.run, args=(), daemon=True)
    MQTT_Thread.start()
    RFID_Thread.start()
    MQTT_Thread.join()
    RFID_Thread.join()
    print("Exiting")

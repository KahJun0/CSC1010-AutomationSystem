from paho.mqtt import client as mqtt_client


class MQTTPublisher:

    def __init__(self, broker_ip, topic, cid):
        self.broker = broker_ip
        self.port = 1883
        self.topic = topic
        self.client_id = cid
        self.connect_mqtt()

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self.client = mqtt_client.Client(self.client_id)
        self.client.username_pw_set('endpoint1', 'Endp0int123')
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        return self.client

    def publish(self, msg):
        result = self.client.publish(self.topic, msg)
        status = result[0]
        if status == 0:
            print("Sent {0} to topic '{1}'".format(msg, self.topic))
        else:
            print("Failed to send message to topic {0}".format(self.topic))

    def run(self):
        self.client.loop_start()


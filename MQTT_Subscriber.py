from paho.mqtt import client as mqtt_client


class MQTTSubscriber:

    def __init__(self, cid):
        self.broker = '192.168.86.234'
        self.port = 1883
        self.topic = 'has/door'
        self.client_id = cid

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print('Connected')
            else:
                print('Error connection {0}'.format(rc))

        client = mqtt_client.Client(self.client_id)
        client.username_pw_set('server', 'P@ssw0rd123')
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client, servo_obj):
        def on_message(client, userdata, msg):
            print("Received {0} from {1} topic".format(msg.payload.decode(), msg.topic))
            if msg.topic == 'has/door':
                if msg.payload.decode() == 'open':
                    servo_obj.open()
                elif msg.payload.decode() == 'close':
                    servo_obj.close()
        client.subscribe(self.topic)
        client.on_message = on_message

    def run(self, servo_obj):
        client = self.connect_mqtt()
        self.subscribe(client, servo_obj)
        client.loop_forever()



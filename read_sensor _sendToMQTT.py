import paho.mqtt.client as mqtt
import time


MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_TOPIC_TEMP = "sensor/aht10/temperature"
MQTT_TOPIC_HUMID = "sensor/aht10/humidity"


TEMP_PATH = "/sys/bus/i2c/devices/i2c-1/1-0038/hwmon/hwmon2/temp1_input"
HUMID_PATH = "/sys/bus/i2c/devices/i2c-1/1-0038/hwmon/hwmon2/humidity1_input"


def read_sensor_data():
    try:
        with open(TEMP_PATH, "r") as temp_file:
            temperature = int(temp_file.read().strip()) / 1000.0
        with open(HUMID_PATH, "r") as humid_file:
            humidity = int(humid_file.read().strip()) / 1000.0
        return temperature, humidity
    except FileNotFoundError:
        print("Sensor data files not found!")
        return None, None

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
 
        temperature, humidity = read_sensor_data()
        if temperature is not None and humidity is not None:
            print(f"Temperature: {temperature}℃, Humidity: {humidity}%")

        client.publish(MQTT_TOPIC_TEMP, temperature)
        client.publish(MQTT_TOPIC_HUMID, humidity)

        time.sleep(10)
except KeyboardInterrupt:
    print("Script interrupted. Disconnecting MQTT client...")

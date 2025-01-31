# IoT Project: Temperature Acquisition and Transmission with Raspberry Pi & MQTT

## Project Overview

This project is designed to acquire temperature and humidity data using an AHT10 sensor connected to a Raspberry Pi 4. The data is then transmitted in real-time to an MQTT broker for remote monitoring.

## Features

- Reads temperature and humidity data from the AHT10 sensor via I2C.
- Publishes the data to an MQTT broker for real-time monitoring.
- Utilizes Python for data acquisition and transmission.
- Uses Bash scripts for initializing the I2C module and sensor setup and execute the code python.

## Technologies Used

- Raspberry Pi 4 running Linux
- AHT10 Sensor (I2C)
- MQTT Protocol (Mosquitto Broker)
- Bash & Python

## Installation and Setup

### Prerequisites

- Raspberry Pi with Raspbian installed
- AHT10 sensor connected via I2C
- Mosquitto MQTT broker installed
- Python3 and required dependencies

### Setup Instructions

   Navigate to `Interfacing Options > I2C` and enable it.


3. **Clone the repository:**

  
   https://github.com/Karim-Sahnoun117/Data-send-MQTT-Raspberry-Pi-4.git
  
   

4. **Run the shell script:**

   ./init_aht10 &execute py


## Contributing

Contributions are welcome. Feel free to submit issues or pull requests.


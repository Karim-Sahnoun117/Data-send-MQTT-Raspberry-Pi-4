#chargement des modules i2c et aht10
echo "Loading I2C and AHT10 modules..."

    sudo modprobe i2c-dev

    sudo modprobe aht10


#parcourir i2c device
echo "Configuring AHT10 device on I2C bus..."
if [ ! -d "/sys/bus/i2c/devices/i2c-1" ]; then
  echo "I2C bus not found! Exiting..."
  exit 1
fi

echo "Adding AHT10 device at 0x38..."
echo "aht10 0x38" | sudo tee /sys/bus/i2c/devices/i2c-1/new_device


if [ ! -d "/sys/bus/i2c/devices/i2c-1/1-0038" ]; then
  echo "Failed to initialize AHT10 device. Exiting..."
  exit 1
fi
echo "AHT10 device initialized successfully."
#le repertoir de python
SCRIPT_PYTHON="/path/to/your_script.py"
if [ -f "$SCRIPT_PYTHON" ]; then
  echo "Running Python script to read AHT10 data and send to MQTT..."
  python3 "$SCRIPT_PYTHON"
else
  echo "Python script not found at $SCRIPT_PYTHON. Exiting..."
  exit 1
fi

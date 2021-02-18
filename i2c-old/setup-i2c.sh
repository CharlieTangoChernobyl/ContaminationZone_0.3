#/bin/bash

# Strips device-type from hostname (only works on resin.io base images)
DEVICE_TYPE=${HOSTNAME%-*}
I2C_BUS=0 # Default i2c bus number
	modprobe i2c-dev
	export I2C_BUS=1
echo "detected $DEVICE_TYPE"

#Starts our sensor read script.
python src/sensor.py

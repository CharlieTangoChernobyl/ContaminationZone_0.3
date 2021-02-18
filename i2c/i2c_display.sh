#!/bin/bash

# Set LCD driver parameters
sed -i "s/I2C_BUS/`echo $I2C_BUS`/g" /sbin/I2C_LCD_driver.py
sed -i "s/I2C_ADDRESS/`echo $I2C_ADDRESS`/g" /sbin/I2C_LCD_driver.py

# Display text in LCD
python /sbin/i2c_display.py

FROM resin/rpi-raspbian:stretch-20180214

MAINTAINER Nicolas Singh <nicolas.singh@gmail.com>

# Download required software
RUN apt-get update -y && apt-get -y install i2c-tools python python-smbus

# Set up I2C driver variables
ENV I2C_BUS 1
ENV I2C_ADDRESS 20

# Set up I2C default text
RUN mkdir -p /tmp/textRows
COPY row1.txt /tmp/textRows/row1.txt
COPY row2.txt /tmp/textRows/row2.txt
VOLUME /tmp/textRows

# Copy I2C Library and Python script
COPY I2C_LCD_driver.py /sbin/I2C_LCD_driver.py
COPY i2c_display.py /sbin/i2c_display.py

# Execute I2C display script
COPY i2c_display.sh /sbin/i2c_display.sh
RUN chmod +x /sbin/i2c_display.sh
CMD i2c_display.sh

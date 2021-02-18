[![pipeline status](https://gitlab.com/nicosingh/rpi-i2cdisplay/badges/master/pipeline.svg)](https://gitlab.com/nicosingh/rpi-i2cdisplay/commits/master) [![Docker Pulls](https://img.shields.io/docker/pulls/nicosingh/rpi-i2cdisplay.svg)](https://hub.docker.com/r/nicosingh/rpi-i2cdisplay/)

Docker image of Raspbian prepared to display messages in a 1602A screen using I2C bus.

## Preparing image execution

Before anything, we have to enable I2C interface in our raspberry pi. This can be done in raspy-config > Advanced Settings > I2C Enable/Disable > choose "yes".

Then, we have to know two values related to our LCD screen:

1. **I2C Bus**: **"1"** (for original raspberry pi) or **"2"** (for raspberry pi revision 2 or 3)
2. **I2C Address**: I2C connected device address can be discovered with the following command: ```i2cdetect -y 1```.

Finally, we have to create a folder in our host filesystem to host two files: ```row1.txt``` and ```row2.txt```, to host the plaintext messages to be displayed in our screen. Remember this path name.

## How to use this Docker image?

Having I2C interface enabled in our raspberry pi and knowing I2C bus and address, we can execute our Docker image issuing something like:

```docker run -d --restart=always --privileged -e I2C_BUS=1 -e I2C_ADDRESS=20 -v /tmp/lcdvolume:/tmp/textRows nicosingh/rpi-i2cdisplay```

Where:

```-d``` (optional): Is recommended to run this container as a daemon

```--restart=always``` (optional): Is recommended to restart our container when it goes down (ie. by a system reboot).

```--privileged``` (required): Is required to use GPIO ports and Python SMBUS libraries in our image.

```-e I2C_BUS``` (required): Is our LCD I2C Bus number (1 or 2).

```-e I2C_ADDRESS``` (required): Is our LCD I2C Address.

```-v my_lcd_text:/tmp/textRows``` (optional): Means we are mounting our local folder my_lcd_text into our container. This folder is in our docker host and contains row1.txt and row2.txt files.

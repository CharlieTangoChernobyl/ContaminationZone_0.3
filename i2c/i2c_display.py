# Use I2C python driver
import I2C_LCD_driver
import time
import subprocess

# Initialise screen
mylcd = I2C_LCD_driver.lcd()
screen_size = 16

# Push text into LCD rows, forever
while True:
  message_1 = open('/tmp/textRows/row1.txt').read()
  message_1 = message_1[:-1]
  message_2 = open('/tmp/textRows/row2.txt').read()
  message_2 = message_2[:-1]
  mylcd.lcd_display_string(message_1, 1, 0)
  mylcd.lcd_display_string(message_2, 2, 0)

  if(len(message_1) > screen_size):
    for it in range(0,len(message_1)-screen_size+1):
      mylcd.lcd_display_string(message_1[it:], 1, 0)
      time.sleep(0.6)
    time.sleep(1)
    for it in range(len(message_1)-screen_size,-1,-1):
      mylcd.lcd_display_string(message_1[it:], 1, 0)
      time.sleep(0.6)
  else:
      for it in range(len(message_1),screen_size):
        message_1 = message_1 + " "
      mylcd.lcd_display_string(message_1, 1, 0)
  if(len(message_2) > screen_size):
    for it in range(0,len(message_2)-screen_size+1):
      mylcd.lcd_display_string(message_2[it:], 2, 0)
      time.sleep(0.6)
    time.sleep(1)
    for it in range(len(message_2)-screen_size,-1,-1):
      mylcd.lcd_display_string(message_2[it:], 2, 0)
      time.sleep(0.6)
  else:
      for it in range(len(message_2),screen_size):
        message_2 = message_2 + " "
      mylcd.lcd_display_string(message_2, 2, 0)
  time.sleep(1)


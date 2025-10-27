"""
This project will initialize the display using displayio and draw a solid black
background, then read the BME680 data and write it to the TFT display in colors
according to the thresholds defined (see lines 72-98). It also shows on NeoPixels 
which range each measurement is in.

NeoPixel Top Left: Temperature
NeoPixel Top Right: Humidity
NeoPixel Bottom Left: Barometric Pressure
NeoPixel Bottom Right: Gas

Workshop attendees' tasks:
   - Find the elevation of your location
   - Determine appropriate thresholds for temperature, humidity, barometric pressure, and gas
   - Define any extra text label colors you want to use
   - Set display positions for text labels using (X,Y) coordinates
   - Obtain the temperature, humidity, barometric pressure and gas measurements from the BME680 sensor
   - Implement barometric pressure adjustment based on the international Standard Atmosphere
   - Use f-strings to create text labels for LCD
"""

import board
import adafruit_bme680
import time
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from fourwire import FourWire
import time
import digitalio
import microcontroller
from micropython import const
import math
import neopixel

def DisableAutoReload():
   import supervisor
   supervisor.runtime.autoreload = False
   print("Autoreload disabled. After saving code, use CTRL-D, then CTRL-C to run your code")

# Uncomment this if you have problems with your editor autosaving causing frequent restarts   
# DisableAutoReload()

# Change this boolean to False to disable debug print statements
Debug = True

# NeoPixel RGB Colors are defined as 8-bit values as follows: 0xRRGGBB or (RR, GG, BB)
NEOPIXEL_RED = (255, 0, 0)
NEOPIXEL_YELLOW = (255, 150, 0)
NEOPIXEL_GREEN = (0, 255, 0)
NEOPIXEL_BLUE = (0, 0, 255)
NEOPIXEL_ORANGE = (255, 64, 0)
NEOPIXEL_OFF = (0, 0, 0)
# Add any other colors you would like to use

pixel_pin = board.NEOPIXEL
# There are 5 NeoPixels total: 1 on the dev board and 4 on the ruler
num_pixels = 5
# Initialize the NeoPixels: Adjust brightness as required
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

# Turn off NeoPixels in case they were set on by a previous program
pixels.fill(NEOPIXEL_OFF)
pixels.show()

# Task: Find the Elevation for your location. Set CONST_ELEVATION
# See docs on how to set a const: https://docs.circuitpython.org/en/latest/shared-bindings/micropython/index.html
# Your code here:
CONST_ELEVATION = 

# Task: Set temperature thresholds for your comfort level using constants.
# NOTE: Temperatures are set in degrees Celcius!
# Your code here:
CONST_TEMP_LOW = 
CONST_TEMP_MED = 
CONST_TEMP_HI = 

# Task: Set humidity thresholds for your comfort level using constants
# Your code here:
CONST_HUMID_LOW = 
CONST_HUMID_MED = 
CONST_HUMID_HI = 

# Task: Set barometric pressure thresholds using constants
# NOTE: Pressure is set in milliBar (mB) !
# Your code here:
CONST_PRESS_LOW =      # Low pressure
CONST_PRESS_MED =      # Standard pressure
CONST_PRESS_HI =       # High pressure

# Task: Set Gas thresholds
# High resistance (Ohms) indicates better air quality - adjust for your comfort & location using constants
# Note: Gas measurements can range from a few thousand to over 100,000. This measurment has NO units.
# Your code here:
CONST_GAS_LOW = 
CONST_GAS_MED = 
CONST_GAS_HI = 

CONST_TEXT_COLOR_BLUE = 0x0000FF
# Task: Set text label colors - display uses 8-bit values for RGB: 0xRRGGBB or (RR, GG, BB)
CONST_TEXT_COLOR_GREEN = 
CONST_TEXT_COLOR_RED = 
CONST_TEXT_COLOR_PURPLE = 
CONST_TEXT_COLOR_YELLOW = 
# Add any other colors you would like to use

# Create instance of I2C object & BME680 object
i2c = board.I2C()
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

if Debug:
    print("Create pin called 'backlight' for LCD backlight on PA06")
backlight = digitalio.DigitalInOut(microcontroller.pin.PA06)
backlight.direction = digitalio.Direction.OUTPUT

# Release any resources currently in use for the displays
if Debug:
    print("Release displays")
displayio.release_displays()

if Debug:
    print("Create SPI Object for display")
spi = board.LCD_SPI()
tft_cs = board.LCD_CS
tft_dc = board.D4

if Debug:
    print("Turn TFT Backlight On")
# Backlight is Active LOW
backlight.value = False

DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 135

if Debug:
    print("Create DisplayBus")
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    display_bus, rotation=90, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rowstart=40, colstart=53
)

# Set text, font, and color and create four text labels
# Label text is placeholder text commonly used in publishing for viewing layouts
font = bitmap_font.load_font("/Helvetica-Bold-16.bdf")
text_area1 = label.Label(font, text="Lorem ipsum dolor sit amet", color=CONST_TEXT_COLOR_PURPLE)
text_area2 = label.Label(font, text="consectetur adipiscing elit", color=CONST_TEXT_COLOR_BLUE)
text_area3 = label.Label(font, text="sed do eiusmod tempor incididunt ut", color=CONST_TEXT_COLOR_RED)
text_area4 = label.Label(font, text="labore et dolore magna aliqua", color=CONST_TEXT_COLOR_GREEN)

# Set positions for the labels
# Task: Set position for text_area1. Hint: you will need to use both x and y coordinates
# Your code here: 
text_area1.x = 
text_area1.y = 

# The nested group's items can have their own coordinates relative to the nested group
# Task: Set position for text_area2. Hint: you will need to use x and y coordinates
# Your code here: 
text_area2.x = 
text_area2.y = 

# Task: Set position for text_area3. Hint: you will need to use x and y coordinates
# Your code here: 
text_area3.x = 
text_area3.y = 

# Task: Set position for text_area4. Hint: you will need to use x and y coordinates
# Your code here: 
text_area4.x = 
text_area4.y = 

# Create the parent group
parent_group = displayio.Group()

# Add the first label directly to the parent group
parent_group.append(text_area1)

# Create 3 nested groups for the other 3 labels
nested_group1 = displayio.Group()
nested_group1.append(text_area2)

nested_group2 = displayio.Group()
nested_group2.append(text_area3)

nested_group3 = displayio.Group()
nested_group3.append(text_area4)

# Append the nested groups to the parent group
parent_group.append(nested_group1)
parent_group.append(nested_group2)
parent_group.append(nested_group3)

# Show the parent group on the display
display.root_group = parent_group

# Show labels for 2 seconds
time.sleep(2)

# Main loop
while True:
    # Pressure sensors return absolute pressure. However atmospheric
    # pressure changes with elevation. In weather reports, the pressure
    # is adjusted to an equivalent seal level pressure. This is so that 
    # pressure's in different places can be directly compared.

    # Task: Adjust sensor pressure reading for our elevation according
    # to the international Standard Atmosphere
    # Note: Atmospheric pressure changes with elevation.
    # The following equation takes the absolute pressure and returns the 
    # equivalent pressure at sea level to give accurate readings
    # in accordance with the international Standard Atmosphere.
    # The equation is: P0 = P1 (1 - (0.0065h/ (T + 0.0065h + 273.15))^(-5.257)
    # where:   P0 = calculated mean sea level pressure (hPa)
    # P1 = actual measured pressure (hectoPascals [hPa] or milliBar [mB])
    # h = elevation of your location (metres)
    # T = temp is degrees Celcius

    # Task: Get the temperature from the BME680
    # Hint: See Adafruit's documentation: https://learn.adafruit.com/adafruit-bme680-humidity-temperature-barometic-pressure-voc-gas/python-circuitpython
    # Alternatively you can use the API reference: https://docs.circuitpython.org/projects/bme680/en/latest/
    # Your code here:
    temp = 

    # Task: Now you need to adjust the pressure reading for your Elevation. The equation (see line 204) consists of a Mantissa raised to a Power.
    # First calculate the mantissa.
    # Your code here:
    mantissa =
    
    # Task: Raise the mantissa to the required power to return the adjustment- Hint: see the Python math library 
    adjustment = 
    if Debug:
        print("Adjustment: ", adjustment)

    # Task: Apply the adjustment
    # Your code here:
    pressure_adjusted = 
    if Debug:
        print("Pressure adjusted: ", pressure_adjusted)
    # Don't forget to compare against your local weather service to see if the adjusted pressure makes sense!
    
    # Task: Create the text strings for both the LCD and terminal
    # Hint: CircuitPython supports f-strings (formatted string literals)
    # Your code here:
    str1 = 
    str2 = 
    str3 = 
    str4 = 
    
    if Debug:
        print(str1)
        print(str2)
        print(str3)
        print(str4, "\n")
        	
    # set temperature text color according to thresholds
    if sensor.temperature <= CONST_TEMP_LOW:
        text_area1.color = CONST_TEXT_COLOR_BLUE
        # Pixel 3 is top left
        pixels[3] = NEOPIXEL_BLUE
        pixels.show()
    elif (sensor.temperature > CONST_TEMP_LOW and sensor.temperature <= CONST_TEMP_MED):
        text_area1.color = CONST_TEXT_COLOR_GREEN
        # Pixel 3 is top left
        pixels[3] = NEOPIXEL_GREEN
        pixels.show()
    elif (sensor.temperature > CONST_TEMP_MED and sensor.temperature <= CONST_TEMP_HI):
        text_area1.color = CONST_TEXT_COLOR_YELLOW
        # Pixel 3 is top left
        pixels[3] = NEOPIXEL_ORANGE
        pixels.show()
    else:
        text_area1.color = CONST_TEXT_COLOR_RED
        # Pixel 3 is top left
        pixels[3] = NEOPIXEL_RED
        pixels.show()

    # set humidity text color according to thresholds
    if sensor.humidity <= CONST_HUMID_LOW:
        text_area2.color = CONST_TEXT_COLOR_BLUE
        # Pixel 2 is top right
        pixels[2] = NEOPIXEL_BLUE
        pixels.show()
    elif (sensor.humidity > CONST_HUMID_LOW and sensor.humidity <= CONST_HUMID_MED):
        text_area2.color = CONST_TEXT_COLOR_GREEN
        # Pixel 2 is top right
        pixels[2] = NEOPIXEL_GREEN
        pixels.show()
    elif (sensor.humidity > CONST_HUMID_MED and sensor.humidity <= CONST_HUMID_HI):
        text_area2.color = CONST_TEXT_COLOR_YELLOW
        # Pixel 2 is top right
        pixels[2] = NEOPIXEL_ORANGE
        pixels.show()
    else:
        text_area2.color = CONST_TEXT_COLOR_RED
        # Pixel 2 is top right
        pixels[2] = NEOPIXEL_RED
        pixels.show()

    # set pressure text color according to thresholds
    if pressure_adjusted <= CONST_PRESS_LOW:
        text_area3.color = CONST_TEXT_COLOR_BLUE
        # Pixel 4 is bottom left
        pixels[4] = NEOPIXEL_BLUE
        pixels.show()
    elif (pressure_adjusted > CONST_PRESS_LOW and pressure_adjusted <= CONST_PRESS_MED):
        text_area3.color = CONST_TEXT_COLOR_GREEN
        # Pixel 4 is bottom left
        pixels[4] = NEOPIXEL_GREEN
        pixels.show()
    elif (pressure_adjusted > CONST_PRESS_MED and pressure_adjusted <= CONST_PRESS_HI):
        text_area3.color = CONST_TEXT_COLOR_YELLOW
        # Pixel 4 is bottom left
        pixels[4] = NEOPIXEL_ORANGE
        pixels.show()
    else:
        text_area3.color = CONST_TEXT_COLOR_RED
        # Pixel 4 is bottom left
        pixels[4] = NEOPIXEL_RED
        pixels.show()

    # set gas text color according to thresholds
    if sensor.gas <= CONST_GAS_LOW:
        text_area4.color = CONST_TEXT_COLOR_RED
        # Pixel 1 is bottom right
        pixels[1] = NEOPIXEL_RED
        pixels.show()
    elif (sensor.gas > CONST_GAS_LOW and sensor.gas <= CONST_GAS_MED):
        text_area4.color = CONST_TEXT_COLOR_YELLOW
        # Pixel 1 is bottom right
        pixels[1] = NEOPIXEL_ORANGE
        pixels.show()
    elif (sensor.gas > CONST_GAS_LOW and sensor.gas <= CONST_GAS_MED):
        text_area4.color = CONST_TEXT_COLOR_GREEN
        # Pixel 1 is bottom right
        pixels[1] = NEOPIXEL_GREEN
        pixels.show()
    else:
        text_area4.color = CONST_TEXT_COLOR_BLUE
        # Pixel 1 is bottom right
        pixels[1] = NEOPIXEL_BLUE
        pixels.show()

    # Set the display text areas to the created strings
    text_area1.text = str1
    text_area2.text = str2
    text_area3.text = str3
    text_area4.text = str4

    # Adjust this time between readings as required 
    time.sleep(1)

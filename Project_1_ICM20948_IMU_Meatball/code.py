
"""
This project will initialize the display using displayio and draw a solid black
background, a Microchip "Meatball" logo, and move the logo around the screen from the IMU data.

Workshop attendees' tasks:
    Determine whether to use accelerometer or gyroscope
    Read X,Y,Z from IMU
    Determine which 2 IMU values to use
    Cast IMU float output to int for display coordinates
    Move Meatball according to IMU measurements
    Adjust X & Y Drift variables to keep Meatball stable when Ruler is on a flat level surface
    Figure out how to keep Meatball within confines of display
"""
import time
import board
import adafruit_icm20x
import displayio
import adafruit_imageload
import digitalio
import microcontroller
import neopixel
from fourwire import FourWire
from adafruit_st7789 import ST7789

def DisableAutoReload():
    import supervisor
    supervisor.runtime.autoreload = False
    print("Auto-reload is currently disabled.")
    print("After saving your code, press the RESET button.")
    
# uncomment this if auto-reload is causing issues from your editor     
# DisableAutoReload()

# Change this to True to show debug print statements
Debug = False

# In case previous program turned on NeoPixels, this will turn them all off
pixel_pin = board.NEOPIXEL
num_pixels = 5
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
pixels.fill(0x000000)
pixels.show()

# Initialize I2C object for IMU
i2c = board.I2C()  # uses board.SCL and board.SDA pins
# Try default ICM20948 address. If not found try alternate address 0x68.
try:
    icm = adafruit_icm20x.ICM20948(i2c, 0x69)
except:
    print("No ICM20948 found at default address 0x69. Trying alternate address 0x68.")
    icm = adafruit_icm20x.ICM20948(i2c, 0x68)

# Release any resources currently in use for the displays
if Debug:
    print("Release displays")
displayio.release_displays()
# Configure LCD backlight
if Debug:
    print("Create pin called 'backlight' for LCD backlight on PA06")
backlight = digitalio.DigitalInOut(microcontroller.pin.PA06)
backlight.direction = digitalio.Direction.OUTPUT
if Debug:
    print("Turn TFT Backlight On")
# LCD Backlight is Active LOW    
backlight.value = False

# Initialize LCD display
if Debug:
    print("Create SPI Object for display")
spi = board.LCD_SPI()
tft_cs = board.LCD_CS
tft_dc = board.D4

# Configure display size
DISPLAY_WIDTH = 240
DISPLAY_HEIGHT = 135
# Set logo size - must match logo size being used!
LOGO_WIDTH = 32
LOGO_HEIGHT = 30

# Create displaybus object for LCD display
if Debug:
    print("Create DisplayBus")
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    display_bus, rotation=90, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rowstart=40, colstart=53
)

# Load the sprite sheet (bitmap)
if Debug:
    print("Load Sprite sheet")
sprite_sheet, palette = adafruit_imageload.load("/Meatball_32x30_16color.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create a sprite (tilegrid)
if Debug:
    print("Create Sprite")
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width=1,
                            height=1,
                            tile_width=LOGO_WIDTH,
                            tile_height=LOGO_HEIGHT)

# Create a Group to hold the sprite
if Debug:
    print("Create Group to hold Sprite")
group = displayio.Group(scale=1)

# Add the sprite to the Group
if Debug:
    print("Append Sprite to Group")
group.append(sprite)

# Add the Group to the Display
if Debug:
    print("Add Group to Display")
display.root_group = group

# Explanation of variables used:
# group.x and group.y are the location coordinates on the display of the Meatball logo
# X_pos and Y_pos are the measurements from the IMU

# Set sprite initial location
if Debug:
    print("Set Sprite Initial Location")
group.x = 150
group.y = 70

X_pos = 150
Y_pos = 70

# User to adjust drift values to keep Meatball stable when on flat level surface
drift_X = 0.0
drift_Y = 0.0

while True:
    # https://learn.adafruit.com/adafruit-tdk-invensense-icm-20948-9-dof-imu/python-circuitpython  
    # Read the Docs: https://docs.circuitpython.org/projects/icm20x/en/latest/api.html

    # Task: Decide whether to use accelerometer or gyroscope data from IMU
    # Task: Get X,Y,Z data from IMU

    # Print IMU data as sanity check
    if Debug:
        print("X: {:.2f}".format(X))
        print("Y: {:.2f}".format(Y))
        print("Z: {:.2f}".format(Z))
        print("")

    # Task: Display has only 2 axes, but IMU has 3 (X,Y,Z): decide which 2 to use!
    # Task: IMU data is of type float. Display position uses type int. Cast float to int.
    # Task: Move Meatball according to IMU data & drift_X / drift_Y adjustments.

    # Your code here: Set X_position (X_pos) using the IMU data and drift_X variables
    # Your code here: Set Y_position (Y_pos) using the IMU data and drift_Y variables

    # Task: Figure out how to stop Meatball from drifting off screen
    if X_pos >= DISPLAY_WIDTH - LOGO_WIDTH:     
        # Your code here to prevent Meatball from moving off display in positive X-axis. 
        # Use group.x to set Meatball position in X-axis
        # Don't forget to update X_pos variable as well!

    else:
        group.x = X_pos                 

    if X_pos <= 0:                      
        # Your code here to prevent Meatball from moving off display in negative X-axis.
        # Use group.x to set Meatball position in X-axis
        # Don't forget to update X_pos variable as well!
                     
    else:           
        group.x = X_pos                 

    if Y_pos >= DISPLAY_HEIGHT - LOGO_HEIGHT:   
        # Your code here to prevent Meatball from moving off display in positive Y-axis
        # Use group.y to set Meatball position in Y-axis
        # Don't forget to update Y_pos variable as well!

    else:
        group.y = Y_pos

    if Y_pos <= 0:
        # Your code here to prevent Meatball from moving off display in negative Y-axis
        # Use group.x to set Meatball position in X-axis
        # Don't forget to update X_pos variable as well!
        group.y = 0
        Y_pos = 0
    else:
        group.y = Y_pos

    # Adjust this for Meatball responsiveness to IMU
    # Smaller time = Meatball more responsive to movement
    time.sleep(0.02)








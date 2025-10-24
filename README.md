# Curiosity_CircuitPython_Workshop_Projects
Repo for partially completed code for students to complete in workshops.
The code is to used with the Microchip PyKit Explorer. This kit consists of a Curiosity CircuitPython dev board, a PyKit Ruler baseboard, an Adafruit BME680 QWIIC/STEMMA breakout, and an Adafruit APDS9960 QWIIC/STEMMA breakout.

More workshop projects will be added over time. To start there are 3 projects and 1 bonus project.

### Project 1: ICM20948 9-DoF IMU "Meatball"

This project uses the ICM20948 9-DoF IMU on the PyKit Ruler baseboard to move the Microchip logo known as the "Meatball" 
around the TFT display on the PyKit Ruler baseboard. Students have to read from the IMU and translate that into movement 
on the display.

### Project 2: BME680 Temperature/Humidity/Pressure/Gas
In this project the students read from the BME680 sensor 4 measurements: Temperature, Humidity, Barometric Pressure, and Gas. 
They then write those to the TFT display using colored labels that are triggered by thresholds. Students have to decide on the 
thresholds themselves. Students then write to the 4 NeoPixels on the PyKit Ruler baseboard, with each NeoPixel corresponding
to a given measurement.

### Project 3: APDS9960 Proximity/Gesture/Color
In this project the students utilize a state machine to switch between the 3 measurements (Proximity/Gesture/Color). In Proximity state, the students will output a tone via the DAC that is inversely 
proportional to the measured distance. 
In Gesture state, four Gestures are supported: Up, Down. Left, Right. Students will map a WAV file to each gesture.
In Color state, students will read the measured color, write its RGB components to the TFT display and reproduce the measured color using the 4 NeoPixels on the PyKit Ruler.

### Bonus project: Snake Game
In this project, students will modify the [Adafruit version of the Snake game (from the RP2350)](https://learn.adafruit.com/snake-game-on-metro-rp2350/) to use the TFT display on the PyKit Ruler.
Next they will then modify the project to use the ICM20948 IMU accelerometer as user input.
Then they will keep track of the "food" the snake eats and assign a score. They will also create a Game Over splash screen and flash the 4 NeoPixels when Game Over occurs.
Finally, they will use NVM to store the High Score.

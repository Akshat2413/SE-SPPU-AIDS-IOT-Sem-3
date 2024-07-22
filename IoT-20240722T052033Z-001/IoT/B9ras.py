import RPi.GPIO as GPIO
import time

# Define GPIO pins for RGB LED
RED_PIN = 17  # GPIO pin 17 (physical pin 11)
GREEN_PIN = 18  # GPIO pin 18 (physical pin 12)
BLUE_PIN = 22  # GPIO pin 22 (physical pin 15)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def rgb_color(red_value, green_value, blue_value):
    GPIO.output(RED_PIN, red_value)
    GPIO.output(GREEN_PIN, green_value)
    GPIO.output(BLUE_PIN, blue_value)

try:
    while True:
        red = int(input("Enter red value (0-255): "))
        green = int(input("Enter green value (0-255): "))
        blue = int(input("Enter blue value (0-255): "))

        red_normalized = 255 - red  # Reverse as Arduino code uses inverted logic
        green_normalized = 255 - green
        blue_normalized = 255 - blue

        rgb_color(red_normalized, green_normalized, blue_normalized)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()

import RPi.GPIO as GPIO
import time

# Set GPIO pins
OUTPUT_PIN = 17  # GPIO pin 17 (physical pin 11) for output
INPUT_PIN = 18   # GPIO pin 18 (physical pin 12) for input

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    GPIO.setup(INPUT_PIN, GPIO.IN)
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)  # Set output pin initially high

def loop():
    try:
        while True:
            if GPIO.input(INPUT_PIN) == GPIO.HIGH:
                GPIO.output(OUTPUT_PIN, GPIO.HIGH)
            else:
                GPIO.output(OUTPUT_PIN, GPIO.LOW)
            time.sleep(0.1)  # Adjust delay as needed
    except KeyboardInterrupt:
        pass

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except Exception as e:
        print("Error:", e)
    finally:
        cleanup()

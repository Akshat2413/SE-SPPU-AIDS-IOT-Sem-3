import RPi.GPIO as GPIO
import time

# Set GPIO pins
BUZZER_PIN = 17  # GPIO pin 17 (physical pin 11)
KNOCK_PIN = 18  # GPIO pin 18 (physical pin 12)

# Set threshold for knock detection
THRESHOLD = 400

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(KNOCK_PIN, GPIO.IN)

def loop():
    while True:
        sensor_reading = GPIO.input(KNOCK_PIN)
        if sensor_reading == GPIO.HIGH:  # Detect knock
            tone_sequence()
        time.sleep(0.1)  # Adjust delay as needed

def tone_sequence():
    frequencies = [261, 293, 329, 349, 392]  # Frequencies for D, E, F, G notes
    for frequency in frequencies:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        buzzer = GPIO.PWM(BUZZER_PIN, frequency)
        buzzer.start(50)  # Duty cycle
        time.sleep(0.2)
        buzzer.stop()
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()

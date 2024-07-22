import Adafruit_DHT
import time

# Set up the GPIO pin for DHT11
DHT_PIN = 4  # GPIO pin 4

def main():
    # Main loop to read and print sensor data
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f'Temperature: {temperature:.1f} °C, Humidity: {humidity:.1f}%')
        else:
            print('Failed to retrieve data from sensor')
        time.sleep(2)  # Delay between readings

if __name__ == '__main__':
    main()

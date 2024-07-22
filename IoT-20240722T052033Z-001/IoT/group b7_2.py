import time
from gpiozero import LED
led1 = LED(7)
led2 = LED(22)
led3 = LED(23)
led4 = LED(25)

led1.on()
led2.on()
led3.on()
led4.on()
        

key=input("Enter Character")
print(key)

while True:
    time.sleep(0.2)
    key=input("Enter Character")
    print (key)
    if key=='g' or key=='G':
        led1.off()
        led2.on()
        led3.on()
        led4.on()
    elif key=='r' or key=='R':
        led1.on()
        led2.off()
        led3.on()
        led4.on()
    elif key=='y' or key=='Y':
        led1.on()
        led2.on()
        led3.off()
        led4.on()
    else :
        led1.on()
        led2.on()
        led3.on()
        led4.on()


      


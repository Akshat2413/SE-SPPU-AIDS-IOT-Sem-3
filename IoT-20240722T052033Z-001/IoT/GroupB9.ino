int red_light_pin= 5;
int green_light_pin = 6;
int blue_light_pin = 3;

unsigned int red,green,blue;

void setup() {
  pinMode(red_light_pin, OUTPUT);
  pinMode(green_light_pin, OUTPUT);
  pinMode(blue_light_pin, OUTPUT);
}

void loop() {
red = analogRead(A0); // reads the value from the specified analog pin present on the particular Arduino board and returns a number between 0 and 1023 that is proportional to the amount of voltage being applied to the pin.
red = (red/4);
green = analogRead(A2);
green = (green/4);
blue = analogRead(A3);
blue = (blue/4);  

  RGB_color(255-red, 255-green, 255-blue); // turning potentiometer will show change in color
  delay(1000);

 /*RGB_color(0, 255, 255); // Red (show by removing comments without turning
  delay(1000);
  RGB_color(255, 0, 255); // Green
  delay(1000);
  RGB_color(255, 255, 0); // Blue
  delay(1000);
  RGB_color(0, 0, 125); // Raspberry
  delay(1000);
  RGB_color(255, 0, 0); // Cyan
  delay(1000);
  RGB_color(0, 255, 0); // Magenta
  delay(1000);
  RGB_color(0, 0, 255); // Yellow
  delay(1000);
  RGB_color(0, 0, 0); // White
  delay(1000);
  */
 
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value)
 {
  analogWrite(red_light_pin, red_light_value);
  analogWrite(green_light_pin, green_light_value);
  analogWrite(blue_light_pin, blue_light_value);
}

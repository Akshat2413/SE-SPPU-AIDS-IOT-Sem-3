
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);  // starts serial communication and the serial port is capable of transferring a maximum of 9600 bits per second
Serial.println("input the number"); //writes data to the serial port
}

void loop() {
  // put your main code here, to run repeatedly:

int input = Serial.parseInt();  // Looks for the next valid integer in the incoming serial. The function terminates if it times out
int inputSquared = sq(input);
Serial.println(int(inputSquared)); // show the difference between println and print
delay(500);
}

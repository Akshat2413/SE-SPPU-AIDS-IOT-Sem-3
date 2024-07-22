void setup() {
  // put your setup code here, to run once:
pinMode(4,OUTPUT);
pinMode(9,INPUT);
digitalWrite(4,HIGH);
}

void loop() {
 if(digitalRead(9)== 1)
    digitalWrite(4,HIGH);
 else
    digitalWrite(4,LOW);   
}

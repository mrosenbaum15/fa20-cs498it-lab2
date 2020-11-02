void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available() == 0) {
    //Serial.print("WiFi waiting");
  }
  
  
  //Serial.println("WiFi");
  Serial.println(Serial.read());

  delay(1000);
}


void setup(){  
     Serial.begin(9600); // baud rate to 9600
}

void loop(){

    /* code for sending just the air quality 
    *  acts as proof of concept that AQ gets sent to Pi... run serial_read.py on the Pi to see AQ
    */
    int airQuality;
    airQuality = analogRead(0); // read from pin A0    
    Serial.println(airQuality, DEC); // print numerical value from sensor        
  //  Serial.println(" PPM"); // unit of air quality
    delay(1000); // wait a second      

    /* code or sending air quality and number of devices from wifi module
     * this is what you'll eventually need
    int airQuality;
    airQuality = analogRead(0); // read from pin A0    
    
    if (Serial.available() > 0) {
      int total_devices = Serial.read(); // gets number of devices sent from End Xbee
      // Serial.print("Total Devices: "); // probably don't need to transmit this serially to rasp pi xbee
      // Might need to modify next two lines to determine how you want to send devices and AQ
      Serial.println(total_devices);
      Serial.println(airQuality, DEC); // print numerical value from sensor        
    }
    delay(1000); // wait a second
    */
}

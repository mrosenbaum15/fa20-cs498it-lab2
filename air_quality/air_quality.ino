
void setup(){  
     Serial.begin(9600); // baud rate to 9600
}

void loop(){

    /* code for sending just the air quality 
    *  acts as proof of concept that AQ gets sent to Pi... run serial_read.py on the Pi to see AQ
    */
//    int airQuality;
//    airQuality = analogRead(0); // read from pin A0    
//    Serial.println(airQuality, DEC); // print numerical value from sensor        
//  //  Serial.println(" PPM"); // unit of air quality
//    delay(1000); // wait a second      

    /* code or sending air quality and number of devices from wifi module
     * this is what you'll eventually need
     * */
     
    int airQuality;
    airQuality = analogRead(0); // read from pin A0    
    
    while (Serial.available() == 0 && Serial.read() != '\n') {
    }

    Serial.print(airQuality, DEC); // print numerical value from sensor
    Serial.println(" PPM"); // print numerical value from sensor           
    Serial.print(Serial.read());
    Serial.println(" devices"); // print numerical value from sensor             
    delay(1000); // wait a second
    
}

// ESP32-S3 raw ADC demonstration. Set a safe ADC pin for your board and use voltage conditioning.
const int TURBIDITY_PIN = 4;
void setup(){Serial.begin(115200);analogReadResolution(12);}
void loop(){Serial.printf("{\"source\":\"sensor\",\"turbidity_raw\":%d}\n",analogRead(TURBIDITY_PIN));delay(1000);}

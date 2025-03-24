void setup() {
    // 初始化串口通信
    Serial.begin(9600);
  }
  
  void loop() {
    for (int pin = A0; pin <= A6; pin++) {
        int value = analogRead(pin);
        Serial.print("Pin A");
        Serial.print(pin - A0);
        Serial.print(": ");
        Serial.println(value);
    }
    delay(1000);
  }
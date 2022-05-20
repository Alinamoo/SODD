#include <IRremote.h> // >v3.0.0
                                            
#define PIN_SEND 3

unsigned long long on = 0xFFA25D;
unsigned long long off = 0xFF629D;
unsigned long long red = 0xFF6897;
unsigned long long green = 0xFF9867;

void setup() {
  Serial.begin(9600);  // start serial for input
  Serial.setTimeout(0.05);

  IrSender.begin(PIN_SEND); // Initializes IR sender
  IrSender.sendNEC(on, 32);
}

void loop() {
  if (Serial.available()) {
    IrSender.sendNEC(green, 32);
  }
}

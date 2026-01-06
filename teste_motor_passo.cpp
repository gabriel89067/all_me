

#define STEP_PIN 3
#define DIR_PIN 2
#define TIME1 500
int TIME = 2100;
void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  
}

void loop() {
  // Sentido 1
  TIME = 2100;
  digitalWrite(DIR_PIN, HIGH);
  for (int i = 0; i < 200; i++) {
     TIME = TIME - 15;
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);
  }

  delay(100);
TIME = 2100;
  // Sentido oposto
  digitalWrite(DIR_PIN, LOW);
  for (int i = 0; i < 200; i++) {
    TIME = TIME - 15;
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);
  }

  delay(100);
}

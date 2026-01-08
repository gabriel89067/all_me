

#define STEP_PIN 3
#define DIR_PIN 2
#define TIME1 45000
int value = 1000;
int count = 0;
int TIME = 5500;
int conf = 0;
void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  
}

void loop() {
  // Sentido 1
  TIME = 9400;
  count = 0;
  digitalWrite(DIR_PIN, HIGH);
  for (int i = 0; i < 125; i++) {
     TIME = TIME - 40;
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);
    
  }
  while(count < value){
  digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);}


count = 0;
 
  delay(100);
TIME = 5500;
  // Sentido oposto
  digitalWrite(DIR_PIN, LOW);
  for (int i = 0; i < 500; i++) {
    TIME = TIME - 10;
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);
  }

 while(count < value){
  digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(TIME);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(TIME);}


  delay(100);
  
}

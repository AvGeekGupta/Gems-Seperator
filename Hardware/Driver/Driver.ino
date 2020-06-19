// Header files
#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Global Objects
Servo dropper1, dropper2;
LiquidCrystal_I2C lcd = LiquidCrystal_I2C(0x3F, 16, 2);

//Global Variables
int indicatorLight = 11;
int runningLight = 10;
int rbgRed = 9;
int rbgBlue = 8;
int rbgGreen = 7;
int buzzer = 6;
String output;

// Initial Setup Function
void setup() {
  dropper1.attach(13);
  dropper2.attach(12);
  pinMode(indicatorLight, OUTPUT);
  digitalWrite(indicatorLight, HIGH);
  pinMode(runningLight, OUTPUT);
  digitalWrite(runningLight, LOW);
  pinMode(rbgRed, OUTPUT);
  digitalWrite(rbgRed, HIGH);
  pinMode(rbgBlue, OUTPUT);
  digitalWrite(rbgBlue, HIGH);
  pinMode(rbgGreen, OUTPUT);
  digitalWrite(rbgGreen, HIGH);
  pinMode(buzzer, OUTPUT);
  digitalWrite(buzzer, LOW);
  lcd.init();
  lcd.begin(16, 2);
  lcd.backlight();
  Serial.begin(9600);
  lcd.setCursor(3, 0);
  lcd.print("Welcome to");
  lcd.setCursor(1, 1);
  lcd.print("Gems Seperator");
  dropper1.write(0);
  dropper2.write(25);
}

void loop() {
   while(!Serial.available());
   output = Serial.readStringUntil('\n');
   digitalWrite(runningLight, HIGH);
   lcd.clear();
   // Blue
   if (output == "1"){
    digitalWrite(rbgBlue, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(6, 1);
    lcd.print("Blue");
    dropper2.write(0);
    beep();
    digitalWrite(rbgBlue, HIGH);
   }
   // Brown
   else if (output == "2"){
    digitalWrite(rbgRed, LOW);
    digitalWrite(rbgBlue, LOW);
    digitalWrite(rbgGreen, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(6, 1);
    lcd.print("Brown");
    dropper2.write(10);
    beep();
    digitalWrite(rbgRed, HIGH);
    digitalWrite(rbgBlue, HIGH);
    digitalWrite(rbgGreen, HIGH);
   }
   // Green
   else if (output == "3"){
    digitalWrite(rbgGreen, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(6, 1);
    lcd.print("Green");
    dropper2.write(20);
    beep();
    digitalWrite(rbgGreen, HIGH);
   }
   // Pink
   else if (output == "4"){
    digitalWrite(rbgRed, LOW);
    digitalWrite(rbgBlue, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(6, 1);
    lcd.print("Pink");
    dropper2.write(30);
    beep();
    digitalWrite(rbgRed, HIGH);
    digitalWrite(rbgBlue, HIGH);
   }
   // Red
   else if (output == "5"){
    digitalWrite(rbgRed, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(6, 1);
    lcd.print("Red");
    dropper2.write(40);
    beep();
    digitalWrite(rbgRed, HIGH);
   }
   // Yellow
   else if (output == "6"){
    digitalWrite(rbgRed, LOW);
    digitalWrite(rbgGreen, LOW);
    lcd.setCursor(0, 0);
    lcd.print("The colour is ->");
    lcd.setCursor(5, 1);
    lcd.print("Yellow");
    dropper2.write(50);
    beep();
    digitalWrite(rbgRed, HIGH);
    digitalWrite(rbgGreen, HIGH);
   }
   delay(3000);
   digitalWrite(runningLight, LOW);
   sweep();
}

inline void beep(){
  digitalWrite(buzzer, HIGH);
  delay(100);
  digitalWrite(buzzer, LOW);
  delay(100);
  digitalWrite(buzzer, HIGH);
  delay(100);
  digitalWrite(buzzer, LOW);
}

inline void sweep(){
  for (int i = 0;i <= 90; i++){
    dropper1.write(i);
    delay(10);
    }
   dropper1.write(0);
}
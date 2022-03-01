//전압 A0
int sa0 = A0;
//전압ref A1
int sa1 = A1;
// 전류 A2
int sa2 = A2;
// 기울기-x A3
int sa3 = A3;
// 기울기 -y A4
int sa4 = A4;
//습도 A5
int sa5 = A5;
// 온도 -r권선 A6
int sa6 = A6;
//온도-상부베어링 A7
int sa7 = A7;
String response = "";
void setup() {
Serial.begin(115200);
Serial.setTimeout(1);
//Serial.println();
//delay(1000);
}
void loop() {
  // esp센서 ==================================== //
  String espid = "id001";
  Serial.print(espid);
  Serial.print(" ");
  delay(100);
  //전압센서 ===================================== //
  int Valtage = analogRead(sa0);
  Serial.print(Valtage, DEC); //print the value to serial
  Serial.print(" ");
  delay(100);
  //전압ref 센서======================================//
 int Valtage_ref = analogRead(sa1);
 Serial.print(Valtage_ref, DEC); //print the value of serial
 Serial.print(" ");
 delay(100);
 //전류센서 ====================================//
 int current_t = analogRead(sa2);
 Serial.print(current_t, DEC); //print the value to serial
 Serial.print(" ");
 delay(100);
 //기울기_x 센서 ==================================//
 int grad_X = analogRead(sa3);
 Serial.print(grad_X, DEC); //print the value to serial
 Serial.print(" ");
 delay(100);
 //기울기_Y 센서 ===================================//
 int grad_Y = analogRead(sa4);
 Serial.print(grad_Y, DEC); //print the value to serial
 Serial.print(" ");
 delay(100);
 //습도센서 ===================================//
 int Humidity = analogRead(sa5);
Serial.print(Humidity,DEC); //print the value to serial
Serial.print(" ");
delay(100);
//온도-R권선센서//
int Temperature_R = analogRead(sa6);
Serial.print(Temperature_R,DEC);
Serial.print(" ");
delay(100);
//온도-상부베어링센서//
int Temperature_UB = analogRead(sa7);
Serial.print(Temperature_UB,DEC); //print the value to serial
Serial.print(" ");
delay(100);
Serial.print('\n');
delay(5000);
}

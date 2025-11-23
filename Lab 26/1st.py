import serial
import time

ser = serial.Serial('COM7', 9600, timeout=1)  # Update COM port
time.sleep(2)  # Allow time for connection setup

while True:
    command = input("Enter command (ON/OFF): ").strip()
    if command in ["ON", "OFF"]:
        ser.write((command + '\n').encode())  # Send command
        print(f"Sent: {command}")
    else:
        print("Invalid command. Enter ON or OFF.")

ser.close()

#Arduino Code:
# void setup() {
#     Serial.begin(9600);
#     pinMode(13, OUTPUT);
# }

# void loop() {
#     if (Serial.available() > 0) {
#         String command = Serial.readStringUntil('\n');
#         command.trim();

#         if (command == "ON") {
#             digitalWrite(13, HIGH);
#             Serial.println("LED Turned ON");
#         } else if (command == "OFF") {
#             digitalWrite(13, LOW);
#             Serial.println("LED Turned OFF");
#         }
#     }
# }

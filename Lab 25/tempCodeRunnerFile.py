import serial
import time

ser = serial.Serial('COM7', 9600)
time.sleep(2)

while True:
    message = input("Enter message: ")
    ser.write((message + '\n').encode())
    print(ser.readline().decode().strip())

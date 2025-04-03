import serial

SERIAL_PORT = 'COM3' #COM3 on the arudino ide
BAUD_RATE = 115200 #matching to baud rate in ide
TIMEOUT = 1

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = 1)

print("listening for ESP32 sensor data")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print("received data: ", line)

            sensor_data = line.encode('utf-8')

except KeyboardInterrupt:
    print("stopped listening")
    ser.close()
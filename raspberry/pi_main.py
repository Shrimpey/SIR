import serial

if __name__ == "__main__":
    com = serial.Serial("/dev/serial0", 115200)
    
    while True:
        print(com.readline())

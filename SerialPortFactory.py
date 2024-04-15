import serial


class SerialPortFactory:
    @staticmethod
    def create(port):
        return serial.Serial(port, baudrate=9600, timeout=1)
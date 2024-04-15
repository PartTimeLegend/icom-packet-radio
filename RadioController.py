from SerialPortFactory import SerialPortFactory


class RadioController:
    def __init__(self, port):
        self.port = port
        self.serial = SerialPortFactory.create(port)

    def send_packet_data(self, data):
        self.serial.write(data.encode())

    def receive_packet_data(self):
        return self.serial.readline().decode().strip()

    def close(self):
        self.serial.close()

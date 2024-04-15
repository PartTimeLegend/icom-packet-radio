from RadioDetector import RadioDetector


import serial.tools.list_ports


class IcomRadioDetector(RadioDetector):
    def detect_radios(self):
        radios = []
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            if self.is_radio(desc):
                radios.append(port)
        return radios

    def is_radio(self, description):
        return "icom" in description.lower()
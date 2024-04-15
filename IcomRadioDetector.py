import serial.tools.list_ports

from RadioDetector import RadioDetector


class IcomRadioDetector(RadioDetector):
    def detect_radios(self):
        radios = []
        ports = serial.tools.list_ports.comports()
        # trunk-ignore(ruff/B007)
        for port, desc, hwid in sorted(ports):
            if self.is_radio(desc):
                radios.append(port)
        return radios

    def is_radio(self, description):
        return "icom" in description.lower()

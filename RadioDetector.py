class RadioDetector:
    def detect_radios(self):
        raise NotImplementedError("Subclasses must implement detect_radios method")

    def is_radio(self, description):
        raise NotImplementedError("Subclasses must implement is_radio method")

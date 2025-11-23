class Settings:
    def __init__(self, day_nom, night_nom):
        self.voltage = 0.0
        self.mode = "Off"
        self.day_nom = day_nom
        self.night_nom = night_nom
        self.day_night_limit = (day_nom - night_nom) / 2 + night_nom
        
    def set_voltage(self, voltage):
        self.voltage = voltage
        if voltage == 0.0:
            elf.mode = "Off"
        elif voltage > self.day_night_limit:
            self.mode = "Day"
        else:
            self.mode = "Night"
        
    def get_voltage(self):
        return self.voltage
        
    def set_mode(self, mode):
        if mode == "Day":
            self.mode = "Day"
            self.voltage = self.day_nom
        elif mode == "Night":
            self.mode = "Night"
            self.voltage = self.night_nom
        else:
            self.mode = "Off"
            self.voltage = 0.0
        
    def get_mode(self):
        return self.mode



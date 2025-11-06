class Menu:
    def __init__(self, display):
        self.display = display
        self.current_menu = "main"  # Das Hauptmenü
        self.current_option = 0
        self.menus = {
            "main": {
                "options": ["Tag", "Nacht", "Aus", "Blinken", "U/I-Kennlinie", "Einstellungen"]
            },
            "settings": {
                "options": ["Helligkeit", "Sprache", "Zurück"]
            },
        }
        
    def display_start(self, voltage, current, power, mode):
        self.display.putstr(str(voltage) + " V")
        self.display.putstr("       ")
        self.display.putstr(mode)
        self.display.putstr(" ")
        self.display.putstr(str(current) + " A")
        self.display.putstr("    ")
        self.display.putstr(str(power) + " W")
        
    def display_menu(self, current_option):
        """ Zeigt das aktuelle Menü mit der markierten Option an. """
        menu = self.menus[self.current_menu]
        options = menu["options"]

        self.current_option = current_option
        
        # Zeige den Titel und die beiden Optionen auf dem Display
        self.display.clear()
        
        # Wenn mehr als 2 Optionen vorhanden sind, zeige die zweite Zeile
        if current_option + 1 < len(options):
            self.display.putstr(options[current_option] + "\n" + options[current_option + 1])
        else:
            self.display.putstr(options[current_option])

    def navigate(self, option_number):
        """ Navigiere zu der ausgewählten Option (z.B. Untermenü aufrufen). """
        menu = self.menus[self.current_menu]
        if option_number == len(menu["options"]) - 1:  # Wenn "Zurück" oder ein spezielles Menü gewählt wird
            self.current_menu = "settings"
        else:
            self.handle_option(option_number)

    def handle_option(self, option_number):
        """ Logik für die ausgewählte Option. """
        if option_number == 0:
            self.display.show_message("Option 1 ausgewählt")
        elif option_number == 1:
            self.display.show_message("Option 2 ausgewählt")
            
    def get_current_menu(self):
        return self.current_menu, self.current_option

    


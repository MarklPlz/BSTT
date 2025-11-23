class UserInput:
    def __init__(self, lcd_display, menu):
        self.lcd_display = lcd_display
        self.menu = menu

    def cw(self):
        self.menu.current_option = max(0, self.menu.current_option - 1)
        self.menu.display_menu(self.menu.current_option)

    def ccw(self):
        self.menu.current_option = min(len(self.menu.menus[self.menu.current_menu]["options"]) - 1, self.menu.current_option + 1)
        self.menu.display_menu(self.menu.current_option)

    def sw_press(self):
        self.menu.navigate(self.menu.current_option)

    def sw_release(self):
        print("unused yet")

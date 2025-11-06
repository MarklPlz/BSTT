class UserInput:
    def __init__(self, lcd_display, menu):
        self.lcd_display = lcd_display
        self.menu = menu

    def move_up(self):
        self.current_option = max(0, self.current_option - 1)
        self.menu.display_menu(self.current_option)

    def move_down(self):
        self.current_option = min(len(self.menu.menus[self.menu.current_menu]["options"]) - 1, self.current_option + 1)
        self.menu.display_menu(self.current_option)

    def select_option(self):
        self.menu.navigate(self.current_option)


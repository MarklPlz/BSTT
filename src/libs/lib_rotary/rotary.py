from machine import Pin, Timer

class Rotary:
    
    def __init__(self, pin_dt, pin_clk, pin_sw, parent):
        self.dt = pin_dt
        self.clk = pin_clk
        self.sw = pin_sw
        self.last_rotary = False
        self.last_sw = False
        self.t_sw = Timer(freq=10, mode=Timer.PERIODIC, callback=self._handle_sw)
        self.t_rotary = Timer(freq=200, mode=Timer.PERIODIC, callback=self._handle_rotary)
        self.parent = parent   # parent receives callback events
    
    def _handle_sw(self, timer):
        if not self.sw.value() and not self.last_sw:
            self.parent.sw_press()
            self.last_sw = True
        if self.sw.value() and self.last_sw:
            self.parent.sw_release()
            self.last_sw = False

    def _handle_rotary(self, pin):
        if self.dt.value() and not self.clk.value() and self.last_rotary:
            self.parent.cw()
            self.last_rotary = False
        if self.clk.value() and not self.dt.value() and self.last_rotary:
            self.parent.ccw()
            self.last_rotary = False
        if self.dt.value() and self.clk.value() and not self.last_rotary:
            self.last_rotary = True

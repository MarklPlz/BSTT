from machine import Pin, Timer

class Rotary:
    
    def __init__(self, dt, clk, sw, callbacks):
        self.clk = Pin(clk, Pin.IN)
        self.dt = Pin(dt, Pin.IN)
        self.sw = Pin(sw, Pin.IN)
        self.last_rotary = False
        self.last_sw = False
        self.t_sw = Timer(freq=10, mode=Timer.PERIODIC, callback=self.handle_sw)
        self.t_rotary = Timer(freq=200, mode=Timer.PERIODIC, callback=self.handle_rotary)
        self.callback_cw = callbacks[0]
        self.callback_ccw = callbacks[1]
        self.callback_sw_press = callbacks[2]
        self.callback_sw_release = callbacks[3]
    
    def handle_sw(self, timer):
        if not self.sw.value() and not self.last_sw:
            self.callback_sw_press()
            self.last_sw = True
        if self.sw.value() and self.last_sw:
            self.callback_sw_release()
            self.last_sw = False

    def handle_rotary(self, pin):
        if self.dt.value() and not self.clk.value() and self.last_rotary:
            self.callback_cw()
            self.last_rotary = False
        if self.clk.value() and not self.dt.value() and self.last_rotary:
            self.callback_ccw()
            self.last_rotary = False
        if self.dt.value() and self.clk.value() and not self.last_rotary:
            self.last_rotary = True

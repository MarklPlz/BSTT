# To do
- On/Off
- U/I graph
- set voltage
- show voltage and current
- show power
- show input voltage
- add lcd screen - https://github.com/dhylands/python_lcd/tree/master
- add rotary encoder
- add INA219 sensor
- add DC-link powerup
- add microSD reader
- add multicore support

## Rotary
``` Python
def rotary_cw():
    print("rotary_cw")

def rotary_ccw():
    print("rotary_ccw")
    
def sw_pressed():
    print("sw_pressed")

def sw_release():
    print("sw_release")


# List of callback functions for each button
callbacks = [rotary_cw, rotary_ccw, sw_pressed, sw_release]

rotary = Rotary(pin_dt, pin_clk, pin_sw, callbacks)
```

import machine
import time
import math
import config as cfg
from libs.lib_lcd.machine_i2c_lcd import I2cLcd
from libs.lib_rotary.rotary import Rotary
import utils.menu as menu

# ===============================
# FUNCTIONS
# ===============================
    
def set_duty(Timer):
    # Elapsed time from start
    index = int(time.ticks_us() / 100)  # convert to index
    pwm_value = SINE_LUT[index % cfg.SINE_LUT_SIZE]
    pwm.duty_u16(pwm_value)
    
def rotary_cw():
    lcd.clear()
    lcd.putstr("rotary_cw")

def rotary_ccw():
    lcd.clear()
    lcd.putstr("rotary_ccw")
    
def sw_pressed():
    lcd.clear()
    lcd.putstr("sw_pressed")

def sw_release():
    lcd.clear()
    lcd.putstr("sw_release")

# ===============================
# SETUP
# ===============================

# create PWM object, set frequency(Hz) and duty(0-65535)
pwm = machine.PWM(cfg.PIN_PWM, freq=cfg.FREQ_PWM, duty_u16=0)

# create a lookup-table for a rectified sine
# the values are already calculated for the pwm duty
SINE_LUT = [int(math.sin(math.radians(i * (180/cfg.SINE_LUT_SIZE)))*65535) for i in range(cfg.SINE_LUT_SIZE)]

# List of callback functions for each button
callbacks = [rotary_cw, rotary_ccw, sw_pressed, sw_release]
# init rotary encoder
rotary = Rotary(cfg.PIN_ROTARY_DT, cfg.PIN_ROTARY_CLK, cfg.PIN_ROTARY_SW, callbacks)

# init i2c
i2c = machine.I2C(0, sda=cfg.PIN_I2C_SDA, scl=cfg.PIN_I2C_SCL, freq=100000)
# Init LCD 
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Init PWM Timer
tim = machine.Timer(freq=cfg.FREQ_TIMER, mode=machine.Timer.PERIODIC, callback=set_duty)

menu = menu.Menu(lcd)

voltage = 12.3
current = 1.7
power = 19.8
mode = "Tag"
menu.display_start(voltage, current, power, mode)
# ===============================
# MAIN LOOP
# ===============================

def loop():
    # Elapsed time from start
    index = int(time.ticks_us() / 100)  # convert to index

    pwm_value = SINE_LUT[index % cfg.SINE_LUT_SIZE]
    pwm.duty_u16(pwm_value)


# ===============================
# ENTRY POINT
# ===============================

def main():
    try:
        while True:
            loop()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        pwm.duty_u16(0)
        pwm.deinit()
        print("Execution finished.")

if __name__ == "__main__":
    main()

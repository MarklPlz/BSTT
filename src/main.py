from machine import Pin, PWM, Timer
import time
import math

# ===============================
# CONFIGURATION
# ===============================

PIN_PWM = Pin(0)
FREQ_PWM = 25000

SINE_LUT_SIZE = 100 # Signal samples
FREQ_SIGNAL = 100
FREQ_TIMER = FREQ_SIGNAL * SINE_LUT_SIZE

# ===============================
# FUNCTIONS
# ===============================
    
def set_duty(Timer):
    # Elapsed time from start
    index = int(time.ticks_us() / 100)  # convert to index
    pwm_value = SINE_LUT[index % SINE_LUT_SIZE]
    pwm.duty_u16(pwm_value)
    
# ===============================
# SETUP
# ===============================

# create PWM object, set frequency(Hz) and duty(0-65535)
pwm = PWM(PIN_PWM, freq=FREQ_PWM, duty_u16=0)

# create a lookup-table for a rectified sine
# the values are already calculated for the pwm duty
SINE_LUT = [int(math.sin(math.radians(i * (180/SINE_LUT_SIZE)))*65535) for i in range(SINE_LUT_SIZE)]


def setup():
    print()
    tim = Timer(freq=FREQ_TIMER, mode=Timer.PERIODIC, callback=set_duty)
    
# ===============================
# MAIN LOOP
# ===============================

def loop():
    # Elapsed time from start
    index = int(time.ticks_us() / 100)  # convert to index

    pwm_value = SINE_LUT[index % SINE_LUT_SIZE]
    pwm.duty_u16(pwm_value)


# ===============================
# ENTRY POINT
# ===============================

def main():
    try:
        setup()
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

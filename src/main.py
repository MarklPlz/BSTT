from machine import Pin, PWM
import time
import math

# ===============================
# CONFIGURATION
# ===============================

PWM_PIN = Pin(0)
PWM_FREQ = 25000

# 100Hz signal / 100 samples -> 100us resolution
SINE_LUT_SIZE = 100

# ===============================
# SETUP
# ===============================

# create PWM object, set frequency(Hz) and duty(0-65535)
pwm = PWM(PWM_PIN, freq=PWM_FREQ, duty_u16=0)

# create a lookup-table for a rectified sine
# the values are already calculated for the pwm duty
SINE_LUT = [int(math.sin(math.radians(i * (180/SINE_LUT_SIZE)))*65535) for i in range(SINE_LUT_SIZE)]

def setup():
    print()

    
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

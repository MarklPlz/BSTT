import machine

# ===============================
# CONFIGURATION
# ===============================

# Pins
PIN_I2C_SCL = machine.Pin(5)
PIN_I2C_SDA = machine.Pin(4)
PIN_SPI_TX = machine.Pin(19)
PIN_SPI_SCK = machine.Pin(18)
PIN_SPI_CSn = machine.Pin(17)
PIN_SPI_RX = machine.Pin(16)
PIN_ROTARY_CLK = machine.Pin(6, machine.Pin.IN)
PIN_ROTARY_DT = machine.Pin(7, machine.Pin.IN)
PIN_ROTARY_SW = machine.Pin(8, machine.Pin.IN)
PIN_PWM = machine.Pin(15)


FREQ_PWM = 25000

SINE_LUT_SIZE = 100 # Signal samples
FREQ_SIGNAL = 100
FREQ_TIMER = FREQ_SIGNAL * SINE_LUT_SIZE


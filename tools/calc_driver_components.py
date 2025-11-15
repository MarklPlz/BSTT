import math

V_CC = 5               # Supply voltage
V_bootdiode = 0.525     # Gorward voltage drop across boot diode
Q_g = 48e-9             # Gate charge of mosfet
C_iss = 1700e-12        # Input Capacitance
L_S = 7.5e-9            # Internal Source Inductance
f_R = 300e3             # Ring frequency, needs to be measured
Q = 1/(math.sqrt(2))    # Butterworth

L_S = 1/(C_iss*(2*math.pi*f_R)**2)
C_g = Q_g / (V_CC - V_bootdiode)
C_boot = 10 * C_g
C_VCC = 10 * C_boot
R_G = (2*math.pi*f_R*L_S)/Q

print("Bootstrap Capacitor:", round(C_boot * 1e9), "nF")
print("VDD Bypass Capacitor:", round(C_VCC * 1e9), "nF")
print("Gate Resistor:", round(R_G,1), "Ohm")

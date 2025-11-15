import math

f_pwm = 25e3    # pwm frequency
f_s = 100       # signal frequency
f_0 = math.sqrt(f_pwm * f_ns)

R_L = 10    # load resistance

Q = 1/math.sqrt(2)  # Butterworth filter
L = 1/(2*math.pi*f_0*(1/R_L))
C = (Q/R_L)**2*L

print("LC-Filter")
print("~~~~~~~~~")
print("Cutoff frequency:", round(f_0), "Hz")
print("C:", round(C*1e6,2), "µF")
print("L:", round(L*1e3,2), "mH")
print()


Q = 0.35
L2 = (3*Q*R_L)/(4*math.pi*f_0)
L1 = 2*L2 # coil closer to switch should have bigger inductance (2-10x)
C = (2*L1**2)/(3*L1*(Q*R_L)**2)

print("LCL-Filter")
print("~~~~~~~~~~")
print("Cutoff frequency:", round(f_0), "Hz")
print("C:", round(C*1e6,2), "µF")
print("L1:", round(L1*1e3,2), "mH")
print("L2:", round(L2*1e3,2), "mH")

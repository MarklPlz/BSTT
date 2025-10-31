import sympy as sp
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import bode_plot, step_response_plot
import matplotlib.pyplot as plt

# Define symbols
s = sp.symbols('s', complex=True)
R1, R2, L, C = sp.symbols('R1 R2 L C', positive=True, real=True)


# Define the transfer function
# V_in ---- Z1 ----+---- V_out
#                  |
#                  Z2
#                  |
# GND -------------+----

Z1 = R1 + s*L
Z2 = (R2*1/(s*C))/(R2+1/(s*C))
num = Z2
den = Z1+Z2
H = TransferFunction(num, den, s)


# Substitute numeric values
R1_val = 0.277
R2_val = 10
C_val = 5e-6
L_val = 1e-3
H_num = H.subs({R1: R1_val, R2: R2_val, L: L_val, C: C_val})

R2_val = 5.71
H_num1 = H.subs({R1: R1_val, R2: R2_val, L: L_val, C: C_val})
R2_val = 20
H_num2 = H.subs({R1: R1_val, R2: R2_val, L: L_val, C: C_val})


# Bode Plot
fig = plt.figure("Bode Plot")
bode_plot(H_num, show=False, freq_unit='Hz' ,phase_unit='deg', initial_exp=0, final_exp=6, color='tab:blue')
bode_plot(H_num1, show=False, freq_unit='Hz' ,phase_unit='deg', initial_exp=0, final_exp=6, color='tab:orange')
bode_plot(H_num2, show=False, freq_unit='Hz' ,phase_unit='deg', initial_exp=0, final_exp=6, color='tab:green')


# Add vertical line at desired frequency (in rad/s)
f_c = 1 / (2*sp.pi*sp.sqrt(C_val*L_val))
axes = fig.axes  # [magnitude_axis, phase_axis]
for ax in axes:
    ax.axvline(100, color='m', alpha=0.5, linestyle='--')
    ax.axvline(25000, color='m', alpha=0.5, linestyle='--')
    ax.axvline(f_c, color='k', alpha=0.5, linestyle='--')


# Step Response
plt.figure("Step Response")
step_response_plot(H_num, show=False, upper_limit=0.002, color='tab:blue')
step_response_plot(H_num1, show=False, upper_limit=0.002, color='tab:orange')
step_response_plot(H_num2, show=False, upper_limit=0.002, color='tab:green')


plt.show()

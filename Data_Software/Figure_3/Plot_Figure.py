import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def power_law(h, p1):
    return p1 * h ** 0.5


fig, ax = plt.subplots()

height = [46, 66, 87, 93, 106]  # nm
max_width = [4, 6, 7, 7, 8]  # um

param, covariance = curve_fit(power_law, height, max_width, p0=[1])  # p0 = initial guess
error = np.sqrt(np.diag(covariance))

print(f"a = {param[0]:.4f} +/- {error[0]:.4f}")

h_fit = np.linspace(40, 110, 100, endpoint=True)
w_fit = param[0] * h_fit ** 0.5

ax.plot(h_fit, w_fit, color="C0")
ax.errorbar(height, max_width, xerr=10, yerr=1, marker='o', linestyle='')

plt.xlim(35, 117)
plt.ylim(2.5, 9.5)

plt.show()

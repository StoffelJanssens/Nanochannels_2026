import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def power_law(time, p1, p2):
    return p1 * time ** p2


fig, ax = plt.subplots()

# data 1 -- 25 times filling channel 1
frame = np.array([1, 3, 5])
t = frame / 30
pixel = np.array([203, 387, 471])
x = pixel * 200 / 502

params, covariance = curve_fit(power_law, t, x, p0=[1, 1])  # p0 = initial guess
param_1, param_2 = params
errors = np.sqrt(np.diag(covariance))  # standard errors on a and b

print("25 times channel 1")
print(f"a = {param_1:.4f} +/- {errors[0]:.4f}")
print(f"b = {param_2:.4f} +/- {errors[1]:.4f}")

t_fit = np.linspace(0, 0.180, 100, endpoint=True)
x_fit = param_1 * t_fit ** param_2

ax.errorbar(t, x, xerr=0.015, yerr=10, marker='o', linestyle='')
ax.plot(t_fit, x_fit, color="C0")

# data 2 -- 25 times filling channel 2
frame = np.array([1, 3, 5, 7, 9, 11, 13, 17, 21, 27, 33, 39, 59])
t = frame / 30
pixel = np.array([42, 75, 94, 108, 133, 152, 166, 200, 232, 278, 313, 353, 478])
x = pixel * 200 / 506

params, covariance = curve_fit(power_law, t, x, p0=[1, 1])  # p0 = initial guess
param_1, param_2 = params
errors = np.sqrt(np.diag(covariance))  # standard errors on a and b

print("25 times channel 2")
print(f"a = {param_1:.4f} +/- {errors[0]:.4f}")
print(f"b = {param_2:.4f} +/- {errors[1]:.4f}")

t_fit = np.linspace(0, 2.2, 100, endpoint=True)
x_fit = param_1 * t_fit ** param_2

ax.errorbar(t, x, xerr=0.015, yerr=10, marker='o', linestyle='', color="C1")
ax.plot(t_fit, x_fit, color="C1")

# data 3 -- 50 times filling channel 1
frame = np.array([1, 3, 5, 7, 9, 13])
t = frame / 30
pixel = np.array([383, 556, 669, 736, 800, 955])
x = pixel * 200 / 1013

params, covariance = curve_fit(power_law, t, x, p0=[1, 1])  # p0 = initial guess
param_1, param_2 = params
errors = np.sqrt(np.diag(covariance))  # standard errors on a and b

print("50 times channel 1")
print(f"a = {param_1:.4f} +/- {errors[0]:.4f}")
print(f"b = {param_2:.4f} +/- {errors[1]:.4f}")

t_fit = np.linspace(0, 0.5, 100, endpoint=True)
x_fit = param_1 * t_fit ** param_2

ax.errorbar(t, x, xerr=0.015, yerr=10, marker='^', linestyle='', color="C0")
ax.plot(t_fit, x_fit, color="C0")

# data 4 -- 50 times filling channel 2
frame = np.array([20, 40, 60, 80, 100, 120, 140])
t = frame / 30
pixel = np.array([83, 200, 320, 422, 539, 640, 740])
x = pixel * 200 / 1013

params, covariance = curve_fit(power_law, t, x, p0=[1, 1])  # p0 = initial guess
param_1, param_2 = params
errors = np.sqrt(np.diag(covariance))  # standard errors on a and b

print("50 times channel 2")
print(f"a = {param_1:.4f} +/- {errors[0]:.4f}")
print(f"b = {param_2:.4f} +/- {errors[1]:.4f}")

t_fit = np.linspace(0, 4.8, 100, endpoint=True)
x_fit = param_1 * t_fit ** param_2

ax.errorbar(t, x, xerr=0.015, yerr=10, marker='^', linestyle='', color="C1")
ax.plot(t_fit, x_fit, color="C1")

plt.xlim(-0.1, 4.9)
plt.ylim(0, 205)

plt.show()

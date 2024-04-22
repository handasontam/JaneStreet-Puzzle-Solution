import scipy.integrate as integrate
import scipy.special as special
from scipy.optimize import minimize_scalar
import numpy as np

def f(r_1):
    return integrate.quad(lambda r: 2*r/np.pi * np.arccos(np.sqrt(r_1 * (2 * r - r_1))/r), r_1/2, 1, epsabs=1e-30, epsrel=1e-30)[0] + (r_1**2)/4

res = minimize_scalar(f, bounds=(0,1), method='bounded')


print("Erwin should choose r_1 = ", res.x)  # 0.5013067075684123
print(f"The best response of Aaron is to choose r_2 = 0 if r < (r_1)/2 and choose r_2 = sqrt(r_1 * (2r - r_1)) if (r_1)/2 < r < 1")
print("Erwin's win probability is ", 1-res.fun)  # 0.8338135135259306
print("Aaron's win probability is ", res.fun)  # 0.16618648647406942

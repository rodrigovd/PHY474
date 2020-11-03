import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats
import scipy.constants as sc

dielectric_constant=np.array([1.00059 ,2.8, 3, 3.8, 7.3])
phase = np.array([0, 185.5, 399.25, 552.75, 968.25])
material =np.array(["Air","Nylon","Wood", "Delrin","Glass"])

def k():
    m, b, r_value, p_value, std_err = stats.linregress(phase, dielectric_constant)
    return m, b
import numpy as np
import pandas as pd
from scipy import stats
import scipy.constants as sc


'''This function takes the values from Dielectric Constant Data.csv and
   calculates the calibration equation to obtain elctron density.
'''
data = pd.DataFrame("Dielectric Constant Data.csv",delimiter='\t')
dielectric_constant = data['Dielectric Constant']
phase = data['Avg. Phase']

def k():
    m, b, r_value, p_value, std_err = stats.linregress(phase, dielectric_constant)
    return m, b

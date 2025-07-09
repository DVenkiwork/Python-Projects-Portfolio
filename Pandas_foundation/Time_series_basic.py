# Objective: Time series basic functionalities
import numpy as np 
import pandas as pd 
import datetime 

# Parsing time series information from various sources and formats
dti = pd.to_datetime(["1/1/2018", np.datetime64("2018-01-01"), datetime.datetime(2018, 1, 1)])
print("Parsing time series information from various sources and formats")
print(f"{dti=}")

# Generate sequences of fixed-frequency dates and time spans
dti = pd.date_range("2018-01-01", periods=3, freq="M")
print("Generate sequences of fixed-frequency dates and time spans")
print(f"{dti=}")

# Manipulating and converting date times with timezone information
print("Manipulating and converting date times with timezone information")
dti = dti.tz_localize("UTC")
print(f"{dti=}")
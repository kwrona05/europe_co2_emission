import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('europe_co2_emissions.csv')
data.describe()
print(data)
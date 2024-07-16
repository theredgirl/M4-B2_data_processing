import numpy as np
import pandas as pd
x = pd.ExcelFile("070124_m4_raw.xlsx")
names = x.sheet_names

print(names)
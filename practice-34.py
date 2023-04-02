import pandas as pd
import numpy as np

data = {"physic": [18, 12, 19],
        "chemistry": [16.25, 15, 20],
        "math": [14, 13, 18],
        "literature": [17, 15, 17]}

data_f = pd.DataFrame(data, index=["ali", "mohammad", "reza"])
mat = np.cov(data_f)

print(data_f.describe())
print(mat)

import matplotlib as mpl

import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

df = pd.DataFrame({'date': np.array([datetime.datetime(2020, 1, i+1)
                                     for i in range(12)]),
                   'status': [3, 4, 4, 7, 8, 9, 14, 17, 12, 8, 8, 13]})

plt.plot(df.date, df.status)
plt.show()
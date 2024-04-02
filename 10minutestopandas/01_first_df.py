import numpy as np
import pandas as pd

# s = pd.Series([1, 2, 5, np.nan, 9])
# s

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
df

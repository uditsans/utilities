# PyTest
import pytest

# Numpy
import numpy as np

def test_numpy():
    assert np.power(2,3) == 8

# Pandas
import pandas as pd
def test_pandas():
    power_list = pd.Series([np.power(2, i) for i in range(5)])
    x = np.random.randint(0,4)
    assert power_list[x] == np.power(2,x)
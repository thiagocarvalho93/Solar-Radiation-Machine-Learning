import pandas as pd

df = pd.read_table('table1.dat', delimiter=',', skiprows=[0,2]).drop(0)


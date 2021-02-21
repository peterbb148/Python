import pandas as pd
pd.read_csv('AAB.csv', header=None).T.to_csv('output.csv', header=False, index=False)
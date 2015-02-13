import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('test.csv', names=['run', 'threads', 'tps'])

data = {
    'run_1': df[df.run.isin(['run_1'])].groupby('threads').tps.mean(),
    'run_2': df[df.run.isin(['run_2'])].groupby('threads').tps.mean(),
    'run_3': df[df.run.isin(['run_3'])].groupby('threads').tps.mean(),
    'run_4': df[df.run.isin(['run_4'])].groupby('threads').tps.mean()
}

index = sorted(df.threads.unique())
columns = sorted(df.run.unique())
df = pd.DataFrame(data=data, index=index, columns=columns)
df.plot()
plt.show()
